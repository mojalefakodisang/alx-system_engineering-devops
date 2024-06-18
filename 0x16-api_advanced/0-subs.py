#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Queries a Reddit subreddit and return number of subscribers"""
    base_url = "https://www.reddit.com"
    end_point = "/subreddits/search"

    headers = {
            'Accept': 'application/json',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                    Chrome/111.0.0.0'
    }
    url = "{}/r/{}/about/.json".format(base_url, subreddit)

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200 and 'subscribers' in res.json()['data']:
        return res.json()['data']['subscribers']
    else:
        return 0
