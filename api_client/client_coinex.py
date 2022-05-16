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


if __name__ == '__main__':
    client = ClientCoinex()
    print(client.get_ticker(symbol='BTCUSDT'))
    print(client.get_ticker(symbol='BTCUSD'))
