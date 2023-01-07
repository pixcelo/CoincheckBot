import hmac
import hashlib
import json
import time
from pprint import pprint
import configparser

import requests

conf = configparser.ConfigParser()
conf.read('config.ini')

ACCESS_KEY = conf['coincheck']['access_key']
SECRET_KEY = conf['coincheck']['secret_key']

BASE_URL = 'https://coincheck.com'
url = BASE_URL + '/api/exchange/orders'

nonce = str(int(time.time()))

params = {
    'pair': 'btc_jpy',
    'order_type': 'buy',
    'rate': '2000000',
    'amount': '0.005'
}

body = json.dumps(params)

# body = ''
message = nonce + url + body
signature = hmac.new(SECRET_KEY.encode(),
                     message.encode(),
                     hashlib.sha256).hexdigest()
headers = {
    'ACCESS-KEY': ACCESS_KEY,
    'ACCESS-NONCE': nonce,
    'ACCESS-SIGNATURE': signature,
    'Content-Type': 'application/json'
}

# r = requests.get(url, headers=headers)
r = requests.post(url, headers=headers, data=body)
r = r.json()

pprint(r)