Inside gitbucket we can see two repositories:
- Logservice: `A service that helps in logs correlation and much more other tasks`
- Caption-portal: `Portal to manage all your devices in single place.` -> likely the service at port 80.
### CONTENTS FROM FILES 

Let us analyze:
- [[Caption-portal]]
- [[Logservice]]

In the meantime, i also created a token to be able to edit things in this repository:

`5e23ad9d1b452f981cc956c40614d93ae210d629`

### OTHER  INFORMATION

| MODULE_ID      | VERSION |
| -------------- | ------- |
| gitbucket-core | 4.40.0  |
| gist           | 4.23.0  |
| emoji          | 4.6.0   |
| notifications  | 1.11.0  |
| pages          | 1.10.0  |

|Property|Value|
|---|---|
|GITBUCKET_VERSION|4.40.0|
|GITBUCKET_HOME|/home/margo/.gitbucket|
|DATABASE_URL|jdbc:h2:/home/margo/.gitbucket/data;MVCC=true<br><br>GitBucket is using the embedded H2 database. It's recommended that you [configure GitBucket to use an external database](https://github.com/gitbucket/gitbucket/wiki/External-database-configuration) if you're running GitBucket in a production environment.|

The username running this gibucket is margo

| USER_NAME | MAIL_ADDRESS     | PASSWORD                                                                                                        | ADMINISTRATOR | URL                | REGISTERED_DATE       | UPDATED_DATE            | LAST_LOGIN_DATE       | IMAGE  | GROUP_ACCOUNT | FULL_NAME     | REMOVED | DESCRIPTION                |
| --------- | ---------------- | --------------------------------------------------------------------------------------------------------------- | ------------- | ------------------ | --------------------- | ----------------------- | --------------------- | ------ | ------------- | ------------- | ------- | -------------------------- |
| root      | root@caption.htb | $pbkdf2-sha256$100000$O5zdxA5m9ZtnSSMnUfXK4zw9j/8WgKxo9ItXxVIPw3s=$xUd/Zorr75r/yWR9IXkW7TJlLXuEH+3U1uMAm37cBMk= | true          | http://caption.htb | 2024-03-08 03:01:05.0 | 2024-03-08 04:16:07.215 | 2024-09-22 17:21:38.6 | <NULL> | false         | Administrator | false   | clob15: 'Caption Networks' |
### KNOWN VULNS 

There was supposed to be an arbitrary local file read but it seems part of the exploit does not work -> it is for an older version

Found https://www.exploit-db.com/exploits/44668, but it only works on windows and we are on linux

Also found this repository with useful information https://github.com/kacperszurek/exploits/blob/master/GitBucket/gitbucket-unauthenticated-rce.md#unrestricted-file-upload
