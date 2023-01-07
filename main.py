import requests

url = 'https://coincheck.com/api/ticker'

r = requests.get(url)
print(r.json())
#  {'last': 2239853.0, 'bid': 2239604.0, 'ask': 2240041.0, 'high': 2245372.0, 'low': 2237000.0, 'volume': 364.79393303, 'timestamp': 1673127354}