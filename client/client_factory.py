from client.client import Client
from client.localai_client import LocalaiClient


def get_client(client_type) -> Client:
    clients = {
        'localai': LocalaiClient
    }
    return clients.get(client_type)()
