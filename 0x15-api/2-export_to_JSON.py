#!/usr/bin/python3
"""A Python script to export data in the JSON format"""

import json
import re
import requests
import sys

"""The base URL of the JSONPlaceholder API"""
API_URL = 'https://jsonplaceholder.typicode.com'

def fetch_user_todos(user_id):
    """Fetches user information and todos (tasks) associated with the user"""
    try:
        # Retrieves user information
        user_res = requests.get(f'{API_URL}/users/{user_id}')
        user_res.raise_for_status()
        user_data = user_res.json()
        user_name = user_data.get('username')

        # Retrieves todos for the user
        todos_res = requests.get(f'{API_URL}/todos?userId={user_id}')
        todos_res.raise_for_status()
        todos_data = todos_res.json()

        # Map todos to the desired JSON format
        user_todos = [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user_name
        } for todo in todos_data]

        # This Writes the data to a JSON file
        with open(f'{user_id}.json', 'w') as file:
            json.dump({str(user_id): user_todos}, file, indent=4)
        print(f"Data has been exported to {user_id}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # This is to Check if a user ID is provided as a command-line argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    fetch_user_todos(user_id)

