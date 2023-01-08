import configparser
import time
import pandas as pd

from coincheck import Coincheck


conf = configparser.ConfigParser()
conf.read('config.ini')

ACCEES_KEY = conf['coincheck']['access_key']
SECRET_KEY = conf['coincheck']['secret_key']

coincheck = Coincheck(access_key=ACCEES_KEY, secret_key=SECRET_KEY)

interval = 1
duration = 20

df = pd.DataFrame()
while True:
    time.sleep(interval)
    df = df.append(
        {'price': coincheck.last}, ignore_index=True
    )

    if len(df) < duration:
        continue

    # ポリンジャーバンドの計算
    df['SMA'] = df['price'].rolling(window=duration).mean()
    df['std'] = df['price'].rolling(window=duration).std()

    df['-2σ'] = df['SMA'] - 2*df['std']
    df['+2σ'] = df['SMA'] + 2*df['std']

    # df['カラム名']iloc[-1] は最後の値を取得

    # logic
    # -2σを割ったら買いを入れる
    if df['price'].iloc[-1] < df['-2σ'].iloc[-1]:
        print('buy!!!')

    # +2σを超えたら売りを入れる
    if df['+2σ'].iloc[-1] < df['price'].iloc[-1]:
        print('sell!!!')
