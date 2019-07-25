
from .client import Client
from .cli_output import CliOutput
from .json_maker import JsonMaker

class CliRouter:

    def __init__(self):
        self.cli_output = CliOutput()


    def get(self, *args, **kwargs):
        client = Client()
        ret = client.get(*args)
        self.cli_output.output(ret, 'get')


    def post(self, *args, **kwargs):
        if kwargs.get("json", None) is not None:
            jm = JsonMaker()
            json = jm.make(kwargs['json'])
            kwargs['json'] = json

        client = Client()
        ret = client.post(*args, **kwargs)
        self.cli_output.output(ret, 'post')


    def delete(self, *args, **kwargs):
        client = Client()
        ret = client.delete(*args)
        self.cli_output.output(ret, 'delete')