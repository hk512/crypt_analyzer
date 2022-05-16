import requests

BASE_URL = 'https://api.phemex.com'


class ClientPhemex(object):
    def get_ticker(self, symbol):
        url = f'{BASE_URL}/md/ticker/24hr'
        params = {
            'symbol': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientPhemex()
    print(client.get_ticker(symbol='BTCUSD'))
