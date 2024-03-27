#!/usr/bin/python3
"""This is a Python script that returns information about a given employee ID"""

import requests
import sys

"""The API's URL"""
API_URL = 'https://jsonplaceholder.typicode.com'

def get_employee_todo_progress(employee_id):
    """Fetches information about the employee's TODO list progress"""
    try:
        # Fetch user information
        user_res = requests.get(f'{API_URL}/users/{employee_id}')
        user_res.raise_for_status()
        user_data = user_res.json()
        user_name = user_data.get('name')

        # Fetch TODO list for the user
        todos_res = requests.get(f'{API_URL}/todos?userId={employee_id}')
        todos_res.raise_for_status()
        todos_data = todos_res.json()

        # Filter completed tasks
        completed_tasks = [todo for todo in todos_data if todo['completed']]

        # Print progress information
        print(f"Employee {user_name} is done with tasks ({len(completed_tasks)}/{len(todos_data)}):")
        for todo in completed_tasks:
            print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)

