#!/usr/bin/python3
"""
Module
"""
import sys
import urllib.request as request
import urllib.parse as parse
import urllib.error as error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
