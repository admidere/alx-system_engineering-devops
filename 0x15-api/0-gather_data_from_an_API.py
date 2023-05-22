#!/usr/bin/python3

"""
This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
/users api endpoint and todo lists from todos?userId={} api
endpoint
"""


import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(user_id))
    if user_response.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    user = user_response.json()
    todos_response = requests.get(url + "todos?userId={}".format(user_id))
    if todos_response.status_code != 200:
        print("Error: Failed to fetch todos")
        sys.exit(1)

    todos = todos_response.json()

    completed = [t.get("title") for t in todos if t.get("completed")]
    completed_tasks = len(completed)
    total_tasks = len(todos)
    print("Employee Name: {}".format(user.get("name")))
    print("({}/{}):".format(completed_tasks, total_tasks))
    for task in completed:
        print("\t{}".format(task))
