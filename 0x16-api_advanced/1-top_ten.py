#!/usr/bin/python3
"""Module that queries the Reddit API"""

import requests

base_url = "https://www.reddit.com"

headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 \
                    Safari/537.36'
}


def top_ten(subreddit):
    """Queries a Reddit subreddit and return number of subscribers"""
    res = requests.get("{}/r/{}/.json?\
                       sort=top&limit=10".format(base_url, subreddit),
                       headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json().get('data', {})
        children = data.get('children', {})

        for post in children[0:10]:
            print(post['data']['title'])
    else:
        print(None)
