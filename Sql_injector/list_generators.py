from typing import *

class List_Generator:
    '''List_Generator is the base class to all list generators in this file'''

    basic_list: list[str]
    post_list: list[str]
    
    def __init__(self) -> None:
        raise NotImplementedError("You did not implement the init of some list generator")
    
    def generate_post_list(self) -> list[str]:
        raise NotImplementedError("You did not implement the init of some list generator")

class Logic_inverter(List_Generator):
    
    def __init__(self) -> None:
        self.basic_list = [""]
        self.post_list = []
    
    def generate_post_list(self) -> list[str]:
        ...

