#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None

    Raises:
        None
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (f"https://jsonplaceholder.typicode.com/users/"
                 f"{employee_id}/todos")

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if (user_response.status_code != 200 or
            todos_response.status_code != 200):
        print("Error: Unable to fetch data from the API.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data["name"]
    done_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks "
          f"({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    """
    Entry point of the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
