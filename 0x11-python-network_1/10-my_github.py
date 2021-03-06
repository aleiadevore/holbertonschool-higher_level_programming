#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
        usr = argv[1]
        pswd = argv[2]

        r = requests.get("https://api.github.com/user",
                         auth=HTTPBasicAuth(usr, pswd))
        try:
                print(r.json()['id'])
        except:
                print("None")
