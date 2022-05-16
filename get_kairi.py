from datetime import datetime

import numpy as np
import pandas as pd
import talib as ta

from api_client.client_binance import ClientBinance
from api_client.client_bybit import ClientBybit

from const import *


def get_binance_btc_usd_index_price_kairi(period='15m'):
    symbol = 'BTCUSD_PERP'
    client = ClientBinance()

    response_data = client.get_d_api_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume',
        'Close time',
        'Quote asset volume',
        'Number of trades',
        'Taker buy base asset volume',
        'Taker buy quote asset volume',
        'Ignore.',
    ]

    klines = pd.DataFrame(response_data, columns=columns)

    response_data = client.get_d_api_index_price_klines(symbol='BTCUSD', period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close (or latest price)',
        'Ignore',
        'Close time',
        'Ignore',
        'Number of bisic data',
        'Ignore',
        'Ignore',
        'Ignore',
    ]

    index_klines = pd.DataFrame(response_data, columns=columns)

    klines['time'] = (klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)
    klines.rename(columns={'Close': 'close'}, inplace=True)
    index_klines.rename(columns={'Close (or latest price)': 'index_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['index_close'].astype(float)

    data = pd.merge(klines, index_klines, left_index=True, right_index=True)

    data['kairi_pct'] = round((data['close'] / data['index_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BINANCE,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_binance_btc_usd_mark_price_kairi(period='15m'):
    symbol = 'BTCUSD_PERP'
    client = ClientBinance()

    response_data = client.get_d_api_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume',
        'Close time',
        'Quote asset volume',
        'Number of trades',
        'Taker buy base asset volume',
        'Taker buy quote asset volume',
        'Ignore.',
    ]

    klines = pd.DataFrame(response_data, columns=columns)

    response_data = client.get_d_api_mark_price_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close (or latest price)',
        'Ignore',
        'Close time',
        'Ignore',
        'Number of bisic data',
        'Ignore',
        'Ignore',
        'Ignore',
    ]

    index_klines = pd.DataFrame(response_data, columns=columns)

    klines['time'] = (klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)
    klines.rename(columns={'Close': 'close'}, inplace=True)
    index_klines.rename(columns={'Close (or latest price)': 'mark_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['mark_close'].astype(float)

    data = pd.merge(klines, index_klines, left_index=True, right_index=True)

    data['kairi_pct'] = round((data['close'] / data['mark_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BINANCE,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_binance_btc_usdt_index_price_kairi(period='15m'):
    symbol = 'BTCUSDT'
    client = ClientBinance()

    response_data = client.get_f_api_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume',
        'Close time',
        'Quote asset volume',
        'Number of trades',
        'Taker buy base asset volume',
        'Taker buy quote asset volume',
        'Ignore.',
    ]

    klines = pd.DataFrame(response_data, columns=columns)

    response_data = client.get_f_api_index_price_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close (or latest price)',
        'Ignore',
        'Close time',
        'Ignore',
        'Number of bisic data',
        'Ignore',
        'Ignore',
        'Ignore',
    ]

    index_klines = pd.DataFrame(response_data, columns=columns)

    klines['time'] = (klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)
    klines.rename(columns={'Close': 'close'}, inplace=True)
    index_klines.rename(columns={'Close (or latest price)': 'index_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['index_close'].astype(float)

    data = pd.merge(klines, index_klines, left_index=True, right_index=True)

    data['kairi_pct'] = round((data['close'] / data['index_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BINANCE,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_binance_btc_usdt_mark_price_kairi(period='15m'):
    symbol = 'BTCUSDT'
    client = ClientBinance()

    response_data = client.get_f_api_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume',
        'Close time',
        'Quote asset volume',
        'Number of trades',
        'Taker buy base asset volume',
        'Taker buy quote asset volume',
        'Ignore.',
    ]

    klines = pd.DataFrame(response_data, columns=columns)

    response_data = client.get_f_api_mark_price_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time',
        'Open',
        'High',
        'Low',
        'Close (or latest price)',
        'Ignore',
        'Close time',
        'Ignore',
        'Number of bisic data',
        'Ignore',
        'Ignore',
        'Ignore',
    ]

    index_klines = pd.DataFrame(response_data, columns=columns)

    klines['time'] = (klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['Open time'] / 1000).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)
    klines.rename(columns={'Close': 'close'}, inplace=True)
    index_klines.rename(columns={'Close (or latest price)': 'mark_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['mark_close'].astype(float)

    data = pd.merge(klines, index_klines, left_index=True, right_index=True)

    data['kairi_pct'] = round((data['close'] / data['mark_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BINANCE,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_bybit_btc_usd_index_price_kairi(period=15):
    symbol = 'BTCUSD'
    client = ClientBybit()

    response_data = client.get_inverse_kline(symbol=symbol, interval=period, limit=500)
    klines = pd.DataFrame(response_data)

    response_data = client.get_inverse_index_price_kline(symbol=symbol, interval=period, limit=500)
    index_klines = pd.DataFrame(response_data)

    klines['time'] = (klines['open_time']).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['open_time']).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)

    index_klines.rename(columns={'close': 'index_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['index_close'].astype(float)
    data = pd.merge(klines, index_klines, left_index=True, right_index=True)
    data['kairi_pct'] = round((data['close'] / data['index_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BYBIT,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_bybit_btc_usd_mark_price_kairi(period=15):
    symbol = 'BTCUSD'
    client = ClientBybit()

    response_data = client.get_inverse_kline(symbol=symbol, interval=period, limit=500)
    klines = pd.DataFrame(response_data)

    response_data = client.get_inverse_mark_price_kline(symbol=symbol, interval=period, limit=500)
    index_klines = pd.DataFrame(response_data)

    klines['time'] = (klines['open_time']).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['start_at']).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)

    index_klines.rename(columns={'close': 'mark_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['mark_close'].astype(float)
    data = pd.merge(klines, index_klines, left_index=True, right_index=True)
    data['kairi_pct'] = round((data['close'] / data['mark_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BYBIT,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_bybit_btc_usdt_index_price_kairi(period=15):
    symbol = 'BTCUSDT'
    client = ClientBybit()

    response_data = client.get_linear_kline(symbol=symbol, interval=period, limit=500)
    klines = pd.DataFrame(response_data)

    response_data = client.get_linear_index_price_kline(symbol=symbol, interval=period, limit=500)
    index_klines = pd.DataFrame(response_data)

    klines['time'] = (klines['open_time']).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['open_time']).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)

    index_klines.rename(columns={'close': 'index_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['index_close'].astype(float)
    data = pd.merge(klines, index_klines, left_index=True, right_index=True)
    data['kairi_pct'] = round((data['close'] / data['index_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BYBIT,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_bybit_btc_usdt_mark_price_kairi(period=15):
    symbol = 'BTCUSDT'
    client = ClientBybit()

    response_data = client.get_linear_kline(symbol=symbol, interval=period, limit=500)
    klines = pd.DataFrame(response_data)

    response_data = client.get_linear_mark_price_kline(symbol=symbol, interval=period, limit=500)
    index_klines = pd.DataFrame(response_data)

    klines['time'] = (klines['open_time']).apply(datetime.fromtimestamp)
    klines.set_index('time', inplace=True)
    index_klines['time'] = (index_klines['start_at']).apply(datetime.fromtimestamp)
    index_klines.set_index('time', inplace=True)

    index_klines.rename(columns={'close': 'mark_close'}, inplace=True)

    klines = klines['close'].astype(float)
    index_klines = index_klines['mark_close'].astype(float)
    data = pd.merge(klines, index_klines, left_index=True, right_index=True)
    data['kairi_pct'] = round((data['close'] / data['mark_close'] - 1) * 100, 4)
    # data['kairi_pct'] = ta.EMA(data['kairi_pct'], timeperiod=24)
    data['kairi_pct'] = data['kairi_pct'].replace([np.nan], [None])

    return {
        'exchange': BYBIT,
        'symbol': symbol,
        'values': data['kairi_pct'].to_list(),
        'indexes': data.index.strftime(TIME_FORMAT).to_list()
    }


def get_btc_index_price_kairi():
    return [
        get_binance_btc_usd_index_price_kairi(),
        get_binance_btc_usdt_index_price_kairi(),
        get_bybit_btc_usd_index_price_kairi(),
        get_bybit_btc_usdt_index_price_kairi()
    ]


def get_btc_mark_price_kairi():
    return [
        get_binance_btc_usd_mark_price_kairi(),
        get_binance_btc_usdt_mark_price_kairi(),
        get_bybit_btc_usd_mark_price_kairi(),
        get_bybit_btc_usdt_mark_price_kairi()
    ]


if __name__ == '__main__':
    print(get_btc_index_price_kairi())
    print(get_btc_mark_price_kairi())
