# pip install requests
import json
import requests

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'
# REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'
REFRESH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/refresh/'
ENDPOINT = 'http://127.0.0.1:8000/api/status/'

# data = {
#     'username': 'omar',
#     'password': 'omar'
# }

# r = requests.post(AUTH_ENDPOINT, data=data)
# # print(r.json())
# token = r.json()['token']
# print(token)


headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'omar',
    'password': 'omar'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
# print(token)

# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']
# print(new_token)



headers = {
    "Content-Type": "application/json",
    "Authorization": "JWT" + token,
}

post_data = json.dumps({'content': 'Some random content'})
posted_response = requests.post(ENDPOINT, data=post_data, headers=headers)
print(posted_response.text)





def do(method='get', data={}, id=6):
    r = requests.request(method, ENDPOINT + '?id=' + str(id), data=data)
    print(r.text)
    return r

# do()
# do(data={'id': 8})  # We can see that on runserver shell.

# r = requests.request('get', 'http://127.0.0.1:8000/api/status/?id=' + str(id), data={'id': 8})



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
# do3(method='delete', data={'id': 13})
# do3(method='put', data={'id': 6, 'content': 'Some new cool content', 'user': 1})
# do3(method='post', data={'content': 'Some new cool content', 'user': 1})


import os

image_path = os.path.join(os.getcwd(), 'Screenshot_9.png')  # location of the image

def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do_img(method='post', data={'user': 1, 'content': ''}, is_json=False, img_path=image_path)
# do_img(method='put', data={'id': 17, 'user': 1, 'content': 'Some new biki content'}, is_json=False, img_path=image_path) # it will create another one. Will not update.




# get_endpoint = ENDPOINT + str(17)
# post_data = json.dumps({'content': 'Some random content'})

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers = {
#     'content-type': 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)