from config import cfg
import requests

class Craft():
    def __init__(self, *, type: str, id: str, amount: int | None = None):
        self.type = type
        self.id = id
        self.amount = amount
    
    def submit(self):
        url = cfg.baseurl + "/api/requests/craft"
        postobj = {
            "type": self.type,
            "id": self.id,
            "amount": self.amount
        }

        send = [postobj]

        print(postobj)

        request = requests.post(url=url, json=send)
        return request.json()

def get(endpoint: str):
    url = cfg.baseurl + endpoint
    request = requests.get(url)

    return request.json()