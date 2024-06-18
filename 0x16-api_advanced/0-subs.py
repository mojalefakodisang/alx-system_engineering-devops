#!/usr/bin/python3
"""Module that queries the Reddit API"""

import requests


base_url = "https://www.reddit.com"

headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
}


def number_of_subscribers(subreddit):
    """Queries a Reddit subreddit and return number of subscribers"""
    url = base_url + f'/r/{subreddit}/about.json'

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        results = res.json().get('data')
        return results.get('subscribers')
    else:
        return 0
