- user: `helpme@helpme.com`
- password: `5d3c93182bb20f07b994a7f617e99cff` -> `godhelpmeplz`

## INTRODUCTION

The only thing that changes when using a user is that we now have access to our tickets, and that we do no longer need to input a mail in the ticket submission process.

After a little bit of digging i found that there are probably two known exploits that we can use:

- Unauthenticated file upload: https://www.exploit-db.com/exploits/40300. The app in the version it is (1.0.2) should allow for us to upload a php file, but it appears this is being filtered (for all extensions of php that i know of).
- [[SQL injection]]: https://www.exploit-db.com/exploits/41200. After a bit of playing i actually got this to work. Let us see what we can do with this.
