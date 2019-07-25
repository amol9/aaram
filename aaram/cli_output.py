import json

class CliOutput:

    def __init__(self):
        pass

    def output(self, response, subcmd):
        print("%d (%s)"%(response.code, response.reason))
        #print(response.text)
        print(json.dumps(response.json, indent=2))