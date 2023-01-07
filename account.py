import hmac
import hashlib
import time
from pprint import pprint
import configparser

import requests

# iniファイルの読み込み
conf = configparser.ConfigParser()
conf.read('config.ini')

ACCESS_KEY = conf['coincheck']['access_key']
SECRET_KEY = conf['coincheck']['secret_key']

BASE_URL = 'https://coincheck.com'
url = BASE_URL + '/api/accounts/balance'

# ACCESS NONCEの設定（正の整数に変換したUNIXスタンプを、ACCESS NONCEにする）
nonce = str(int(time.time()))

body = ''
message = nonce + url + body

# ACCESS SIGNATUREの作成
signature = hmac.new(SECRET_KEY.encode(),
                     message.encode(),
                     hashlib.sha256).hexdigest()

# リクエストヘッダー
headers = {
    'ACCESS-KEY': ACCESS_KEY,
    'ACCESS-NONCE': nonce,
    'ACCESS-SIGNATURE': signature,
    'Content-Type': 'application/json'
}

r = requests.get(url, headers=headers)
r = r.json()

pprint(r)