import os
import requests

request = requests.post(
    'https://api.bfl.ml/v1/flux-pro-1.1',
    headers={
        'accept': 'application/json',
        'x-key': os.environ.get("BLACK_FOREST-API-KEY"),
        'Content-Type': 'application/json',
    },
    json={
        'prompt': 'An illustration of a cartoon-style rat and duck, both as friendly characters, set in a colorful, animated version of Moscow. The rat has a curious and adventurous look, while the duck appears cheerful and loyal. They are standing together in front of iconic Moscow landmarks, like Saint Basils Cathedral, with a bright, playful background that includes trees and city elements. The scene conveys friendship and adventure, with a whimsical and heartwarming tone suitable for a childrens cartoon.',
        'width': 1024,
        'height': 768,
    },
).json()
print(request)
request_id = request["id"]
import time

while True:
    time.sleep(0.5)
    result = requests.get(
        'https://api.bfl.ml/v1/get_result',
        headers={
            'accept': 'application/json',
            'x-key': os.environ.get("BFL_API_KEY"),
        },
        params={
            'id': request_id,
        },
    ).json()
    if result["status"] == "Ready":
        print(f"Result: {result['result']['sample']}")
        break
    else:
        print(f"Status: {result['status']}")