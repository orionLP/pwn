## Existing users
Through basic enumeration the following users have been found (via the *user already exists message*).
- admin

## ATTEMPTED BYPASSES

In here i attempted to send payloads that mimic those found in upload (though changing how it is basically a fuzz to try to break application logic)

- all ascii characters no modification for password: so far no luck (all redirections to register)
- same in utf : no results 
- same in hex: no results 

One thing i noted when doing these is that cookies are set in base 64 and have the following structure:

```json
{"_flashes":[{" t":["message","Username already exists."]}]}g/
#�Q}o;3/˦

{"_flashes":[{" t":["message","Username already exists."]}]}g/R%&~ZuʻT
```

It appears that user already exists is also sent when using special characters 

When creating a new account:

```json
{"_fresh":false}r$?bIXڒw?ETE>
```