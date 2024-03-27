import string
from abc import abstractmethod


class Client(object):
    @abstractmethod
    def request(self, file_path) -> string:
        pass
