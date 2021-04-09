#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed
URL with email as parameter, and displays body of response """

from sys import argv
from urllib import request
import urllib

data = urllib.parse.urlencode({"email": argv[2]})

data = data.encode('ascii')

url = argv[1]
with request.urlopen(url, data) as text:
        html = text.read()
        print(html.decode('utf-8'))
