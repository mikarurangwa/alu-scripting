#!/usr/bin/python3
"""
Prints the title of the first 10 hot posts listed for a given subreddit.
If the subreddit is invalid or there are no posts, it prints 'None'.
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python/requests:API_advanced:v1.0 (by /u/your_reddit_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])

        # Check if there are any hot posts
        if not data:
            print(None)
            return

        # Print the titles of the first 10 hot posts
        for post in data:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
