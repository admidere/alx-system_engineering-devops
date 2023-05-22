#!/usr/bin/python3
"""
This script fetches an employee's TODO list progress from a REST API and displays it in the specified format.
"""

import requests
import sys


if __name__ == "__main__":
    """
        Fetches and displays an employee's TODO list progress from a REST API.
    """

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        """
        Fetches and displays an employee's TODO list progress from a REST API.

        Args:
            employee_id (int): The employee ID.
        """
        employee_id = sys.argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code != 200 or todos_response.status_code != 200:
            print("Error: Unable to fetch data from the API.")
            sys.exit(1)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name")
        done_tasks = [task for task in todos_data if task.get("completed")]
        total_tasks = len(todos_data)

        print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
