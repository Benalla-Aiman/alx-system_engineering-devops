import requests
import sys

def get_todo_list_progress(employee_id):
    # Base URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Getting user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch data for user ID {employee_id}.")
        return

    user_data = user_response.json()
    employee_name = user_data["name"]

    # Getting todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch todo data for user ID {employee_id}.")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task["title"] for task in todos_data if task["completed"]]
    
    # Printing the output
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for employee ID.")
        sys.exit(1)

    get_todo_list_progress(employee_id)

