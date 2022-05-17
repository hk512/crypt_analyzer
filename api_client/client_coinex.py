import requests

BASE_URL = 'https://api.coinex.com'


class ClientCoinex(object):
    def get_ticker(self, symbol):
        url = f'{BASE_URL}/perpetual/v1/market/ticker'

        params = {
            'market': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_funding_history(self, symbol):
        url = f'{BASE_URL}/perpetual/v1/market/funding_history'

        params = {
            'market': symbol,
            'offset': 0,
            'limit': 500,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientCoinex()
    print(client.get_ticker(symbol='BTCUSDT'))
    print(client.get_funding_history(symbol='BTCUSDT'))
    print(client.get_ticker(symbol='BTCUSD'))
    print(client.get_funding_history(symbol='BTCUSD'))

    # import pandas as pd
    # from datetime import datetime
    # data = pd.DataFrame(client.get_funding_history(symbol='BTCUSD')['data']['records'])
    # data['time'] = data['time'].astype(int).apply(datetime.fromtimestamp)
    # print(data)
