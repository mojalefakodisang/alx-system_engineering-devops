#!/usr/bin/python3
"""Module that saves all employee data into JSON file
"""


if __name__ == '__main__':
    import json
    import requests

    basename = "https://jsonplaceholder.typicode.com/"
    u_data = requests.get(basename + "users").json()
    out_dict = {}
    for user in u_data:
        user_id = user.get('id')
        username = user.get('username')
        todos = requests.get(basename+"todos",
                             params={"userId": user_id}).json()

        user_tasks = [{'task': todo.get('title'),
                       'completed': todo.get('completed'),
                       'username': username} for todo in todos]

        out_dict.update({user_id: user_tasks})

    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(out_dict, f)
