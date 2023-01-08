import configparser

from coincheck import Coincheck

conf = configparser.ConfigParser()
conf.read('config.ini')

ACCESS_KEY = conf['coincheck']['access_key']
SECRET_KEY = conf['coincheck']['secret_key']

coincheck = Coincheck(ACCESS_KEY, SECRET_KEY)
ticker = coincheck.ticker()
print(ticker)