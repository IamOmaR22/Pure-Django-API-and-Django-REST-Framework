# pip install requests
import requests

ENDPOINT = 'http://127.0.0.1:8000/api/status/'

def do(method='get', data={}, id=6):
    r = requests.request(method, ENDPOINT + '?id=' + str(id), data=data)
    print(r.text)
    return r

# do()
# do(data={'id': 8})  # We can see that on runserver shell.

# r = requests.request('get', 'http://127.0.0.1:8000/api/status/?id=' + str(id), data={'id': 8})


import json

def do2(method='get', data={}, id=6, is_json=True):
    if is_json:
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT + '?id=' + str(id), data=data)
    print(r.text)
    return r

# do2(data={'id': 8})


def do3(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do3(data={'id': 8})
# do3(method='delete', data={'id': 800})
do3(method='delete', data={'id': 13})
# do3(method='put', data={'id': 6, 'content': 'Some new cool content', 'user': 1})
# do3(method='post', data={'content': 'Some new cool content', 'user': 1})