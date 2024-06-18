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


def recurse(subreddit, hot_list=[], after=None):
    """Queries a Reddit subreddit and return number of subscribers"""
    if after is not None:
        url = f"{base_url}/r/{subreddit}/hot.json?after={after}"
    else:
        url = f"{base_url}/r/{subreddit}/hot.json"

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json().get('data', {})
        children = data.get('children', {})

        for post in children:
            hot_list.append(post['data']['title'])

        after = data.get('after')

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
