#!/usr/bin/python3
"""
Script that uses the JSONPlaceholder API to display an employee's TODO list progress.
"""

import requests
import sys


def display_progress(employee_id):
    """
    Displays the TODO list progress of an employee from the JSONPlaceholder API.
    """
    # Base API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch data from API
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check if user exists
    if user_response.status_code != 200:
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_data = todos_response.json()
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            display_progress(employee_id)
        except ValueError:
            pass

