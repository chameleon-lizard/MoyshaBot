import requests as r
from time import sleep

def send_request(url, headers, data):
    while True:
        response = r.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response
        else:
            print(f"Does not respond: {response.json()}")
            sleep(1)