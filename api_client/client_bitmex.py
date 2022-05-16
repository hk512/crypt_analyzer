import requests

BASE_URL = 'https://www.bitmex.com/api'


class ClientBitMEX(object):
    def get_instrument(self, symbol):
        url = f'{BASE_URL}/v1/instrument'
        params = {
            'symbol': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_funding(self, symbol):
        url = f'{BASE_URL}/v1/funding'
        params = {
            'symbol': symbol,
            # Maximum count
            'count': 500,
            'reverse': True
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientBitMEX()
    print(client.get_instrument(symbol='XBTUSD'))
    print(client.get_instrument(symbol='XBTUSDT'))
    print(client.get_instrument(symbol='XBTEUR'))
    print(client.get_funding(symbol='XBTUSD'))
    print(client.get_funding(symbol='XBTUSDT'))
