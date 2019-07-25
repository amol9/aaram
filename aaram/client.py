import requests


class Response:

    def __init__(self, res):
        #import pdb; pdb.set_trace()
        self.code = res.status_code
        self.reason = res.reason
        self.text = res.text
        self.json = res.json() if len(res.text) > 0 else ''


class Client:

    def __init__(self):
        pass


    def get(self, url, params=None):
        res = requests.get(url, params=params)
        return Response(res)

    
    def post(self, url, json=None):
        res = requests.post(url, json=json)
        return Response(res)


    def delete(self, url):
        res = requests.delete(url)
        return Response(res)