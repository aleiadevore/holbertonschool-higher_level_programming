#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a
parameter """

import requests
from sys import argv


if __name__ == "__main__":
        url = 'http://0.0.0.0:5000/search_user'

        if len(argv) > 0:
                letter = argv[1]
        else:
                letter = ""

        data = {'q': letter}
        response = requests.post(url, data=data)
        try:
                if response.json():
                        id = response.json()['id']
                        name = response.json()['name']
                        print("[{}] {}".format(id, name))
                else:
                        print("No result")
        except:
                print("Not a valid JSON")
