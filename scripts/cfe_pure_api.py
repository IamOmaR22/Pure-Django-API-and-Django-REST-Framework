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

def create_update():
    new_data = {
        'user': 1,
        'content': 'Another more cool content'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))  # post method
    # r = requests.post(BASE_URL + ENDPOINT + '1/', data=json.dumps(new_data))  # post method
    # r = requests.post(BASE_URL + ENDPOINT, data=new_data)  # post method
    # r = requests.delete(BASE_URL + ENDPOINT, data=new_data)  # delete method
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(get_list())
# get_list()  # Call the function
# print(create_update())



def do_obj_update():
    new_data = {
        'content': 'Some new awesome content'
    }
    # r = requests.put(BASE_URL + ENDPOINT + '1/', data=new_data) #json.dumps(new_data))  # put method
    r = requests.put(BASE_URL + ENDPOINT + '1/', data=json.dumps(new_data))  # put method
    # r = requests.put(BASE_URL + ENDPOINT + '100/', data=json.dumps(new_data))  # put method
    # new_data = {
    #     'id': 1,
    #     'content': 'New obj data'
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)

    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(do_obj_update())


def do_obj_delete():
    new_data = {
        'content': 'Some new awesome content'
    }
    r = requests.delete(BASE_URL + ENDPOINT + '1/')  # delete method
    # r = requests.delete(BASE_URL + ENDPOINT + '5/')  # give 1 or 2 or 5 etc.. You can delete which one you added.

    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

print(do_obj_delete())