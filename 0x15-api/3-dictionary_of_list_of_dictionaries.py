#!/usr/bin/python3
"""A Python script to export data for all employees in JSON format"""

import json
import requests

"""The base URL of the JSONPlaceholder API"""
API_URL = 'https://jsonplaceholder.typicode.com'

def fetch_all_employee_todos():
    """Fetches todos (tasks) for all employees"""
    try:
        # Retrieves all users
        users_res = requests.get(f'{API_URL}/users')
        users_res.raise_for_status()
        users_data = users_res.json()

        # Initializes dictionary to store todos for all employees
        all_employee_todos = {}

        # Iterates over each user to fetch their todos
        for user in users_data:
            user_id = user['id']
            user_name = user['username']

            # Retrieves todos for the user
            todos_res = requests.get(f'{API_URL}/todos?userId={user_id}')
            todos_res.raise_for_status()
            todos_data = todos_res.json()

            # Map todos to the desired JSON format
            user_todos = [{
                'username': user_name,
                'task': todo.get('title'),
                'completed': todo.get('completed')
            } for todo in todos_data]

            # This adds todos to the dictionary with user ID as key
            all_employee_todos[user_id] = user_todos

        # This writes the data to a JSON file
        with open('todo_all_employees.json', 'w') as file:
            json.dump(all_employee_todos, file, indent=4)
        print("Data has been exported to todo_all_employees.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    fetch_all_employee_todos()

