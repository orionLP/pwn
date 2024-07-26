#include <unistd.h>
#include <sys/types.h>

int main() {

    if (setuid(0) == -1) {  // Change to user ID 1000
        perror("setuid");
        return 1;
    }
    if (setgid(0) == -1) {  // Change to group ID 1000
        perror("setgid");
        return 1;
    }

    char *argv[] = { "/bin/ls", "-l", NULL };  // Arguments to the command
    char *envp[] = { NULL };  // Environment variables

    execve("/usr/bin/bash", argv, envp);
    return 0;
    
}