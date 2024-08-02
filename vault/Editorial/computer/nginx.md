The enabled sites 

```bash
dev@editorial:/etc/nginx/sites-enabled$ ls -la
total 8
drwxr-xr-x 2 root root 4096 Jan 31  2023 .
drwxr-xr-x 8 root root 4096 Jun  4 14:38 ..
lrwxrwxrwx 1 root root   36 Jan 31  2023 editorial -> /etc/nginx/sites-available/editorial
dev@editorial:/etc/nginx/sites-enabled$ cat editorial 
server {
    listen 80;
    server_name editorial.htb;

    if ($host != $server_name) {
        return 301 http://editorial.htb;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/opt/apps/app_editorial/editorial.sock;

    }
}

```