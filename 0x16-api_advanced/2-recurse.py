#!/usr/bin/python3
"""Using requests library"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Get Top ten from reddit API"""

    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?&after={after}"

    headers = {"User-Agent": "MyApp/1.0"}
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    if response.status_code == 200:
        data = response.json()

        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])

        after = f"{data['data']['after']}"
        if after is not None:
            return recurse(subreddit, hot_list, after)
    else:
        return hot_list
