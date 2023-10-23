import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # Define URLs for employee and their todos
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details and their todos
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    # Ensure both requests were successful
    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from the API")
        sys.exit(1)

    # Parse the responses
    employee = employee_response.json()
    todos = todos_response.json()

    # Filter completed tasks
    completed_todos = [todo for todo in todos if todo['completed']]

    # Print the results
    print(f"Employee {employee['name']} is done with tasks({len(completed_todos)}/{len(todos)}):")
    for todo in completed_todos:
        print(f"\t {todo['title']}")

if __name__ == "__main__":
    # Check for command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py [employee_id]")
        sys.exit(1)

    # Get employee ID from the command line argument
    employee_id = sys.argv[1]
    
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Please provide a valid integer as the employee ID.")
        sys.exit(1)

    # Fetch and display the progress
    fetch_employee_todo_progress(employee_id)

