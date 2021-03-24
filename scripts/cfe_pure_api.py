import json
import requests  # Allow you to do http request

BASE_URL = 'http://127.0.0.1:8000/'

ENDPOINT = 'api/updates/'

def get_list():  # ---> Lists all this out.
    r = requests.get(BASE_URL + ENDPOINT)
    
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:  # 404 - Page not fount or not found
        print('Probably not good sign!')
        
    data = r.json()
    # print(type(data))  # It will print the list class.
    # print(type(json.dumps(data)))  # It will print the string class.
    for obj in data:
        # print(obj['id'])
        if obj['id'] == 1:   # get individual id. ---> User Interaction.
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            # print(dir(r2))
            print(r2.json())
    return data

# print(get_list())
get_list()  # Call the function