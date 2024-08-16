In this case i found a very useful exploit posted in github at https://github.com/m3m0o/chamilo-lms-unauthenticated-big-upload-rce-poc for **CVE-2023-4220**. 

Simply cloned the repository into the vm, and then also a webshell from seclists, and now we are www-data.

### TAKING DATA AWAY

One of the first steps i always take when accessing a system is dumping their database, since most apps store credentials in plaintext. 

After a bit of searching i found the following information regarding the website. Inside cli-config.php:

```php
<?php
/* For licensing terms, see /license.txt */

/**
 * Script needed to execute bin/doctrine.php in the command line
 * in order to:.
 *
 * - Generate migrations
 * - Create schema
 * - Update schema
 * - Validate schema
 * - Etc
 */
use Doctrine\ORM\Tools\Console\ConsoleRunner;

require_once __DIR__.'/vendor/autoload.php';
//require_once __DIR__.'/main/inc/lib/api.lib.php';
$configurationFile = __DIR__.'/app/config/configuration.php';

if (!is_file($configurationFile)) {
    echo "File does not exists: $configurationFile";
    exit();
}

require_once __DIR__.'/main/inc/global.inc.php';
require_once $configurationFile;

$database = new \Database();
$dbParams = [
    'driver' => 'pdo_mysql',
    'host' => $_configuration['db_host'],
    'user' => $_configuration['db_user'],
    'password' => $_configuration['db_password'],
    'dbname' => $_configuration['main_database'],
];

$database->connect($dbParams, realpath(__DIR__).'/', realpath(__DIR__).'/');
$entityManager = $database::getManager();

$helperSet = ConsoleRunner::createHelperSet($entityManager);
$dialogHelper = new Symfony\Component\Console\Helper\QuestionHelper();
$helperSet->set($dialogHelper);

return $helperSet;

```

Inside the app/config/configuration.php

```php
$_configuration['db_host'] = 'localhost';
$_configuration['db_port'] = '3306';
$_configuration['db_user'] = 'chamilo';
$_configuration['db_password'] = '03F6lY3uXAP2bkW8'; # fortunately this is the password for mtz
$_configuration['db_manager_enabled'] = false;
//$_configuration['session_stored_in_db_as_backup'] = true;
//$_configuration['sync_db_with_schema'] = false;
$_configuration['main_database'] = 'chamilo';
```

Now let us execute commands inside this [[database]]

### EXPLORING OTHER USERS

```bash
www-data@permx:/var/www/chamilo$ find / -user mtz 2>/dev/null
find / -user mtz 2>/dev/null
/home/mtz
/run/user/1000
/dev/pts/4
/dev/pts/3
/dev/pts/2
```

### Password discovered

Turns out that the password for the database is the same as the one for the [[mtz]] user.