#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        body = response.headers.get('X-Request-Id')
        print(body)
