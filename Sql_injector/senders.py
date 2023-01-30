from typing import *
import requests

def create_requester(name: str, *args: list[Any], **kargs: dict[Any]) -> Any:
    requester = None
    if name == 'POST':
        requester = requests.post
    elif name == 'GET':
        requester = requests.get
    else:
        raise Exception('you did not give a correct type of request')
    
    return requester

def linear_sender():
    ...