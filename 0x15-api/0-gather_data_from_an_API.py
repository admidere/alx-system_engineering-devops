#!/usr/bin/python3

"""
This script fetches information about a given employee's TODO list progress
using a REST API.

Usage: python script.py employee_id

Arguments:
    employee_id (int): The ID of the employee.

Example:
    python script.py 1
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee information
    employee_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todo_response = requests.get(f'{base_url}/todos',
                                 params={'userId': employee_id})
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    # Display progress information
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")
