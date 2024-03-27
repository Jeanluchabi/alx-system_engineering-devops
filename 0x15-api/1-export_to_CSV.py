#!/usr/bin/python3
'''This a Python script to export data in the CSV format'''

import re
import requests
import sys
import csv

"""The API's URL"""
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """It checks if the command line arguments are provided"""
    if len(sys.argv) > 1:
        """It checks if the argument is a valid user ID"""
        if re.fullmatch(r'\d+', sys.argv[1]):
            """It gets the user's information from the API"""
            user_id = int(sys.argv[1])
            user_res = requests.get(f'{API_URL}/users/{user_id}').json()
            todos_res = requests.get(f'{API_URL}/todos').json()
            user_name = user_res.get('username')

            """Filter todos for the given user"""
            todos = [todo for todo in todos_res if todo.get('userId') == user_id]

            """Writes the data to a CSV file"""
            with open(f'{user_id}.csv', 'w', newline='') as csvfile:
                fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for todo in todos:
                    writer.writerow({
                        'USER_ID': user_id,
                        'USERNAME': user_name,
                        'TASK_COMPLETED_STATUS': todo.get('completed'),
                        'TASK_TITLE': todo.get('title')
                    })

