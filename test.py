
'''
learning to use the requests library to play with APIs

'''

import sys
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
    
    if len(sys.argv) > 2:
        parameters = {
            'lat': sys.argv[1],
            'lon': sys.argv[2]
        }

        response = requests.get('http://api.open-notify.org/iss-pass.json', params = parameters)

        if response.status_code == 200:
            jprint(response.json())
