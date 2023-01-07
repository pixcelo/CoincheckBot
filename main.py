from pprint import pprint

import requests

BASE_URL = 'https://coincheck.com'
url = BASE_URL + '/api/trades'

r = requests.get(url, params={'pair': 'btc_jpy'})
pprint(r.json())
r = r.json()
print(r)
