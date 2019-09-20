
'''
learning to use the requests library to play with APIs

'''

import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object

    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

if __name__ == '__main__':

    response = requests.get('http://api.open-notify.org/astros.json')

    if response.status_code == 200:
        jprint(response.json())
