#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)
    
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    employee = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()

    done_tasks = [task for task in tasks if task["completed"]]
    total_tasks = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee["name"], len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t ", task["title"])

