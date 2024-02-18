import subprocess

subprocess.call(['find', '/','-type', 'f', '-name', 'root.txt'])
subprocess.call(['cat','/root/root.txt'])