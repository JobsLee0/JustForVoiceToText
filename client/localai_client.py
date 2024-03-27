import os
import requests
import string

from client.client import Client
from config import config as conf


class LocalaiClient(Client):
    def request(self, file_path) -> string:
        url = conf.get_conf().getClientUrl()
        model = conf.get_conf().getModel()
        file = open(file_path, 'rb')
        files = {
            'model': (None, model),
            'file': (os.path.split(file_path)[1], file)
        }
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print('request success:', response.text)
            return response.json()['text']
        else:
            print('request failed:', response.status_code, response.text)
            raise Exception('request failed')
