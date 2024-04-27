#!/bin/bash
# takes in a URL, sends a request to that URL and displays the size of the body of the response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
