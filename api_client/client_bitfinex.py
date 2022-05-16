import requests

BASE_URL = 'https://api-pub.bitfinex.com'


class ClientBitfinex(object):
    def get_deriv_status(self, symbol):
        url = f'{BASE_URL}/v2/status/deriv'
        params = {
            'keys': symbol,
        }
        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientBitfinex()
    print(client.get_deriv_status(symbol='tBTCF0:USTF0'))
