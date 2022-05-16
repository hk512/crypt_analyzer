from datetime import datetime
from datetime import timedelta

import joblib

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
from api_client.client_bitget import ClientBitget
from api_client.client_coinex import ClientCoinex
from api_client.client_gate import ClientGate
from const import *


class DerivativeStatus(object):
    def __init__(self, exchange, symbol, last_price, mark_price, index_price, funding_time_dt, funding_rate,
                 next_funding_time_dt, next_funding_rate, long_short_ratio):
        self.exchange = exchange
        self.symbol = symbol
        self.last_price = last_price
        self.mark_price = mark_price
        self.index_price = index_price
        self.funding_time_dt = funding_time_dt
        self.funding_rate = funding_rate
        self.next_funding_time_dt = next_funding_time_dt
        self.next_funding_rate = next_funding_rate
        self.long_short_ratio = long_short_ratio

    @property
    def funding_time(self):
        if self.funding_time_dt is not None:
            return self.funding_time_dt.strftime('%Y/%m/%d %H:%M')
        else:
            return '-'

    @property
    def next_funding_time(self):
        if self.next_funding_time_dt is not None:
            return self.next_funding_time_dt.strftime('%Y/%m/%d %H:%M')
        else:
            return '-'

    @property
    def mark_price_kairi_pct(self):
        if self.mark_price is not None:
            return round((self.last_price / self.mark_price - 1) * 100, 4)
        else:
            return None

    @property
    def index_price_kairi_pct(self):
        if self.index_price is not None:
            return round((self.last_price / self.index_price - 1) * 100, 4)
        else:
            return None

    @property
    def funding_rate_pct(self):
        if self.funding_rate is not None:
            return round(self.funding_rate * 100, 4)
        else:
            return None

    @property
    def next_funding_rate_pct(self):
        if self.next_funding_rate is not None:
            return round(self.next_funding_rate * 100, 4)
        else:
            return None

    @property
    def values(self):
        return {
            'exchange': self.exchange,
            'symbol': self.symbol,
            'last_price': self.last_price,
            'mark_price': self.mark_price,
            'index_price': self.index_price,
            'mark_price_kairi_pct': self.mark_price_kairi_pct,
            'index_price_kairi_pct': self.index_price_kairi_pct,
            'funding_time': self.funding_time,
            'funding_rate_pct': self.funding_rate_pct,
            'next_funding_time': self.next_funding_time,
            'next_funding_rate_pct': self.next_funding_rate_pct,
            'long_short_ratio': self.long_short_ratio
        }


def get_ftx_btc_prep_derivative_status():
    symbol = 'BTC-PERP'
    client = ClientFTX()

    response_data = client.get_future(symbol=symbol)
    last_price = response_data['result']['last']
    index_price = response_data['result']['index']
    mark_price = response_data['result']['mark']

    response_data = client.get_future_stats(symbol=symbol)
    funding_time = datetime.strptime(response_data['result']['nextFundingTime'], '%Y-%m-%dT%H:%M:%S+00:00') + timedelta(
        hours=9)
    funding_rate = response_data['result']['nextFundingRate']

    return DerivativeStatus(
        exchange=FTX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=None,
        long_short_ratio=None
    )


def get_binance_btc_usd_prep_derivative_status():
    symbol = 'BTCUSD_PERP'
    client = ClientBinance()

    response_data = client.get_d_api_premium_index(symbol=symbol)
    index_price = float(response_data[0]['indexPrice'])
    mark_price = float(response_data[0]['markPrice'])
    funding_rate = float(response_data[0]['lastFundingRate'])
    next_funding_time = datetime.fromtimestamp(int(response_data[0]['nextFundingTime']) / 1000)
    next_funding_rate = float(response_data[0]['interestRate'])

    response_data = client.get_d_api_ticker_price(symbol=symbol)
    last_price = float(response_data[0]['price'])

    response_data = client.get_d_api_global_long_short_account_ratio(symbol='BTCUSD', period='5m', limit=1)
    long_short_ratio = round(float(response_data[-1]['longShortRatio']), 4)

    return DerivativeStatus(
        exchange=BINANCE,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_binance_btc_usdt_derivative_status():
    symbol = 'BTCUSDT'
    client = ClientBinance()

    response_data = client.get_f_api_premium_index(symbol=symbol)
    index_price = float(response_data['indexPrice'])
    mark_price = float(response_data['markPrice'])
    funding_rate = float(response_data['lastFundingRate'])
    next_funding_time = datetime.fromtimestamp(int(response_data['nextFundingTime']) / 1000)
    next_funding_rate = float(response_data['interestRate'])

    response_data = client.get_f_api_ticker_price(symbol=symbol)
    last_price = float(response_data['price'])

    response_data = client.get_f_api_global_long_short_account_ratio(symbol=symbol, period='5m', limit=1)
    long_short_ratio = round(float(response_data[-1]['longShortRatio']), 4)

    return DerivativeStatus(
        exchange=BINANCE,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_binance_btc_busd_derivative_status():
    symbol = 'BTCBUSD'
    client = ClientBinance()

    response_data = client.get_f_api_premium_index(symbol=symbol)
    index_price = float(response_data['indexPrice'])
    mark_price = float(response_data['markPrice'])
    funding_rate = float(response_data['lastFundingRate'])
    next_funding_time = datetime.fromtimestamp(int(response_data['nextFundingTime']) / 1000)
    next_funding_rate = float(response_data['interestRate'])

    response_data = client.get_f_api_ticker_price(symbol=symbol)
    last_price = float(response_data['price'])

    response_data = client.get_f_api_global_long_short_account_ratio(symbol=symbol, period='5m', limit=1)
    long_short_ratio = round(float(response_data[-1]['longShortRatio']), 4)

    return DerivativeStatus(
        exchange=BINANCE,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_bitmex_xbt_usd_derivative_status():
    symbol = 'XBTUSD'
    client = ClientBitMEX()
    response_data = client.get_instrument(symbol=symbol)

    last_price = response_data[0]['lastPrice']
    mark_price = response_data[0]['markPrice']

    funding_time = datetime.strptime(response_data[0]['fundingTimestamp'], '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(
        hours=9)
    funding_rate = response_data[0]['fundingRate']
    next_funding_rate = response_data[0]['indicativeFundingRate']

    return DerivativeStatus(
        exchange=BITMEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=None,
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_bitmex_xbt_usdt_derivative_status():
    symbol = 'XBTUSDT'
    client = ClientBitMEX()
    response_data = client.get_instrument(symbol=symbol)

    last_price = response_data[0]['lastPrice']
    mark_price = response_data[0]['markPrice']

    funding_time = datetime.strptime(response_data[0]['fundingTimestamp'], '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(
        hours=9)
    funding_rate = response_data[0]['fundingRate']
    next_funding_rate = response_data[0]['indicativeFundingRate']

    return DerivativeStatus(
        exchange=BITMEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=None,
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_bitmex_xbt_eur_derivative_status():
    symbol = 'XBTEUR'
    client = ClientBitMEX()
    response_data = client.get_instrument(symbol=symbol)

    last_price = response_data[0]['lastPrice']
    mark_price = response_data[0]['markPrice']

    funding_time = datetime.strptime(response_data[0]['fundingTimestamp'], '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(
        hours=9)
    funding_rate = response_data[0]['fundingRate']
    next_funding_rate = response_data[0]['indicativeFundingRate']

    return DerivativeStatus(
        exchange=BITMEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=None,
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_bybit_btc_usd_derivative_status():
    symbol = 'BTCUSD'
    client = ClientBybit()
    response_data = client.get_tickers(symbol=symbol)

    last_price = float(response_data['result'][0]['last_price'])
    index_price = float(response_data['result'][0]['index_price'])
    mark_price = float(response_data['result'][0]['mark_price'])

    funding_time = datetime.strptime(response_data['result'][0]['next_funding_time'], '%Y-%m-%dT%H:%M:%SZ') + timedelta(
        hours=9)
    funding_rate = float(response_data['result'][0]['funding_rate'])
    next_funding_rate = float(response_data['result'][0]['predicted_funding_rate'])

    response_data = client.get_account_ratio(symbol=symbol, period='5min', limit=1)
    long_rate = response_data['result'][0]['buy_ratio']
    short_rate = response_data['result'][0]['sell_ratio']
    long_short_ratio = round(long_rate / short_rate, 4)

    return DerivativeStatus(
        exchange=BYBIT,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_bybit_btc_usdt_derivative_status():
    symbol = 'BTCUSDT'
    client = ClientBybit()
    response_data = client.get_tickers(symbol=symbol)

    last_price = float(response_data['result'][0]['last_price'])
    index_price = float(response_data['result'][0]['index_price'])
    mark_price = float(response_data['result'][0]['mark_price'])

    funding_time = datetime.strptime(response_data['result'][0]['next_funding_time'], '%Y-%m-%dT%H:%M:%SZ') + timedelta(
        hours=9)
    funding_rate = float(response_data['result'][0]['funding_rate'])
    next_funding_rate = float(response_data['result'][0]['predicted_funding_rate'])

    response_data = client.get_account_ratio(symbol=symbol, period='5min', limit=1)
    long_rate = response_data['result'][0]['buy_ratio']
    short_rate = response_data['result'][0]['sell_ratio']
    long_short_ratio = round(long_rate / short_rate, 4)

    return DerivativeStatus(
        exchange=BYBIT,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_okx_btc_usd_swap_derivative_status():
    symbol = 'BTC-USD-SWAP'
    client = ClientOKX()

    response_data = client.get_ticker(symbol=symbol)
    last_price = float(response_data['data'][0]['last'])

    response_data = client.get_index_ticker(symbol='BTC-USD')
    index_price = float(response_data['data'][0]['idxPx'])

    response_data = client.get_mark_price(symbol=symbol, inst_type='SWAP')
    mark_price = float(response_data['data'][0]['markPx'])

    response_data = client.get_funding_rate(symbol=symbol)

    funding_time = datetime.fromtimestamp(int(response_data['data'][0]['fundingTime']) / 1000)
    funding_rate = float(response_data['data'][0]['fundingRate'])
    next_funding_time = datetime.fromtimestamp(int(response_data['data'][0]['nextFundingTime']) / 1000)
    next_funding_rate = float(response_data['data'][0]['nextFundingRate'])

    response_data = client.get_long_short_account_ratio(symbol='BTC', period='5m')
    long_short_ratio = round(float(response_data['data'][0][1]), 4)

    return DerivativeStatus(
        exchange=OKX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_okx_btc_usdt_swap_derivative_status():
    symbol = 'BTC-USDT-SWAP'
    client = ClientOKX()

    response_data = client.get_ticker(symbol=symbol)
    last_price = float(response_data['data'][0]['last'])

    response_data = client.get_index_ticker(symbol='BTC-USDT')
    index_price = float(response_data['data'][0]['idxPx'])

    response_data = client.get_mark_price(symbol=symbol, inst_type='SWAP')
    mark_price = float(response_data['data'][0]['markPx'])

    response_data = client.get_funding_rate(symbol=symbol)

    funding_time = datetime.fromtimestamp(int(response_data['data'][0]['fundingTime']) / 1000)
    funding_rate = float(response_data['data'][0]['fundingRate'])
    next_funding_time = datetime.fromtimestamp(int(response_data['data'][0]['nextFundingTime']) / 1000)
    next_funding_rate = float(response_data['data'][0]['nextFundingRate'])

    response_data = client.get_long_short_account_ratio(symbol='BTC', period='5m')
    long_short_ratio = round(float(response_data['data'][0][1]), 4)

    return DerivativeStatus(
        exchange=OKX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=long_short_ratio
    )


def get_huobi_btc_usd_derivative_status():
    symbol = 'BTC-USD'
    client = ClientHuobi()

    response_data = client.get_swap_funding_rate(symbol=symbol)

    funding_time = datetime.fromtimestamp(int(response_data['data']['funding_time']) / 1000)
    funding_rate = float(response_data['data']['funding_rate'])
    next_funding_time = datetime.fromtimestamp(int(response_data['data']['next_funding_time']) / 1000)
    next_funding_rate = float(response_data['data']['estimated_rate'])

    return DerivativeStatus(
        exchange=HUOBI,
        symbol=symbol,
        last_price=None,
        mark_price=None,
        index_price=None,
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_huobi_btc_usdt_derivative_status():
    symbol = 'BTC-USDT'
    client = ClientHuobi()

    response_data = client.get_linear_swap_funding_rate(symbol=symbol)

    funding_time = datetime.fromtimestamp(int(response_data['data']['funding_time']) / 1000)
    funding_rate = float(response_data['data']['funding_rate'])
    next_funding_time = datetime.fromtimestamp(int(response_data['data']['next_funding_time']) / 1000)
    next_funding_rate = float(response_data['data']['estimated_rate'])

    return DerivativeStatus(
        exchange=HUOBI,
        symbol=symbol,
        last_price=None,
        mark_price=None,
        index_price=None,
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_bitfinex_tbtcf0_ustf0_derivative_status():
    symbol = 'tBTCF0:USTF0'
    client = ClientBitfinex()

    response_data = client.get_deriv_status(symbol=symbol)

    last_price = response_data[0][3]
    mark_price = response_data[0][15]
    funding_rate = response_data[0][12]
    next_funding_time = datetime.fromtimestamp(response_data[0][8] / 1000)
    next_funding_rate = response_data[0][9]

    return DerivativeStatus(
        exchange=BITFINEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=None,
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=next_funding_time,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_phemex_btc_usd_derivative_status():
    symbol = 'BTCUSD'
    client = ClientPhemex()

    response_data = client.get_ticker(symbol=symbol)

    last_price = response_data['result']['close'] / 10000
    index_price = response_data['result']['indexPrice'] / 10000
    mark_price = response_data['result']['markPrice'] / 10000
    funding_rate = response_data['result']['fundingRate'] / 100000000
    next_funding_rate = response_data['result']['predFundingRate'] / 100000000

    return DerivativeStatus(
        exchange=PHEMEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_dydx_btc_usd_derivative_status():
    symbol = 'BTC-USD'
    client = ClientDydx()

    response_data = client.get_markets(symbol=symbol)

    funding_time = datetime.strptime(response_data['markets'][symbol]['nextFundingAt'],
                                     '%Y-%m-%dT%H:%M:%S.000Z') + timedelta(hours=9)
    funding_rate = float(response_data['markets'][symbol]['nextFundingRate'])

    return DerivativeStatus(
        exchange=DYDX,
        symbol=symbol,
        last_price=None,
        mark_price=None,
        index_price=None,
        funding_time_dt=funding_time,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=None,
        long_short_ratio=None
    )


def get_deribit_btc_perpetual_derivative_status():
    symbol = 'BTC-PERPETUAL'
    client = ClientDeribit()

    response_data = client.get_book_summary_by_instrument(symbol=symbol)

    last_price = response_data['result'][0]['last']
    mark_price = response_data['result'][0]['mark_price']
    funding_rate = response_data['result'][0]['current_funding']

    # TODO index価格の取得方法が以下で正しいか怪しい
    response_data = client.get_index_price(symbol='btc_usd')
    index_price = response_data['result']['index_price']

    return DerivativeStatus(
        exchange=DERIBIT,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=None,
        long_short_ratio=None
    )


def get_gate_btc_usd_derivative_status():
    symbol = 'BTC_USD'
    client = ClientGate()

    response_data = client.get_futures_tickers(settle='usd', contract=symbol)

    last_price = float(response_data[0]['last'])
    mark_price = float(response_data[0]['mark_price'])
    index_price = float(response_data[0]['index_price'])
    funding_rate = float(response_data[0]['funding_rate'])
    next_funding_rate = float(response_data[0]['funding_rate_indicative'])

    return DerivativeStatus(
        exchange=GATE,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_gate_btc_usdt_derivative_status():
    symbol = 'BTC_USDT'
    client = ClientGate()

    response_data = client.get_futures_tickers(settle='usdt', contract=symbol)

    last_price = float(response_data[0]['last'])
    mark_price = float(response_data[0]['mark_price'])
    index_price = float(response_data[0]['index_price'])
    funding_rate = float(response_data[0]['funding_rate'])
    next_funding_rate = float(response_data[0]['funding_rate_indicative'])

    return DerivativeStatus(
        exchange=GATE,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=round(mark_price, 1),
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_bitget_btc_usd_derivative_status():
    symbol = 'BTCUSD_DMCBL'
    client = ClientBitget()

    response_data = client.get_current_fundrate(symbol=symbol)

    # last_price = float(response_data[0]['last'])
    # mark_price = float(response_data[0]['mark_price'])
    # index_price = float(response_data[0]['index_price'])
    funding_rate = float(response_data['data']['fundingRate'])
    # next_funding_rate = float(response_data[0]['funding_rate_indicative'])

    return DerivativeStatus(
        exchange=BITGET,
        symbol=symbol,
        last_price=None,
        mark_price=None,
        index_price=None,
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=None,
        long_short_ratio=None
    )


def get_bitget_btc_usdt_derivative_status():
    symbol = 'BTCUSDT_UMCBL'
    client = ClientBitget()

    response_data = client.get_current_fundrate(symbol=symbol)

    # last_price = float(response_data[0]['last'])
    # mark_price = float(response_data[0]['mark_price'])
    # index_price = float(response_data[0]['index_price'])
    funding_rate = float(response_data['data']['fundingRate'])
    # next_funding_rate = float(response_data[0]['funding_rate_indicative'])

    return DerivativeStatus(
        exchange=BITGET,
        symbol=symbol,
        last_price=None,
        mark_price=None,
        index_price=None,
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=None,
        long_short_ratio=None
    )


def get_coinex_btc_usd_derivative_status():
    symbol = 'BTCUSD'
    client = ClientCoinex()

    response_data = client.get_ticker(symbol=symbol)

    last_price = float(response_data['data']['ticker']['last'])
    # mark_price = float(response_data[0]['mark_price'])
    index_price = float(response_data['data']['ticker']['index_price'])
    funding_rate = float(response_data['data']['ticker']['funding_rate_next'])
    next_funding_rate = float(response_data['data']['ticker']['funding_rate_predict'])

    return DerivativeStatus(
        exchange=COINEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=None,
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_coinex_btc_usdt_derivative_status():
    symbol = 'BTCUSDT'
    client = ClientCoinex()

    response_data = client.get_ticker(symbol=symbol)

    last_price = float(response_data['data']['ticker']['last'])
    # mark_price = float(response_data[0]['mark_price'])
    index_price = float(response_data['data']['ticker']['index_price'])
    funding_rate = float(response_data['data']['ticker']['funding_rate_next'])
    next_funding_rate = float(response_data['data']['ticker']['funding_rate_predict'])

    return DerivativeStatus(
        exchange=COINEX,
        symbol=symbol,
        last_price=round(last_price, 1),
        mark_price=None,
        index_price=round(index_price, 1),
        funding_time_dt=None,
        funding_rate=funding_rate,
        next_funding_time_dt=None,
        next_funding_rate=next_funding_rate,
        long_short_ratio=None
    )


def get_btc_derivative_statuses():
    funcs = [
        get_ftx_btc_prep_derivative_status,
        get_binance_btc_usd_prep_derivative_status,
        get_binance_btc_usdt_derivative_status,
        get_binance_btc_busd_derivative_status,
        get_bitmex_xbt_usd_derivative_status,
        get_bitmex_xbt_usdt_derivative_status,
        # get_bitmex_xbt_eur_derivative_status,
        get_bybit_btc_usd_derivative_status,
        get_bybit_btc_usdt_derivative_status,
        get_okx_btc_usd_swap_derivative_status,
        get_okx_btc_usdt_swap_derivative_status,
        get_huobi_btc_usd_derivative_status,
        get_huobi_btc_usdt_derivative_status,
        get_bitfinex_tbtcf0_ustf0_derivative_status,
        get_phemex_btc_usd_derivative_status,
        get_dydx_btc_usd_derivative_status,
        get_deribit_btc_perpetual_derivative_status,
        get_bitget_btc_usd_derivative_status,
        get_bitget_btc_usdt_derivative_status,
        get_gate_btc_usd_derivative_status,
        get_gate_btc_usdt_derivative_status,
        get_coinex_btc_usd_derivative_status,
        get_coinex_btc_usdt_derivative_status,
    ]

    derivative_statuses = joblib.Parallel(n_jobs=-1)(joblib.delayed(func)() for func in funcs)

    return [derivative_status.values for derivative_status in derivative_statuses]


if __name__ == '__main__':
    import rich

    rich.print(get_btc_derivative_statuses())
