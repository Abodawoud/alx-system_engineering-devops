#!/usr/bin/python3
"""REST API"""
import csv
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

            csv_filename = f"{get_users_data.get('id')}.csv"

            with open(csv_filename, mode='w', newline='') as csv_file:
                fieldnames = ["USER_ID", "USERNAME",
                              "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                writer = csv.DictWriter(
                    csv_file,  quoting=csv.QUOTE_NONNUMERIC,
                    fieldnames=fieldnames)
                for todo in get_todos_data:
                    todo_completed_status = "True" if todo.get(
                        'completed') else "False"
                    todo_title = todo.get('title')

                    writer.writerow({
                        "USER_ID": f"{get_users_data.get('id')}",
                        "USERNAME": get_users_data.get('username'),
                        "TASK_COMPLETED_STATUS": todo_completed_status,
                        "TASK_TITLE": todo_title
                    })
