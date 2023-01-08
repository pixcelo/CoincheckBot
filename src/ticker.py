import requests

BASE_URL = 'https://coincheck.com'
url = BASE_URL + '/api/ticker'

r = requests.get(url)
r = r.json()

print('最新価格：', r['last'])