import random


class EmailGen:
    email_domains = ["gmail.com", "hotmail.com", "mail.com", "gmx.com"]

    def __init__(self):
        pass


    def gen(self):
        return random.choice(self.email_domains)