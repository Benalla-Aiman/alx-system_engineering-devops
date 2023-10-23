#!/usr/bin/python3
"""Module to fetch data from the JSONPlaceholder API"""

import requests
import sys

def get_employee_data(employee_id):
    """Fetch and print the TODO list progress for a given employee ID"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    done_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print("\t", task["title"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)

