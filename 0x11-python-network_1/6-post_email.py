#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed
URL with email as parameter, and displays body of response """

from sys import argv
import requests

if __name__ == "__main__":
        data = {"email": argv[2]}
        url = argv[1]

        r = requests.post(url, data=data)
        print(r.text)
