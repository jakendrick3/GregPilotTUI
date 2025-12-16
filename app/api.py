from config import cfg
import requests

class Craft():
    def __init__(self, *, type: str, id: str, amount: int | None = None):
        self.type = type
        self.id = id
        self.amount = amount
    
    def submit(self) -> bool:
        url = cfg.baseurl + "/api/requests/craft"
        postobj = {
            "type": self.type,
            "id": self.id,
            "amount": self.amount
        }

        send = [postobj]

        #request = requests.post(url=url, json=send)
        #result = request.json()

        result = []
        try:
            if result["id"] == postobj["id"] and result["amount"] == postobj["amount"]:
                return True
            else:
                return False
        except:
            return False

async def get(endpoint: str):
    url = cfg.baseurl + endpoint
    request = requests.get(url)

    return request.json()