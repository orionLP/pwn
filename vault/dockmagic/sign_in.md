## CONTENT

The web page has the following set up:

- You can change the password of a given gmail -> Needs to provide a password
- You can delete the account :)

## SIGN IN WITH REMEMBER ME 

```http
POST /users/sign_in HTTP/1.1
Host: site.empman.thm
Content-Length: 231
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://site.empman.thm
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://site.empman.thm/users/sign_in
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: _emp_man_session=WMxsrKS0x1Hs%2FGqT0Pjeuw3h87Uy5eez2y2pSB1hNqJdPmYuEzpf28fZY1fa2wYYxtm3Mn2j1XxULIbNfrLMoyEeMsfsi61293oq9rkosmExpQdcewqWQ1aherA%2BK8kfqGWN9iP%2FXDuos1EK07PX1PEn%2FoSEm4Vmttn6bSmKELGARkTmQyXhLR9%2FF3js%2FnC6t4AzKJ9cxVzUa9xYIg88WXfFf4gH2b%2F8PIAGjBdWqw%2BAIZ8gz5I82N3M9p44MG2gf2NyaIPDfrxycO015wq0XMJ7niswK%2BJB--TTzGPWcTtqTY0YKb--PL0GXvok0BF3GpMeuAzvMA%3D%3D
Connection: close

authenticity_token=spHeTKjrzVZZ0YomF-pt6hEKG7TskRbAzXtlHlUj3XUb9JHDNqu8IK0CDq0HIDa0-aIFgXPvnGoN3mHsQdc_7Q&user%5Bemail%5D=someemail%40gmail.com&user%5Bpassword%5D=aaaaaa&user%5Bremember_me%5D=0&user%5Bremember_me%5D=1&commit=Log+in
```

```http
Set-Cookie: remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNRjBzSWlReVlTUXhNaVJrTjFKbU5WQmlkVkExWmsxWVp6aExiMFF6YmtoMUlpd2lNVGN4TmpNeE5UazVPQzQxTnprMU5EZzBJbDA9IiwiZXhwIjoiMjAyNC0wNi0wNFQxODoyNjozOC41NzlaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D--b536a286ef3c07c5c26e453f172ebe2266df157c; path=/; expires=Tue, 04 Jun 2024 18:26:38 GMT; HttpOnly; SameSite=Lax
```


The cookie is partially base 64 encoded 

For user someemail@gmail.com
For pass aaaaaa

```bash
$ echo "eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNRjBzSWlReVlTUXhNaVJrTjFKbU5WQmlkVkExWmsxWVp6aExiMFF6YmtoMUlpd2lNVGN4TmpNeE9ETXpOUzR6TURRME9ETTNJbDA9IiwiZXhwIjoiMjAyNC0wNi0wNFQxOTowNTozNS4zMDRaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D--be8afd23ba2ef353dde484664c2b9681431e52a5" | base64 --decode -

{"_rails":{"message":"W1sxMF0sIiQyYSQxMiRkN1JmNVBidVA1Zk1YZzhLb0Qzbkh1IiwiMTcxNjMxODMzNS4zMDQ0ODM3Il0=","exp":"2024-06-04T19:05:35.304Z","pur":"cookie.remember_user_token"}}base64: invalid input
```

The last part 

```bash
$ hashid be8afd23ba2ef353dde484664c2b9681431e52a5 
Analyzing 'be8afd23ba2ef353dde484664c2b9681431e52a5'
[+] SHA-1 
[+] Double SHA-1 
[+] RIPEMD-160 
[+] Haval-160 
[+] Tiger-160 
[+] HAS-160 
[+] LinkedIn 
[+] Skein-256(160) 
[+] Skein-512(160) 
```

**AFTER LOGGING IN AND RESETTING THIS**

```bash
$ echo "eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNRjBzSWlReVlTUXhNaVJrTjFKbU5WQmlkVkExWmsxWVp6aExiMFF6YmtoMUlpd2lNVGN4TmpNeE9EYzVPUzR6TVRNeE16TTNJbDA9IiwiZXhwIjoiMjAyNC0wNi0wNFQxOToxMzoxOS4zMTNaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D--cdf0d8bc0bc9e78346e4eb9b6ad8cf9ef9aa6436" | base64 --decode -

{"_rails":{"message":"W1sxMF0sIiQyYSQxMiRkN1JmNVBidVA1Zk1YZzhLb0Qzbkh1IiwiMTcxNjMxODc5OS4zMTMxMzM3Il0=","exp":"2024-06-04T19:13:19.313Z","pur":"cookie.remember_user_token"}}base64: invalid input

```

```bash
$ hashid cdf0d8bc0bc9e78346e4eb9b6ad8cf9ef9aa6436
Analyzing 'cdf0d8bc0bc9e78346e4eb9b6ad8cf9ef9aa6436'
[+] SHA-1 
[+] Double SHA-1 
[+] RIPEMD-160 
[+] Haval-160 
[+] Tiger-160 
[+] HAS-160 
[+] LinkedIn 
[+] Skein-256(160) 
[+] Skein-512(160) 
```


### DECODING OF THE COOKIES 


```bash

$ echo 'W1sxMF0sIiQyYSQxMiRkN1JmNVBidVA1Zk1YZzhLb0Qzbkh1IiwiMTcxNjMxODMzNS4zMDQ0ODM3Il0=' | base64 --decode -
[[10],"$2a$12$d7Rf5PbuP5fMXg8KoD3nHu","1716318335.3044837"]

$ echo 'W1sxMF0sIiQyYSQxMiRkN1JmNVBidVA1Zk1YZzhLb0Qzbkh1IiwiMTcxNjMxODc5OS4zMTMxMzM3Il0=' | base64 --decode -
[[10],"$2a$12$d7Rf5PbuP5fMXg8KoD3nHu","1716318799.3131337"]
```

-> hash inside looks like bcrypt 2\*, Blowfish (Unix)


Very much suspect the last is a timestamp

```bash
$ date +%s
1716319703

$ date +%s.%N | awk '{printf "%.7f\n", $1}'
1716319778.1242328

```

### GENERIC TRIAL

```
Set-Cookie: remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNVjBzSWlReVlTUXhNaVJITGxaRmRtOXVVV3d2TDJGSmNYVTRhRGxaYTNoUElpd2lNVGN4TmpNeU1EQXlPQzQxTURNM016Z3lJbDA9IiwiZXhwIjoiMjAyNC0wNi0wNFQxOTozMzo0OC41MDNaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D--bd7cd087b4b0fce2699a9d607bc6677749ef4a9f; path=/; expires=Tue, 04 Jun 2024 19:33:48 GMT; HttpOnly; SameSite=Lax

$ echo 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNVjBzSWlReVlTUXhNaVJITGxaRmRtOXVVV3d2TDJGSmNYVTRhRGxaYTNoUElpd2lNVGN4TmpNeU1EQXlPQzQxTURNM016Z3lJbDA9IiwiZXhwIjoiMjAyNC0wNi0wNFQxOTozMzo0OC41MDNaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D=' | base64 --decode -
{"_rails":{"message":"W1sxMV0sIiQyYSQxMiRHLlZFdm9uUWwvL2FJcXU4aDlZa3hPIiwiMTcxNjMyMDAyOC41MDM3MzgyIl0=","exp":"2024-06-04T19:33:48.503Z","pur":"cookie.remember_user_token"}}


$ echo 'W1sxMV0sIiQyYSQxMiRHLlZFdm9uUWwvL2FJcXU4aDlZa3hPIiwiMTcxNjMyMDAyOC41MDM3MzgyIl0' | base64 --decode -
[[11],"$2a$12$G.VEvonQl//aIqu8h9YkxO","1716320028.5037382"]base64: invalid input

```


After creating an account this has been observed 

-> The number in the index has increased to 11 so i have the sensation that there are other accounts, at least 9~10
-> The hash has changed, so it is not the same for all
-> i have the sensation that that is not all the hash.