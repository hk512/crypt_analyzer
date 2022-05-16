import requests

BASE_URL = 'https://api.dydx.exchange'


class ClientDydx(object):
    def get_markets(self, symbol):
        url = f'{BASE_URL}/v3/markets'
        params = {
            'market': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientDydx()
    print(client.get_markets(symbol='BTC-USD'))
