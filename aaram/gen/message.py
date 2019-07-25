import random

class MessageGen:
    messages = [
        "hello",
        "welcome to the service",
        "hello world"
    ]

    def __init__(self):
        pass


    def gen(self):
        return random.choice(self.messages)