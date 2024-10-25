#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function to fetch and print titles of hot posts from a subreddit."""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if the response status code is not 200
        if RESPONSE.status_code != 200:
            print(None)
            return
        
        HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
        
        # Check if there are no hot posts
        if not HOT_POSTS:
            print(None)
            return
        
        # Print the titles of the first 10 hot posts
        for post in HOT_POSTS:
            print(post.get('data').get('title'))
        
        return "OK"  # Indicate successful retrieval

    except requests.exceptions.RequestException:
        print(None)  # Handle request exceptions
