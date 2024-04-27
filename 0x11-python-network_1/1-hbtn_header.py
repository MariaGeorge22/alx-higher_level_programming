#!/usr/bin/python3
"""
Module
"""
import sys
import urllib.request as request

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        body = response.read()
        headers = response.info()
        print(headers.get('X-Request-Id'))
