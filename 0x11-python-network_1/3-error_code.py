#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

from urllib import request
from sys import argv
import urllib

if __name__ == "__main__":
        req = request.Request(argv[1])
        try:
                with request.urlopen(req) as text:
                        html = text.read()
                        print(html.decode('utf-8'))
        except urllib.error.HTTPError as e:
                print("Error code: {}".format(e.code))
