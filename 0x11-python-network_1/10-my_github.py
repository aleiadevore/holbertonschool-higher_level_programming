#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

from sys import argv
import requests

usr = argv[1]
pswd = argv[2]

if __name__ == "__main__":
        for k, v in requests.get("http://api.github.com/{}".format(usr),
                                 auth=(usr, pswd)).headers.items():
                if k == 'x-github-request-id':
                        print(v)
