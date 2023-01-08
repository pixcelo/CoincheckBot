import requests
import configparser

conf = configparser.ConfigParser()
conf.read('config.ini')
ACCEES_TOKEN = conf['line']['access_token']

def send_message_to_line(message):
    headers = {
        'Authorization': f'Bearer {ACCEES_TOKEN}'
    }
    data = {'message': message}
    requests.post(url='https://notify-api.line.me/api/notify',
                  headers=headers,
                  data=data)

if __name__ == '__main__':
    send_message_to_line('テスト')