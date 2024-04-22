#!/usr/bin/python3
"""Module that returns tasks of an employee
"""

if __name__ == '__main__':
    import requests
    import sys

    user_id = int(sys.argv[1])
    basename = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(basename + "users")
    todos_data = requests.get(basename + "todos")

    for user in user_data.json():
        if user['id'] == user_id:
            name = user['name']
        l_tasks = []
        count = total = 0
        for task in todos_data.json():
            title = task['title']
            userId = task['userId']
            completed = task['completed']
            if user_id == userId:
                if completed:
                    count += 1
                    l_tasks.append(title)
                total += 1

    print(f"Employee {name} is done with tasks({count}/{total}):")
    for x in l_tasks:
        print(f"\t {x}")
