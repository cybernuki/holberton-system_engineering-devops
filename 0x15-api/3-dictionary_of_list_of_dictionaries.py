#!/usr/bin/python3
# This script get the todo list from a given userId
import json
import requests
from sys import argv


TODOS_SOURCE = 'https://jsonplaceholder.typicode.com/todos?userId={}'

USERS_SOURCE = 'https://jsonplaceholder.typicode.com/users/'


FILE = 'todo_all_employees.json'


def consume():
    users_request = USERS_SOURCE
    usrs_response = requests.get(users_request)
    if usrs_response.status_code != 200:
        print("error")
        return None
    result = []
    for user in usrs_response.json():
        todos = requests.get(TODOS_SOURCE.format(user.get('id')))
        if todos.status_code != 200:
            return None
        result.append({'usr_data': user, 'usr_todos': todos.json()})
    return result


def export(data):
    usr_id = data.get('usr_data').get('id')
    usr_name = data.get('usr_data').get('username')
    usr_todos = data.get('usr_todos')

    if not usr_name or not usr_todos:
        print("Some values are None")
        return None

    with open(FILE, 'a', newline="") as file:
        json.dump({usr_id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": usr_name
        } for task in usr_todos]
        },
            file)


def main():
    data = consume()
    for user in data:
        export(user)

if __name__ == "__main__":
    main()
