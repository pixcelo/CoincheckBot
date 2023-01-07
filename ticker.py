from pprint import pprint

import requests

BASE_URL = 'https://coincheck.com'
url = BASE_URL + '/api/ticker'

r = requests.get(url)
pprint(r.json())
