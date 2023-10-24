#!/usr/bin/python3
"""REST API"""
import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1].isdigit():
        user_id = int(sys.argv[1])
        URL = "https://jsonplaceholder.typicode.com"
        users_url = f"{URL}/users/{user_id}"
        todos_url = f"{URL}/todos?userId={user_id}"

        users_response = requests.get(users_url)
        todos_response = requests.get(todos_url)

        if (todos_response.status_code == 200 and
                users_response.status_code == 200):
            get_users_data = users_response.json()
            get_todos_data = todos_response.json()

            json_filename = f"{get_users_data.get('id')}.json"
            user_tasks = []

            for todo in get_todos_data:
                todo_completed_status = todo.get('completed')
                todo_title = todo.get('title')
                username = get_users_data.get('username')

                task_entry = {
                    "task": todo_title,
                    "completed": todo_completed_status,
                    "username": username
                }
                user_tasks.append(task_entry)

            user_data_json = {str(user_id): user_tasks}

            with open(json_filename, mode='w') as json_file:
                json.dump(user_data_json, json_file)
