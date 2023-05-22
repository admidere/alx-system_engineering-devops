#!/usr/bin/python3
""" A Python script that, using this https://jsonplaceholder.typicode.com/
    REST API for a given employee ID, returns information about his/her
    TODO list progress and exports the data in JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Get employee id from command line
    employee_id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    # Get information about the employee
    response = requests.get(url)
    employee_name = response.json().get('name')

    # Get information about the employee todo list
    response = requests.get("{}/todos".format(url))
    todo_list = response.json()

    # Get list of completed tasks
    completed_tasks = []
    for task in todo_list:
        if task.get('completed') is True:
            completed_tasks.append(task)

    # Print out his/her todo list progress
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), len(todo_list)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

    # Export data to JSON
    json_file = "{}.json".format(employee_id)
    formatted_tasks = []
    for task in todo_list:
        formatted_tasks.append({"task": task.get('title'), "completed": task.get('completed'), "username": employee_name})

    with open(json_file, 'w') as file:
        json.dump({employee_id: formatted_tasks}, file)

    print("Data exported to {}".format(json_file))
