#!/usr/bin/python3
"""Module that exports a user tasks to CSV
"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    basename = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(basename + "users")
    todos_data = requests.get(basename + "todos")

    for user in user_data.json():
        if user_id == str(user['id']):
            name = user['name']
            t_tasks = []
            for task in todos_data.json():
                title = task['title']
                userId = str(task['userId'])
                completed = task['completed']
                if userId == user_id:
                    name = user['name']
                    t_tasks.append([user_id, name, completed, title])

    with open(f"{user_id}.csv", "w") as f:
        writer = csv.writer(f)
        for x in t_tasks:
            writer.writerow(x)
