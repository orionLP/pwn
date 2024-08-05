
## PASSWORD RESET

There is a reset password functionality, given a mail, you get password reset

Given a password reset request the body looks like 

```http
POST /users

...


------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="_method"

put
------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="authenticity_token"

ELWvw4DGMe8aIp2D6JGgJkKopuDwYln0JvMH70nHRopuOggLHri1t6PYTAD_ylSpB4QghnhhRZHD1Ta3wWT8zw
------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="user[avatar]"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="user[email]"

someemail@gmail.com
------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="user[password]"

asdfasdf
------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="user[password_confirmation]"

asdfasdf
------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="user[current_password]"

a
------WebKitFormBoundaryb5YM09GNzteXLBDz
Content-Disposition: form-data; name="commit"

Update
------WebKitFormBoundaryb5YM09GNzteXLBDz--
```

## ACCOUNT DELITION


```http
POST /users HTTP/1.1
Host: site.empman.thm
Content-Length: 120
Accept: text/vnd.turbo-stream.html, text/html, application/xhtml+xml
X-CSRF-Token: 7FYkngFoc1LgnXmGLfa2C8H_YCXz0-rLak7-ZU55SZhiro2gv7lo5KBJ8xOYWLAbh0gjZ6d13-v1lfCjJvAexQ
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Origin: http://site.empman.thm
Referer: http://site.empman.thm/users
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: _emp_man_session=WpzrT%2FNZsBbHUGtZyiTViv5V1uJI%2B%2BEzZv4wLrQ8ZxnmKO4luS4lbOv95O8Uiip2r6x62BImx60Bq9B%2FP13%2FF6C%2FDs%2BlbpsT2n5IaTdE8yhC2%2BvhVl7SkLKd9raxPbIFybo6MDy0f4iB4slM%2FIikg65XUv3uD2vfYC3aKFjo0MZTSJKz2ZNzLdR%2BgT%2By6TqEzTAwUE8xee5qN7u7CCyc70JC9qaJyK2YAHew%2FNvOGTh7xiQ7qnF6JwasEWqEbXjq4A8Gk5DxEXB0TNlppeJ2cSbzqHejw5sKOh5aYZMy8ibDQEdRZ4CVbn%2Fz2NkbL1EhWy3xedfSoQLDnHaOtEfO6xPcMyYPvkmxPQvVHJCJZXSm%2BWlu2L%2Fdy5rcK84hz1lwF1EYaAoXkyQ%3D--HkK%2BGL5x0%2FaOQEqO--xTF4V5oHOHYw3YNFrRKpjw%3D%3D
Connection: close

_method=delete&authenticity_token=2tu7mSKM5HHEDP6p2_N9ww7M8cYmGJzeHpy7OQ33tIVW2JqdQTMpvI0_8HHplISV79hFxkb8kORW203EKOpNgg
```

**NO PASSWORD IS REQUIRED TO DELETE AN ACCOUNT** -> DOUBTFUL IT HAS ANY EFFECT


```http

:§DÀ!m3g6TÏA=/âI7ý§j×³öõkóíøK
```