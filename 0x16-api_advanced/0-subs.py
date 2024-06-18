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


def number_of_subscribers(subreddit):
    """Queries a Reddit subreddit and return number of subscribers"""
    res = requests.get("{}/r/{}/about.json".format(base_url, subreddit),
                       headers=headers, allow_redirects=False)

    if res.status_code == 200 and 'subscribers' in res.json()['data']:
        return res.json()['data']['subscribers']
    else:
        return 0
