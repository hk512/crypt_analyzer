from datetime import datetime
from datetime import timedelta

import pandas as pd

from api_client.client_ftx import ClientFTX
from api_client.client_bitmex import ClientBitMEX
from api_client.client_bybit import ClientBybit
from api_client.client_okx import ClientOKX
from api_client.client_huobi import ClientHuobi
from api_client.client_bitfinex import ClientBitfinex
from api_client.client_phemex import ClientPhemex
from api_client.client_dydx import ClientDydx
from api_client.client_deribit import ClientDeribit
from api_client.client_binance import ClientBinance
from const import *


def get_ftx_btc_prep_funding_rate_history():
    symbol = 'BTC-PERP'
    client = ClientFTX()
    response = client.get_funding_rates(symbol=symbol)
    data = pd.DataFrame(response['result'])
    data['time'] = [datetime.strptime(value, '%Y-%m-%dT%H:%M:%S+00:00') + timedelta(hours=9) for value in
                    data['time'].values]
    data.set_index('time', inplace=True)
    data.drop(columns=['future'], inplace=True)
    data.rename(columns={'rate': 'funding_rate'}, inplace=True)
    data = data.sort_index()

    return {
        'exchange': FTX,
        'symbol': symbol,
        'data_frame': data
    }


def get_binance_btc_usd_funding_rate_history():
    symbol = 'BTCUSD_PERP'
    client = ClientBinance()
    response = client.get_d_api_funding_rate(symbol=symbol, limit=100)
    data = pd.DataFrame(response)
    data['time'] = (data['fundingTime'] / 1000).apply(datetime.fromtimestamp)
    data.set_index('time', inplace=True)
    data.drop(columns=['symbol', 'fundingTime'], inplace=True)
    data.rename(columns={'fundingRate': 'funding_rate'}, inplace=True)

    return {
        'exchange': BINANCE,
        'symbol': symbol,
        'data_frame': data
    }


def get_binance_btc_usdt_funding_rate_history():
    symbol = 'BTCUSDT'
    client = ClientBinance()
    response = client.get_f_api_funding_rate(symbol=symbol, limit=100)
    data = pd.DataFrame(response)
    data['time'] = (data['fundingTime'] / 1000).apply(datetime.fromtimestamp)
    data.set_index('time', inplace=True)
    data.drop(columns=['symbol', 'fundingTime'], inplace=True)
    data.rename(columns={'fundingRate': 'funding_rate'}, inplace=True)

    return {
        'exchange': BINANCE,
        'symbol': symbol,
        'data_frame': data
    }


def get_bitmex_xbt_usd_funding_rate_history():
    symbol = 'XBTUSD'
    client = ClientBitMEX()
    response = client.get_funding(symbol=symbol)
    data = pd.DataFrame(response)
    data['time'] = [datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(hours=9) for value in
                    data['timestamp'].values]
    data.set_index('time', inplace=True)
    data.drop(columns=['symbol', 'timestamp', 'fundingInterval', 'fundingRateDaily'], inplace=True)
    data.rename(columns={'fundingRate': 'funding_rate'}, inplace=True)
    data = data.sort_index()

    return {
        'exchange': BITMEX,
        'symbol': symbol,
        'data_frame': data
    }


def get_bitmex_xbt_usdt_funding_rate_history():
    symbol = 'XBTUSDT'
    client = ClientBitMEX()
    response = client.get_funding(symbol=symbol)
    data = pd.DataFrame(response)
    data['time'] = [datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(hours=9) for value in
                    data['timestamp'].values]
    data.set_index('time', inplace=True)
    data.drop(columns=['symbol', 'timestamp', 'fundingInterval', 'fundingRateDaily'], inplace=True)
    data.rename(columns={'fundingRate': 'funding_rate'}, inplace=True)
    data = data.sort_index()

    return {
        'exchange': BITMEX,
        'symbol': symbol,
        'data_frame': data
    }


def get_okx_btc_usd_funding_rate_history():
    symbol = 'BTC-USD-SWAP'
    client = ClientOKX()
    response = client.get_funding_rate_history(symbol=symbol)
    data = pd.DataFrame(response['data'])
    data['time'] = (data['fundingTime'].astype(int) / 1000).apply(datetime.fromtimestamp)
    data.set_index('time', inplace=True)
    data.drop(columns=['realizedRate', 'instType', 'instId', 'fundingTime'], inplace=True)
    data.rename(columns={'fundingRate': 'funding_rate'}, inplace=True)
    data = data.sort_index()

    return {
        'exchange': OKX,
        'symbol': symbol,
        'data_frame': data
    }


def get_okx_btc_usdt_funding_rate_history():
    symbol = 'BTC-USDT-SWAP'
    client = ClientOKX()
    response = client.get_funding_rate_history(symbol=symbol)
    data = pd.DataFrame(response['data'])
    data['time'] = (data['fundingTime'].astype(int) / 1000).apply(datetime.fromtimestamp)
    data.set_index('time', inplace=True)
    data.drop(columns=['realizedRate', 'instType', 'instId', 'fundingTime'], inplace=True)
    data.rename(columns={'fundingRate': 'funding_rate'}, inplace=True)
    data = data.sort_index()

    return {
        'exchange': OKX,
        'symbol': symbol,
        'data_frame': data
    }


def get_huobi_btc_usd_funding_rate_history():
    symbol = 'BTC-USD'
    client = ClientHuobi()

    response = client.get_swap_historical_funding_rate(symbol=symbol, page_index=1)
    print(response)
    data = pd.DataFrame(response['data']['data'])
    data['time'] = (data['funding_time'].astype(int) / 1000).apply(datetime.fromtimestamp)
    data.set_index('time', inplace=True)
    data.drop(columns=['symbol', 'fee_asset', 'contract_code', 'funding_time', 'avg_premium_index', 'realized_rate'],
              inplace=True)
    data = data.sort_index()

    return {
        'exchange': HUOBI,
        'symbol': symbol,
        'data_frame': data
    }


def get_huobi_btc_usdt_funding_rate_history():
    symbol = 'BTC-USDT'
    client = ClientHuobi()

    response = client.get_linear_swap_historical_funding_rate(symbol=symbol, page_index=1)
    data = pd.DataFrame(response['data']['data'])
    data['time'] = (data['funding_time'].astype(int) / 1000).apply(datetime.fromtimestamp)
    data.set_index('time', inplace=True)
    data.drop(columns=['symbol', 'fee_asset', 'contract_code', 'funding_time', 'avg_premium_index', 'realized_rate',
                       'trade_partition'], inplace=True)
    data = data.sort_index()

    return {
        'exchange': HUOBI,
        'symbol': symbol,
        'data_frame': data
    }


def get_btc_funding_rate_history() -> pd.DataFrame:
    values = [
        get_ftx_btc_prep_funding_rate_history(),
        get_binance_btc_usd_funding_rate_history(),
        get_binance_btc_usdt_funding_rate_history(),
        get_bitmex_xbt_usd_funding_rate_history(),
        get_bitmex_xbt_usdt_funding_rate_history(),
        get_okx_btc_usd_funding_rate_history(),
        get_okx_btc_usdt_funding_rate_history(),
        get_huobi_btc_usd_funding_rate_history()

    ]

    index = []

    for value in values:
        df = value['data_frame']
        symbol = value['symbol']
        exchange = value['exchange']
        df.rename(columns={'funding_rate': f'{exchange}_{symbol}'}, inplace=True)
        df.index = [value.strftime('%Y/%m/%d %H:%M') for value in df.index]
        index += df.index.to_list()

    data = pd.DataFrame(index=sorted(set(index)))

    for value in values:
        df = value['data_frame']
        data = pd.merge(data, df, left_index=True, right_index=True, how='left')

    return data


if __name__ == '__main__':
    # print(get_ftx_btc_prep_funding_rate_history())
    # print(get_binance_btc_usd_funding_rate_history())
    # print(get_binance_btc_usdt_funding_rate_history())
    # print(get_bitmex_xbt_usd_funding_rate_history())
    # print(get_bitmex_xbt_usdt_funding_rate_history())
    # print(get_okx_btc_usd_funding_rate_history())
    # print(get_okx_btc_usdt_funding_rate_history())
    # print(get_huobi_btc_usd_funding_rate_history())
    # print(get_huobi_btc_usdt_funding_rate_history())
    print(get_btc_funding_rate_history().columns)
