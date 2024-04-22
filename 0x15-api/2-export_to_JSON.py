#!/usr/bin/python3
"""Module that converts user data to JSON file
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    basename = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(basename + "users/" + user_id).json()
    tasks_data = requests.get(basename + "todos",
                              params={'userId': user_id}).json()

    l_tasks = [{'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user_data.get('username')} for task in tasks_data]

    filename = f"{user_id}.json"
    with open(filename, "w") as f:
        json.dump({f"{user_id}": l_tasks}, f)
