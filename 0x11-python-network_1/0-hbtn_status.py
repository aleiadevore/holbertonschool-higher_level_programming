#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

from urllib import request

if __name__ == "__main__":
        with request.urlopen('https://intranet.hbtn.io/status') as text:
                html = text.read()
                print(type(html))
                print(html)
                print(html.decode('utf-8'))
