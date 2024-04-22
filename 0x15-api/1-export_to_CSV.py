#!/usr/bin/python3
"""Module that exports a user tasks to CSV
"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    basename = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(basename + "users/" + user_id).json()
    todos_data = requests.get(basename + "todos",
                              params={"userId": user_id}).json()

    c_file = f"{user_id}.csv"
    with open(c_file, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            slctd = [task.get(key, 'N/A') for key in ['completed', 'title']]
            line = [user_data.get('id'), user_data.get('username')] + slctd
            writer.writerow(line)
