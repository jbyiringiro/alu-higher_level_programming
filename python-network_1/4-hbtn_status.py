#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':

    url = "https://intranet.hbtn.io/status"
    if url.startswith("https://"):
        url = "https://alu-intranet.hbtn.io/status"
    res = requests.get(url)
    t = res.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
