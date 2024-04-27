#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    user_name = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/users/{user_name}"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    with requests.get(url, headers=headers) as response:
        print(response.json().get("id"))
