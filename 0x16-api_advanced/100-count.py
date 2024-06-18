#!/usr/bin/python3
"""Module that queries the Reddit API"""

import requests

base_url = "https://www.reddit.com"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 \
        Safari/537.36'
}


def count_words(subreddit, word_list, found_list=[], after=None):
    """Queries a Reddit subreddit"""
    url = base_url + f'/r/{subreddit}/hot.json?after={after}'
    posts = requests.get(url, headers=headers)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json().get('data')
        aft = posts.get('after')
        for post in posts.get('children'):
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)

        if aft is not None:
            count_words(subreddit, word_list, found_list, after=aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in results.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for k, v in sorted(result.items(), key=lamda item: item[1],
                               reverse=True):
                print('{}:{}'.format(k, v))
    else:
        return
