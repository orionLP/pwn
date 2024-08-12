All of the following commands are done inside of the usage_blog database

```sql
mysql> SHOW TABLES;
+------------------------+
| Tables_in_usage_blog   |
+------------------------+
| admin_menu             |
| admin_operation_log    |
| admin_permissions      |
| admin_role_menu        |
| admin_role_permissions |
| admin_role_users       |
| admin_roles            |
| admin_user_permissions |
| admin_users            |
| blog                   |
| failed_jobs            |
| migrations             |
| password_reset_tokens  |
| personal_access_tokens |
| users                  |
+------------------------+
```

## TABLES:

The tables contain the following information 

- admin_menu: the paths in the admin page
- admin_operation_log: logs about connections to the webpage, scrapped some hashes from it into [[credentials]]
- admin_permissions: permissions in admin website
- admin_role_menu: nothing
- admin_role_permissions: nothing
- admin_role_users: nothing
- admin_roles: nothing
- admin_user_permissions: nothing
- admin_users: The hash we cracked before, also to [[credentials]].
- blog: blog related information
- failed_jobs: nothing
- migrations: nothing
- password_reset_tokens: nothing
- personal_access_tokens: nothing
- users: users and their hashes for the website