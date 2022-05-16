from datetime import datetime

import joblib

from api_client.client_bybit import ClientBybit
from api_client.client_binance import ClientBinance

from const import *


class LongShortRatio(object):
    def __init__(self, exchange, symbol, period, indexes, top_long_account_ratios, top_long_position_ratios,
                 global_long_account_ratios):
        self.exchange = exchange
        self.symbol = symbol
        self.period = period
        self.indexes = indexes
        self.top_long_account_ratios = top_long_account_ratios
        self.top_long_position_ratios = top_long_position_ratios
        self.global_long_account_ratios = global_long_account_ratios

    @property
    def values(self):
        return {
            'exchange': self.exchange,
            'symbol': self.symbol,
            'period': self.period,
            'indexes': self.indexes,
            'top_long_account_ratios': self.top_long_account_ratios,
            'top_long_position_ratios': self.top_long_position_ratios,
            'global_long_account_ratios': self.global_long_account_ratios,
        }


def get_binance_btcusd_long_short_ratio(period='15m'):
    symbol = 'BTCUSD'
    client = ClientBinance()

    top_long_account_ratios = []
    top_long_position_ratios = []
    global_long_account_ratios = []
    indexes = []

    response_data = client.get_d_api_top_long_short_account_ratio(symbol=symbol, period=period, limit=500)
    
    for values in response_data:
        indexes.append(datetime.fromtimestamp(values['timestamp'] / 1000).strftime(TIME_FORMAT))
        top_long_account_ratios.append(float(values['longAccount']))

    response_data = client.get_d_api_top_long_short_position_ratio(symbol=symbol, period=period, limit=500)

    for values in response_data:
        top_long_position_ratios.append(float(values['longPosition']))

    response_data = client.get_d_api_global_long_short_account_ratio(symbol=symbol, period=period, limit=500)

    for values in response_data:
        global_long_account_ratios.append(float(values['longAccount']))

    return LongShortRatio(
        exchange=BINANCE,
        symbol=symbol,
        period=period,
        indexes=indexes,
        top_long_account_ratios=top_long_account_ratios,
        top_long_position_ratios=top_long_position_ratios,
        global_long_account_ratios=global_long_account_ratios,
    )


def get_binance_btcusdt_long_short_ratio(period='15m'):
    symbol = 'BTCUSDT'
    client = ClientBinance()

    top_long_account_ratios = []
    top_long_position_ratios = []
    global_long_account_ratios = []
    indexes = []

    response_data = client.get_f_api_top_long_short_account_ratio(symbol=symbol, period=period, limit=500)

    for values in response_data:
        indexes.append(datetime.fromtimestamp(values['timestamp'] / 1000).strftime(TIME_FORMAT))
        top_long_account_ratios.append(float(values['longAccount']))

    response_data = client.get_f_api_top_long_short_position_ratio(symbol=symbol, period=period, limit=500)

    for values in response_data:
        top_long_position_ratios.append(float(values['longAccount']))

    response_data = client.get_f_api_global_long_short_account_ratio(symbol=symbol, period=period, limit=500)

    for values in response_data:
        global_long_account_ratios.append(float(values['longAccount']))

    return LongShortRatio(
        exchange=BINANCE,
        symbol=symbol,
        period=period,
        indexes=indexes,
        top_long_account_ratios=top_long_account_ratios,
        top_long_position_ratios=top_long_position_ratios,
        global_long_account_ratios=global_long_account_ratios,
    )


def get_bybit_btcusdt_long_short_ratio(period='15min'):
    symbol = 'BTCUSDT'
    client = ClientBybit()
    global_long_account_ratios = []
    indexes = []

    response_data = client.get_account_ratio(symbol=symbol, period=period, limit=500)

    for values in reversed(response_data['result']):
        indexes.append(datetime.fromtimestamp(values['timestamp']).strftime(TIME_FORMAT))
        global_long_account_ratios.append(float(values['buy_ratio']))

    return LongShortRatio(
        exchange=BYBIT,
        symbol=symbol,
        period=period,
        indexes=indexes,
        top_long_account_ratios=None,
        top_long_position_ratios=None,
        global_long_account_ratios=global_long_account_ratios,
    )


def get_bybit_btcusd_long_short_ratio(period='15min'):
    symbol = 'BTCUSD'
    client = ClientBybit()
    global_long_account_ratios = []
    indexes = []

    response_data = client.get_account_ratio(symbol=symbol, period=period, limit=500)

    for values in reversed(response_data['result']):
        indexes.append(datetime.fromtimestamp(values['timestamp']).strftime(TIME_FORMAT))
        global_long_account_ratios.append(float(values['buy_ratio']))

    return LongShortRatio(
        exchange=BYBIT,
        symbol=symbol,
        period=period,
        indexes=indexes,
        top_long_account_ratios=None,
        top_long_position_ratios=None,
        global_long_account_ratios=global_long_account_ratios,
    )


def get_btc_long_short_ratio():
    return [
        get_binance_btcusd_long_short_ratio().values,
        get_binance_btcusdt_long_short_ratio().values,
        get_bybit_btcusd_long_short_ratio().values,
        get_bybit_btcusdt_long_short_ratio().values
    ]


if __name__ == '__main__':
    print(get_binance_btcusd_long_short_ratio().values)
    print(get_binance_btcusdt_long_short_ratio().values)
    print(get_bybit_btcusd_long_short_ratio().values)
    print(get_bybit_btcusdt_long_short_ratio().values)
