import requests

url = 'https://coincheck.com/api/ticker'

r = requests.get(url)
print(r.json())