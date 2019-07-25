import requests
import random
import os


class NameGen:
    names_f_filename = os.path.expanduser("~/.aaram/names_f.txt")
    names_l_filename = os.path.expanduser("~/.aaram/names_l.txt")


    def __init__(self):
        self.list_f = []
        self.list_l = []

        self.load()

    
    def load(self):
        with open(self.names_f_filename, "r") as f:
            self.list_f = f.read().splitlines()

        with open(self.names_l_filename, "r") as f:
            self.list_l = f.read().splitlines()

        #import pdb; pdb.set_trace()

    
    def get_first_name(self):
        return random.choice(self.list_f)