#!/usr/bin/python3
""" ist 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” """


from sys import argv
import requests

if __name__ == "__main__":
        repo = argv[1]
        owner = argv[2]

        r = requests.get("https://api.github.com/repos/{}/{}/commits".format(
                owner, repo), params={"page": 1, "per_page": 10})

        for item in r.json():
                author = item.get('commit').get('author').get('name')
                print("{}: {}".format(item['sha'], author))
