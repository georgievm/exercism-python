import random as r
import string as s

def generate_name():
    r.seed()
    name = r.choices(s.ascii_uppercase, k=2) + r.choices(s.digits, k=3)
    return ''.join(name)

class Robot:
    def __init__(self):
        self.name = generate_name()
    def reset(self):
        self.__init__()