#!/usr/bin/python3
"""Using requests lib"""
import requests


def number_of_subscribers(subreddit):
    """Get Subscriber from reddit API"""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 302:
        return 0
    else:
        return 0
