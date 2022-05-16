import requests
import time

BASE_URL = 'https://api.bybit.com'


class ClientBybit(object):
    def get_tickers(self, symbol):
        url = f'{BASE_URL}/v2/public/tickers'
        params = {
            'symbol': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_account_ratio(self, symbol, period, limit=500):
        url = f'{BASE_URL}/v2/public/account-ratio'

        params = {
            'symbol': symbol,
            'period': period,
            'limit': limit,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_inverse_kline(self, symbol, interval=15, limit=500):
        url = f'{BASE_URL}/v2/public/kline/list'

        timestamp = int(time.time())
        results = []

        while len(results) < limit:
            params = {
                'symbol': symbol,
                'interval': interval,
                'from': timestamp - 200 * 60 * interval,
                'limit': 200
            }

            response = requests.get(url, params=params)
            response_data = response.json()
            result = response_data['result']

            results += result
            timestamp -= 200 * 60 * interval

        return results[-limit:]

    def get_inverse_mark_price_kline(self, symbol, interval=15, limit=500):
        url = f'{BASE_URL}/v2/public/mark-price-kline'

        timestamp = int(time.time())
        results = []

        while len(results) < limit:
            params = {
                'symbol': symbol,
                'interval': interval,
                'from': timestamp - 200 * 60 * interval,
                'limit': 200
            }

            response = requests.get(url, params=params)
            response_data = response.json()
            result = response_data['result']

            results += result
            timestamp -= 200 * 60 * interval

        return results[-limit:]

    def get_inverse_index_price_kline(self, symbol, interval=15, limit=500):
        url = f'{BASE_URL}/v2/public/index-price-kline'

        timestamp = int(time.time())
        results = []

        while len(results) < limit:
            params = {
                'symbol': symbol,
                'interval': interval,
                'from': timestamp - 200 * 60 * interval,
                'limit': 200
            }

            response = requests.get(url, params=params)
            response_data = response.json()
            result = response_data['result']

            results += result
            timestamp -= 200 * 60 * interval

        return results[-limit:]

    def get_linear_kline(self, symbol, interval=15, limit=500):
        url = f'{BASE_URL}/public/linear/kline'

        timestamp = int(time.time())
        results = []

        while len(results) < limit:
            params = {
                'symbol': symbol,
                'interval': interval,
                'from': timestamp - 200 * 60 * interval,
                'limit': 200
            }

            response = requests.get(url, params=params)
            response_data = response.json()
            result = response_data['result']

            results += result
            timestamp -= 200 * 60 * interval

        return results[-limit:]

    def get_linear_mark_price_kline(self, symbol, interval=15, limit=500):
        url = f'{BASE_URL}/public/linear/mark-price-kline'

        timestamp = int(time.time())
        results = []

        while len(results) < limit:
            params = {
                'symbol': symbol,
                'interval': interval,
                'from': timestamp - 200 * 60 * interval,
                'limit': 200
            }

            response = requests.get(url, params=params)
            response_data = response.json()
            result = response_data['result']

            results += result
            timestamp -= 200 * 60 * interval

        return results[-limit:]

    def get_linear_index_price_kline(self, symbol, interval=15, limit=500):
        url = f'{BASE_URL}/public/linear/index-price-kline'

        timestamp = int(time.time())
        results = []

        while len(results) < limit:
            params = {
                'symbol': symbol,
                'interval': interval,
                'from': timestamp - 200 * 60 * interval,
                'limit': 200
            }

            response = requests.get(url, params=params)
            response_data = response.json()
            result = response_data['result']

            results += result
            timestamp -= 200 * 60 * interval

        return results[-limit:]


if __name__ == '__main__':
    client = ClientBybit()
    # print(client.get_tickers(symbol='BTCUSD'))
    # print(client.get_account_ratio(symbol='BTCUSD', period='5min'))
    # print(client.get_inverse_kline(symbol='BTCUSD', interval=15))
    # print(client.get_inverse_index_price_kline(symbol='BTCUSD', interval=15))
    # print(client.get_inverse_mark_price_kline(symbol='BTCUSD', interval=15))
    #
    # print(client.get_tickers(symbol='BTCUSDT'))
    # print(client.get_account_ratio(symbol='BTCUSDT', period='5min'))
    # print(client.get_linear_kline(symbol='BTCUSDT', interval=15))
    # print(client.get_linear_index_price_kline(symbol='BTCUSDT', interval=15))
    # print(client.get_linear_mark_price_kline(symbol='BTCUSDT', interval=15))

    print(client.get_tickers(symbol='BTCPERP'))
    print(client.get_account_ratio(symbol='BTCPERP', period='5min'))
    print(client.get_linear_kline(symbol='BTCPERP', interval=15))
    print(client.get_linear_index_price_kline(symbol='BTCPERP', interval=15))
    print(client.get_linear_mark_price_kline(symbol='BTCPERP', interval=15))
