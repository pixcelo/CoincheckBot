import configparser

conf = configparser.ConfigParser()
conf.read('config.ini')

ACCESS_KEY = conf['coincheck']['access_key']
SECRET_KEY = conf['coincheck']['secret_key']

print(ACCESS_KEY)
print(SECRET_KEY)