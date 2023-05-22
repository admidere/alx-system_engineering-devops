#!/usr/bin/python3
""" A Python script that, using this https://jsonplaceholder.typicode.com/
    REST API for a given employee ID, returns information about his/her
    TODO list progress and exports the data in CSV format.
"""
import csv
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

    # Export data to CSV
    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for task in todo_list:
            writer.writerow([employee_id, employee_name, task.get('completed'),
                             task.get('title')])

    print("Data exported to {}".format(csv_file))
