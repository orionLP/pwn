## ENTRY POINT

We are immediately relocated to https://api.craft.htb/api/, which presents to us with an api constructed with swagger.

![[Screenshot from 2024-12-01 17-28-03.png]]

The functionality of the api is as follows:

- /auth/check: checks if a token is correct. The parameter that the token is supposed to go into is not mentioned.

```txt
Incorrect token: 

403
{
  "message": "Invalid token or no token found."
}
```

It might also be the case that we are not authorized to do this action, or that it is done in the background by dome component

- /auth/login: Seems to create a token given a valid user and password. This is achieved through basic authentication
- /brew -> these endpoints manage the repository of brews, from getting, updating, creating and deleting brews. It appears there are access controls based on tokens in order to execute delete, update and create brews.