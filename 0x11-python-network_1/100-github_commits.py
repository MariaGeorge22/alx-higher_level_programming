#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    with requests.get(url, headers=headers) as response:
        for commit in response.json()[:10]:
            print(commit.get("sha"), end=": ")
            print(commit.get("commit").get("author").get("name"))
