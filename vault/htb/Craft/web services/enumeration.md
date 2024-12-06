## ENTRY POINT

The basic website is composed of 3 domains:

```txt
https://10.10.10.110/       # entry point for users
https://api.craft.htb/api/  # entry point for an api (link in 10.10.10.110)
https://gogs.craft.htb/     # entry point for a git repo (link in 10.10...)
```

We will begin to enumerate each one separately to find out what functionality each one has.

- Entry point: [[default_web]]
- Brew api: [[REST_api]]
- Git service: [[Gogs_webpage]]