import json

from .gen import *

class JsonMaker:
    last_fname = None

    def __init__(self):
        self.gen_d = {
            "fname"     : lambda : NameGen().get_first_name(),
            "email"     : lambda : EmailGen().gen(),
            "message"   : lambda : MessageGen().gen()
        }

    def make(self, str):
        d = {}
        for pair in str.split(','):
            k, v = list(map(lambda s: s.strip(), pair.split(':')))
            if v.startswith('%'):
                gv = self.gen(v[1:])
                if v == "%fname":
                    JsonMaker.last_fname = gv
                if v == "%email":
                    gv = JsonMaker.last_fname.lower() + '@' + gv

                #print("gv:", gv)
                d[k] = gv
            else:
                d[k] = v

        #je = json.encoder.JSONEncoder()
        #return je.encode(d)
        #print(d)
        return d


    def gen(self, type):
        return self.gen_d[type]()
