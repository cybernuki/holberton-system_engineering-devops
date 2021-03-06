#!/usr/bin/python3
# This script get the todo list from a given userId
import json
import requests
from sys import argv


TODOS_SOURCE = 'https://jsonplaceholder.typicode.com/todos?userId={}'

USERS_SOURCE = 'https://jsonplaceholder.typicode.com/users/{}'


FILE = '{}.json'


def consume(id):
    user_request = USERS_SOURCE.format(id)
    todos_request = TODOS_SOURCE.format(id)
    usr_response = requests.get(user_request)
    if usr_response.status_code != 200:
        return None

    tds_response = requests.get(todos_request)
    if tds_response.status_code != 200:
        return None
    return {'usr_data': usr_response.json(), 'usr_todos': tds_response.json()}


def export(data, id):
    usr_name = data.get('usr_data').get('username')
    usr_todos = data.get('usr_todos')

    if not usr_name or not usr_todos:
        print("Some values are None")
        return None

    with open(FILE.format(id), 'w', newline="") as file:
        json.dump({id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": usr_name
        } for task in usr_todos]
        },
            file)


def main(id):
    if not id:
        return None
    export(consume(id), id)


if __name__ == "__main__":
    id = argv[1] if len(argv) == 2 else None
    main(id)
