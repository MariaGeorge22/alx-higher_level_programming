#!/bin/bash
# takes in a URL, sends a GET request to the URL, and stores the body and status code in an array
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f2-
