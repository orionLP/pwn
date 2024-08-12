**-----------------------------------------------------------------------------------------**
**mysql** 

```txt
database: usage_blog
user: staff
password: s3cr3t_c0d3d_1uth
```
**-----------------------------------------------------------------------------------------**
**monit**

```txt
port: 2812 
host: localhost
user: admin
password: 3nc0d3d_pa$$w0rd
```
**-----------------------------------------------------------------------------------------**
**api key auth.usage.htb**

```txt
APP_KEY: base64:oMsNNEsunFZxVvNVc0pfq7Gbn8hWGURpQLAgH6/dktA=
```
**-----------------------------------------------------------------------------------------**
**api key auth.usage.htb**

```txt
APP_KEY: base64:pP77nTMTmggnX1939G4nPjHgxwidMjhZUGj1AFhARgE=
```
**-----------------------------------------------------------------------------------------**

## HASHES

**-----------------------------------------------------------------------------------------**
Found in the usage_blog database

```json
{"name":"Administrator","password":"$2y$10$E9.N1P92fYSjJGQDfBrUaO05EHW4BxiQITrqjde\/WQMKnAQ7k2HJK","password_confirmation":"$2y$10$E9.N1P92fYSjJGQDfBrUaO05EHW4BxiQITrqjde\/WQMKnAQ7k2HJK","_token":"PQqkHdjeUpzpIB8ykD7YbMdBziQx1H9xUdwBSS02","_method":"PUT"}
```

```sql
/admin.usage.blog

admin : $2y$10$ohq2kLpBH/ri.P5wR0P3UOmc24Ydvl9DA9H1S6ooOMgH5xVfUPrL2

/other

mysql> SELECT * FROM users;
+----+--------+---------------+-------------------+--------------------------------------------------------------+----------------+---------------------+---------------------+
| id | name   | email         | email_verified_at | password                                                     | remember_token | created_at          | updated_at          |
+----+--------+---------------+-------------------+--------------------------------------------------------------+----------------+---------------------+---------------------+
|  1 | raj    | raj@raj.com   | NULL              | $2y$10$7ALmTTEYfRVd8Rnyep/ck.bSFKfXfsltPLkyQqSp/TT7X1wApJt4. | NULL           | 2023-08-17 03:16:02 | 2023-08-17 03:16:02 |
|  2 | raj    | raj@usage.htb | NULL              | $2y$10$rbNCGxpWp1HSpO1gQX4uPO.pDg1nszoI/UhwHvfHDdfdfo9VmDJsa | NULL           | 2023-08-22 08:55:16 | 2023-08-22 08:55:16 |
|  3 | x      | x@gmail.com   | NULL              | $2y$10$qC8tKqmI6rX48gNDdc2Os.fx.6H3jjovV3WPlgTll2Pth0slMXA5m | NULL           | 2024-08-09 20:28:37 | 2024-08-09 20:28:37 |
|  4 | skg    | skg@skg.com   | NULL              | $2y$10$25e7GnQOneJc/Vu27PcVpe9CuV9GkSvX1XZN64QWh8faG4VS9nKqC | NULL           | 2024-08-09 20:56:41 | 2024-08-09 20:56:41 |
|  5 | teekan | tee@kan       | NULL              | $2y$10$DUGxCGZqVmIetBHhYasSSeqTgY4t7ui0/PJjYqy35.fVJSRCoOOMq | NULL           | 2024-08-09 22:03:55 | 2024-08-09 22:03:55 |
|  6 | skg2   | skg2@skg2.com | NULL              | $2y$10$TLy/UBhQyFhIgZQomS98VehMT7QPvJw/8BpZlWHG4.tHt5NTY071W | NULL           | 2024-08-09 22:26:52 | 2024-08-09 22:26:52 |
|  7 | skg3   | skg3@skg3.com | NULL              | $2y$10$Sp.ybKexBePgUwkz/m0JlOYgaPpm5hRhaUTbTaPWs/bxZW6xYw8te | NULL           | 2024-08-09 22:28:20 | 2024-08-09 22:28:20 |
+----+--------+---------------+-------------------+--------------------------------------------------------------+----------------+---------------------+---------------------+

```

**processed hashes**

```txt
$2y$10$dVAYyH/Wj6ri3oFRIC0w9OHkubPpMsyVAeB/Ga/ews2GWpi0DawV.
$2y$10$E9.N1P92fYSjJGQDfBrUaO05EHW4BxiQITrqjde\/WQMKnAQ7k2HJK
$2y$10$ohq2kLpBH/ri.P5wR0P3UOmc24Ydvl9DA9H1S6ooOMgH5xVfUPrL2 
$2y$10$7ALmTTEYfRVd8Rnyep/ck.bSFKfXfsltPLkyQqSp/TT7X1wApJt4.
$2y$10$rbNCGxpWp1HSpO1gQX4uPO.pDg1nszoI/UhwHvfHDdfdfo9VmDJsa
$2y$10$qC8tKqmI6rX48gNDdc2Os.fx.6H3jjovV3WPlgTll2Pth0slMXA5m
$2y$10$25e7GnQOneJc/Vu27PcVpe9CuV9GkSvX1XZN64QWh8faG4VS9nKqC
$2y$10$DUGxCGZqVmIetBHhYasSSeqTgY4t7ui0/PJjYqy35.fVJSRCoOOMq
$2y$10$TLy/UBhQyFhIgZQomS98VehMT7QPvJw/8BpZlWHG4.tHt5NTY071W
$2y$10$Sp.ybKexBePgUwkz/m0JlOYgaPpm5hRhaUTbTaPWs/bxZW6xYw8te
```

```txt
$2y$10$dVAYyH/Wj6ri3oFRIC0w9OHkubPpMsyVAeB/Ga/ews2GWpi0DawV. : admin123
$2y$10$E9.N1P92fYSjJGQDfBrUaO05EHW4BxiQITrqjde\/WQMKnAQ7k2HJK : 123456
$2y$10$ohq2kLpBH/ri.P5wR0P3UOmc24Ydvl9DA9H1S6ooOMgH5xVfUPrL2 : whatever1
$2y$10$7ALmTTEYfRVd8Rnyep/ck.bSFKfXfsltPLkyQqSp/TT7X1wApJt4. : password
$2y$10$rbNCGxpWp1HSpO1gQX4uPO.pDg1nszoI/UhwHvfHDdfdfo9VmDJsa
$2y$10$qC8tKqmI6rX48gNDdc2Os.fx.6H3jjovV3WPlgTll2Pth0slMXA5m
$2y$10$25e7GnQOneJc/Vu27PcVpe9CuV9GkSvX1XZN64QWh8faG4VS9nKqC
$2y$10$DUGxCGZqVmIetBHhYasSSeqTgY4t7ui0/PJjYqy35.fVJSRCoOOMq
$2y$10$TLy/UBhQyFhIgZQomS98VehMT7QPvJw/8BpZlWHG4.tHt5NTY071W
$2y$10$Sp.ybKexBePgUwkz/m0JlOYgaPpm5hRhaUTbTaPWs/bxZW6xYw8te
```



## HAHAH turns out the admin for monit uses the same password as xander hahahha 

We are now user [[xander]].
