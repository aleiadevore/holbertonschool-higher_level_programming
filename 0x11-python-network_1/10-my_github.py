#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

usr = argv[1]
pswd = argv[2]

if __name__ == "__main__":
        r = requests.get("http://api.github.com/user",
                         auth=HTTPBasicAuth(usr, pswd))
        try:
                print(r.json()[id])
        except:
                print("None")
