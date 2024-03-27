import json
import os.path
import sys


class _Config(object):
    config_data = {}

    def __init__(self):
        base_path = os.path.dirname(__file__)
        if getattr(sys, 'frozen', None):
            base_path = sys._MEIPASS
        config_file_path = os.path.join(base_path, 'config.json')
        if os.path.exists(config_file_path):
            try:
                with open(config_file_path, 'r', encoding='utf-8') as file:
                    self.config_data = json.load(file)
                print("load config data success")
            except json.JSONDecodeError as e:
                print("error decoding JSON:", e)
            except FileNotFoundError:
                print("config file not found:", config_file_path)

    def getModel(self):
        return self.config_data["model_name"]

    def getClientType(self):
        return self.config_data["client_type"]

    def getClientUrl(self):
        return self.config_data["client_url"]

    def getClientToken(self):
        return self.config_data["client_token"]


_conf = _Config()


def get_conf():
    return _conf
