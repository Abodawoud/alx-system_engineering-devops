#!/usr/bin/python3
"""Using requests library"""
import requests


def top_ten(subreddit):
    """Get Top ten from reddit API"""
    api_url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"

    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for i in range(0, 10):
            print(data["data"]["children"][i]["data"]["title"])
    elif response.status_code == 302:
        print(None)
    else:
        print(None)
