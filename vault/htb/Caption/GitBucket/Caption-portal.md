This seems to be the service that runs in the port 80, although this is probably a development environment. I did use the token i had in order to change the webpage, but that was not reflected in the web server.

### MENTIONED SERVICES

In some of the configuration files some ports are mentioned as backend services. These are the following:

- 127.0.0.1:6081
- localhost:6081
- localhost: 6082
- localhost:8000

### MENTIONED SECRETS 

/etc/ssl/certs
/et/ssl/private

### CONTENT REVIEW

There seems to be nothing of value in the /app directory.

In the /config files there are mentions of other services (above). Also, the host seems to use **varnish 4.0** and **haproxy** (the latter with no sand boxing or restricted access)

https://gist.github.com/ndavison/4c69a2c164b2125cd6685b7d5a3c135b


### EXPERIMENTAL 

```
HTTP/1.1 200 OK
server: Werkzeug/3.0.1 Python/3.10.12
date: Mon, 23 Sep 2024 10:27:14 GMT
content-type: text/html; charset=utf-8
content-length: 4412
x-varnish: 1213450
age: 0
via: 1.1 varnish (Varnish/6.6)

```

### LITERALLY THE PASSWORD IS IN A COMMIT

```
        user margo insecure-password vFr&cS2#0!
```

CVE-2021-36740
https://github.com/detectify/Varnish-H2-Request-Smuggling
https://labs.detectify.com/how-to/set-up-docker-for-varnish-http-2-request-smuggling/
