from pprint import pprint

import requests

BASE_URL = 'https://coincheck.com'
url = BASE_URL + '/api/order_books'

params = {
    'limit': 10
}

r = requests.get(url, params=params)
r = r.json()

pprint(r)