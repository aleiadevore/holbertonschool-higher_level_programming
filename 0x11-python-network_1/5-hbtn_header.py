#!/usr/bin/python3
""" akes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response """

from sys import argv
import requests


if __name__ == "__main__":
        r = requests.get(argv[1])
        for key, value in r.headers.items():
                if key == "x-request-id":
                        print(value)
