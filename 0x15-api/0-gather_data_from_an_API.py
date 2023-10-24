#!/usr/bin/python3
"""REST API"""
import json
import requests
import sys


if __name__ == "__main__":
    if sys.argv[1].isdigit():
        URL = f"https://jsonplaceholder.typicode.com"
        users = f"{URL}/users/{sys.argv[1]}"
        todos = f"{URL}/todos?userId={sys.argv[1]}"
        formatted_data = json.dumps

        users_response = requests.get(users)
        todos_response = requests.get(todos)

        if (todos_response.status_code == 200 and
                users_response.status_code == 200):
            get_users_data = users_response.json()
            get_todos_data = todos_response.json()

            todos_length = len(get_todos_data)
            count = 0
            list_completed_todos = []

            for todo in get_todos_data:
                if todo.get('completed') is True:
                    count += 1
                    list_completed_todos.append(todo.get('title'))

            print(f"Employee {get_users_data.get('name')} is done with \
tasks({count}/{todos_length}):")
            for title in list_completed_todos:
                print(f'\t{title}')
