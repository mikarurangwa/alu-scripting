#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API to print
the titles of the first 10 hot posts for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for the given subreddit.
    If the subreddit is invalid, it prints 'None'.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python/requests:API_advanced:v1.0 (by /u/your_reddit_username)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            if len(data) == 0:
                print(None)
            else:
                for post in data[:10]:
                    print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)
