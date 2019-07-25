from redcmd.api import Subcommand, subcmd

from aaram.cli_router import CliRouter


class HttpSubcommands(Subcommand):

    def __init__(self):
        self.cli_router = CliRouter()


    def common(self, url, json=None):
        self.url = url
        self.json = json


    @subcmd(add=[common])
    def get(self):
        self.cli_router.get(self.url)


    @subcmd(add=[common])
    def post(self):
        self.cli_router.post(self.url, json=self.json)


    @subcmd(add=[common])
    def delete(self):
        self.cli_router.delete(self.url)
