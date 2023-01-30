from typing import *
from abc import ABC,abstractmethod

class List_Generator(ABC):
    '''List_Generator is the base class to all list generators in this file'''
    
    basic_list: list[str]
    
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def generate_list(self) -> list[str]:
        pass 

class Logic_inverter(List_Generator):
    
    def __init__(self) -> None:
        self.basic_list = ["' OR 1=1", "'--"]
        self.post_list = []
    
    def generate_list(self) -> list[str]:
        return self.basic_list

def create_generator(type: str, **kargs: dict[Any]) -> List_Generator:
    if type == 'logic':
        return  Logic_inverter()
    