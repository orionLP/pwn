![[Screenshot from 2024-12-01 18-08-22.png]]

This is a git server using **gogs version 0.11.86.0130** 

## BASIC INFORMATION

- The repository of the api is laid out and anyone can read it.
- There are authentication and authorisation mechanisms such as login, forgot password, remember me, etc...
- There are 4 registered users: administrator, ebachman, dinesh, and gilfoyle. 
- The only registered organisation is craft.

Since we have access to the api, it is probably worth it checking out it's functionality. Let us do a [[code_review]].

## COMMITS

Another thing to do when analysing any git repository is to review it's commit history, pull requests, etc... In our case there are several commits and in commit `10e3ba4f0a09c778d7cec673f28d410b73455a86` we find that one of the users was using their credentials in order to do a test. These are:

- username: dinesh
- password: 4aUh0A8PbVJxgd
