#!/usr/bin/python3
""" A Python script that, using this https://jsonplaceholder.typicode.com/
    REST API, returns information about all employees' TODO list progress
    and exports the data in JSON format.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    # Get information about all employees
    response = requests.get(url)
    employees = response.json()

    all_tasks = {}

    for employee in employees:
        employee_id = employee.get('id')
        employee_name = employee.get('name')

        # Get information about the employee todo list
        response = requests.get("{}/{}/todos".format(url, employee_id))
        todo_list = response.json()

        # Format tasks
        formatted_tasks = []
        for task in todo_list:
            formatted_tasks.append({"username": employee_name,
                                    "task": task.get('title'),
                                    "completed": task.get('completed')})

        all_tasks[employee_id] = formatted_tasks

    # Export data to JSON
    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as file:
        json.dump(all_tasks, file)

    print("Data exported to {}".format(json_file))
