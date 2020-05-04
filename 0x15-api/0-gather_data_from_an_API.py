#!/usr/bin/python3
# This script get the todo list from a given userId
import requests
from sys import argv


TODOS_SOURCE = 'https://jsonplaceholder.typicode.com/todos?userId={}'

USERS_SOURCE = 'https://jsonplaceholder.typicode.com/users/{}'

FIRST_LINE = 'Employee {} is done with tasks({}/{}):'

N_LINES_TEMPLATE = '\t {}'


def consume(id):
	"""
		This function consume from the api to search the
		User information and their todos

		id: Is the id of the user
		Return a dictionary with two keys:
		'usr_data': Contains a dictionary with the user information
		'usr_todo': contains a list of dictionaries with todos information
	"""
	user_request = USERS_SOURCE.format(id)
	todos_request = TODOS_SOURCE.format(id)
	usr_response = requests.get(user_request)
	if usr_response.status_code != 200:
		return None

	tds_response = requests.get(todos_request)
	if tds_response.status_code != 200:
		return None
	return {'usr_data': usr_response.json(), 'usr_todos': tds_response.json()}


def display(data):
	"""
		This function display user information and their todos
	"""
	user_name = data.get('usr_data').get('name')
	user_todos = data.get('usr_todos')

	if not user_name or not user_todos:
		print("Some values are None")
		return None

	total_tasks = len(user_todos)
	done_tasks = [done for done in user_todos if done.get('completed')]

	print(FIRST_LINE.format(user_name, len(done_tasks), total_tasks))
	for task in done_tasks:
		title = task.get('title')
		print(N_LINES_TEMPLATE.format(title))


def main(id):
	"""
		Main function
	"""
	if not id:
		return None
	display(consume(id))


if __name__ == "__main__":
	id = argv[1] if len(argv) == 2 else None
	main(id)
