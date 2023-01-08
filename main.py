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
AMOUNT = 0.005

df = pd.DataFrame()
while True:
    time.sleep(interval)
    positions = coincheck.position

    # 残高チェック
    if not positions.get('jpy'):
        raise

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
    if 'btc' in positions.keys():
        if df['+2σ'].iloc[-1] < df['price'].iloc[-1] \
                and coincheck.ask_rate < df['price'].iloc[-1]:
            params = {
                'pair': 'btc_jpy',
                'order_type': 'market_sell',
                'amount': positions['btc']
            }
            r = coincheck.order(params)
            print('exit', r)
    else:
        # もし-2σを割ったら
        if df['price'].iloc[-1] < df['-2σ'].iloc[-1]:
            market_buy_amount = coincheck.rate({'order_type': 'buy',
                                                'pair': 'btc_jpy',
                                                'amount': AMOUNT})
            print('使用する日本円', market_buy_amount['price'])
            params = {
                'pair': 'btc_jpy',
                'order_type': 'market_buy',
                'market_buy_amount': market_buy_amount['price']
            }

            r = coincheck.order(params)
            print('entry', r)

        # もし+2σを割ったら
        if df['+2σ'].iloc[-1] < df['price'].iloc[-1] \
                and coincheck.ask_rate < df['price'].iloc[-1]:
            params = {
                'pair': 'btc_jpy',
                'order_type': 'market_sell',
                'amount': positions['btc']
            }
            r = coincheck.order(params)
            print('exit', r)
