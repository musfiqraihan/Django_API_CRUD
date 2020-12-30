import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# URL = "http://127.0.0.1:8000/student/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data(1)


def post_data():
    data = {
        'name': 'Rana',
        'roll': 145,
        'city': 'Randdabaha',
    }

    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {
        'id': 2,
        'name': 'Abul Kalam Azad',
        'roll': 125,
        'city': 'Dhaka',
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {'id': 7}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

#
# delete_data()
