Now we have access to a backup software. The idea i had here is that since root is running some cronjobs and duplicati allows both to do backups and to restore files is to take the cleanup_cacti.sh script, which is running every minute by root, and add a simple tcp reverse shell to it (any place root is going to run scripts at is fine though, but that is how i did it the first time). 

This can be achieved because, although duplicati is running in a docker container, one of the volumes maps to the root / directory, and thus we have access to the entire computer.

In this case the steps to do this are:

- Create a backup task with no encryption which makes a backup of a shell. Choose the directories of your liking to do this
- Run the task
- Do a restore task, choosing a file/directory that will be overwritten. 

And thus we are [[root]].

