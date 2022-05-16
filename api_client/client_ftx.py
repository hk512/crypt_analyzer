import requests

BASE_URL = 'https://ftx.com/api'


class ClientFTX(object):
    def get_future(self, symbol):
        url = f'{BASE_URL}/futures/{symbol}'
        response = requests.get(url)
        response_data = response.json()

        return response_data

    def get_future_stats(self, symbol):
        url = f'{BASE_URL}/futures/{symbol}/stats'
        response = requests.get(url)
        response_data = response.json()

        return response_data

    def get_funding_rates(self, symbol):
        url = f'{BASE_URL}/funding_rates'

        params = {
            'future': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientFTX()
    print(client.get_future(symbol='BTC-PERP'))
    print(client.get_future_stats(symbol='BTC-PERP'))
    print(client.get_funding_rates(symbol='BTC-PERP'))
