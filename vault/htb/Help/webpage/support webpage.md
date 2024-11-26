
## USERS

- user: `helpme@helpme.com`
- password: `5d3c93182bb20f07b994a7f617e99cff` -> `godhelpmeplz`

That we know the existence of 

```txt
Shiv
```

## LOGIN

Upon trying to log in with the provided credentials we are unable to log in. The forgot password says that there is no such user so probably was changed. We could try to harvest usernames and see if we can do password stuffing.

Turns out this was a hash :) Now we can log in as [[helpme]].

## GENERAL RECON

The guide for using this software can be found in the following webpage https://docs.helpdeskz.com/en/latest/installation/repositories/, and the repository for this software can be found at https://github.com/helpdesk-z/helpdeskz-dev.

After looking around in the github repository, it seems there might be multiple endpoints for this service and a dedicated staff login page