#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Queries a Reddit subreddit and return number of subscribers"""
    if (subreddit is None or len(subreddit) < 1
            or not isinstance(subreddit, str) is True):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url)
    if response.status_code == 200:
        d_json = response.json()
        return d_json['data']['subscribers']
    else:
        return 0
