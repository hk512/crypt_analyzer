import requests

D_API_BASE_URL = 'https://dapi.binance.com'
F_API_BASE_URL = 'https://fapi.binance.com'


class ClientBinance(object):
    def get_d_api_premium_index(self, symbol):
        url = f'{D_API_BASE_URL}/dapi/v1/premiumIndex'
        params = {
            'symbol': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_premium_index(self, symbol):
        url = f'{F_API_BASE_URL}/fapi/v1/premiumIndex'
        params = {
            'symbol': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_ticker_price(self, symbol):
        url = f'{D_API_BASE_URL}/dapi/v1/ticker/price'
        params = {
            'symbol': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_ticker_price(self, symbol):
        url = f'{F_API_BASE_URL}/fapi/v1/ticker/price'
        params = {
            'symbol': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_global_long_short_account_ratio(self, symbol, period, limit=500):
        url = f'{D_API_BASE_URL}/futures/data/globalLongShortAccountRatio'
        params = {
            'pair': symbol,
            'period': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_top_long_short_account_ratio(self, symbol, period, limit=500):
        url = f'{D_API_BASE_URL}/futures/data/topLongShortAccountRatio'
        params = {
            'pair': symbol,
            'period': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_top_long_short_position_ratio(self, symbol, period, limit=500):
        url = f'{D_API_BASE_URL}/futures/data/topLongShortPositionRatio'
        params = {
            'pair': symbol,
            'period': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_global_long_short_account_ratio(self, symbol, period, limit=500):
        url = f'{F_API_BASE_URL}/futures/data/globalLongShortAccountRatio'
        params = {
            'symbol': symbol,
            'period': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_top_long_short_account_ratio(self, symbol, period, limit=500):
        url = f'{F_API_BASE_URL}/futures/data/topLongShortAccountRatio'
        params = {
            'symbol': symbol,
            'period': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_top_long_short_position_ratio(self, symbol, period, limit=500):
        url = f'{F_API_BASE_URL}/futures/data/topLongShortPositionRatio'
        params = {
            'symbol': symbol,
            'period': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_index_price_klines(self, symbol, period, limit=500):
        url = f'{F_API_BASE_URL}/fapi/v1/indexPriceKlines'
        params = {
            'pair': symbol,
            'interval': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_index_price_klines(self, symbol, period, limit=500):
        url = f'{D_API_BASE_URL}/dapi/v1/indexPriceKlines'
        params = {
            'pair': symbol,
            'interval': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_mark_price_klines(self, symbol, period, limit=500):
        url = f'{F_API_BASE_URL}/fapi/v1/markPriceKlines'
        params = {
            'symbol': symbol,
            'interval': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_mark_price_klines(self, symbol, period, limit=500):
        url = f'{D_API_BASE_URL}/dapi/v1/markPriceKlines'
        params = {
            'symbol': symbol,
            'interval': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_klines(self, symbol, period, limit=500):
        url = f'{F_API_BASE_URL}/fapi/v1/klines'
        params = {
            'symbol': symbol,
            'interval': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_klines(self, symbol, period, limit=500):
        url = f'{D_API_BASE_URL}/dapi/v1/klines'
        params = {
            'symbol': symbol,
            'interval': period,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_d_api_funding_rate(self, symbol, limit=1000):
        url = f'{D_API_BASE_URL}/dapi/v1/fundingRate'
        params = {
            'symbol': symbol,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_f_api_funding_rate(self, symbol, limit=1000):
        url = f'{F_API_BASE_URL}/fapi/v1/fundingRate'
        params = {
            'symbol': symbol,
            'limit': limit,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientBinance()
    print(client.get_d_api_premium_index(symbol='BTCUSD_PERP'))
    print(client.get_d_api_ticker_price(symbol='BTCUSD_PERP'))
    print(client.get_d_api_global_long_short_account_ratio(symbol='BTCUSD', period='5m', limit=1))
    print(client.get_d_api_top_long_short_account_ratio(symbol='BTCUSD', period='5m', limit=1))
    print(client.get_d_api_top_long_short_position_ratio(symbol='BTCUSD', period='5m', limit=1))
    print(client.get_d_api_klines(symbol='BTCUSD_PERP', period='15m', limit=500))
    print(client.get_d_api_index_price_klines(symbol='BTCUSD', period='15m', limit=500))
    print(client.get_d_api_mark_price_klines(symbol='BTCUSD_PERP', period='15m', limit=500))
    print(client.get_d_api_funding_rate(symbol='BTCUSD_PERP', limit=1000))

    print(client.get_f_api_premium_index(symbol='BTCUSDT'))
    print(client.get_f_api_ticker_price(symbol='BTCUSDT'))
    print(client.get_f_api_global_long_short_account_ratio(symbol='BTCUSDT', period='5m', limit=1))
    print(client.get_f_api_top_long_short_account_ratio(symbol='BTCUSDT', period='5m', limit=1))
    print(client.get_f_api_top_long_short_position_ratio(symbol='BTCUSDT', period='5m', limit=1))
    print(client.get_f_api_klines(symbol='BTCUSDT', period='15m', limit=500))
    print(client.get_f_api_index_price_klines(symbol='BTCUSDT', period='15m', limit=500))
    print(client.get_f_api_mark_price_klines(symbol='BTCUSDT', period='15m', limit=500))
    print(client.get_f_api_funding_rate(symbol='BTCUSDT', limit=1000))

    print(client.get_f_api_premium_index(symbol='BTCBUSD'))
    print(client.get_f_api_ticker_price(symbol='BTCBUSD'))
    print(client.get_f_api_global_long_short_account_ratio(symbol='BTCBUSD', period='5m', limit=1))
    print(client.get_f_api_top_long_short_account_ratio(symbol='BTCBUSD', period='5m', limit=1))
    print(client.get_f_api_top_long_short_position_ratio(symbol='BTCBUSD', period='5m', limit=1))
    print(client.get_f_api_klines(symbol='BTCBUSD', period='15m', limit=500))
    print(client.get_f_api_index_price_klines(symbol='BTCBUSD', period='15m', limit=500))
    print(client.get_f_api_mark_price_klines(symbol='BTCBUSD', period='15m', limit=500))
    print(client.get_f_api_funding_rate(symbol='BTCBUSD', limit=1000))