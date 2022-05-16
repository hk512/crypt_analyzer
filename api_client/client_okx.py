import requests

BASE_URL = 'https://www.okx.com/api'


class ClientOKX(object):
    def get_ticker(self, symbol):
        url = f'{BASE_URL}/v5/market/ticker'
        params = {
            'instId': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_index_ticker(self, symbol):
        url = f'{BASE_URL}/v5/market/index-tickers'
        params = {
            'instId': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_mark_price(self, symbol, inst_type):
        url = f'{BASE_URL}/v5/public/mark-price'
        params = {
            'instId': symbol,
            'instType': inst_type
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_funding_rate(self, symbol):
        url = f'{BASE_URL}/v5/public/funding-rate'
        params = {
            'instId': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_funding_rate_history(self, symbol):
        url = f'{BASE_URL}/v5/public/funding-rate-history'
        params = {
            'instId': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_long_short_account_ratio(self, symbol, period):
        url = f'{BASE_URL}/v5/rubik/stat/contracts/long-short-account-ratio'
        params = {
            'ccy': symbol,
            'period': period
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientOKX()
    print(client.get_ticker(symbol='BTC-USD-SWAP'))
    print(client.get_index_ticker(symbol='BTC-USD'))
    print(client.get_mark_price(symbol='BTC-USD-SWAP', inst_type='SWAP'))
    print(client.get_funding_rate(symbol='BTC-USD-SWAP'))
    print(client.get_funding_rate_history(symbol='BTC-USD-SWAP'))

    print(client.get_ticker(symbol='BTC-USDT-SWAP'))
    print(client.get_index_ticker(symbol='BTC-USDT'))
    print(client.get_mark_price(symbol='BTC-USDT-SWAP', inst_type='SWAP'))
    print(client.get_funding_rate(symbol='BTC-USDT-SWAP'))
    print(client.get_funding_rate_history(symbol='BTC-USDT-SWAP'))

    print(client.get_long_short_account_ratio(symbol='BTC', period='5m'))
