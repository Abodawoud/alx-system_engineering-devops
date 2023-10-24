#!/usr/bin/python3
"""REST API"""
import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com"

    users_list = requests.get(f'{URL}/users').json()
    todos_list = requests.get(f'{URL}/todos').json()
    todo_all_employees = {}

    for user in users_list:
        user_id = user.get('id')
        employee_todos_list = []
        for todo in todos_list:
            if todo.get('userId') == user_id:
                employee_todos_list.append({
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })

        todo_all_employees[user_id] = employee_todos_list

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(todo_all_employees, outfile)
