#!/usr/bin/python3
""" akes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response """

from sys import argv
from urllib import request


if __name__ == "__main__":
        data = "X-Request-Id".encode('utf-8')
        req = request.Request(argv[1], data=data)
        with request.urlopen(req) as text:
                html = text.read()
                for line in html:
                        print(line)