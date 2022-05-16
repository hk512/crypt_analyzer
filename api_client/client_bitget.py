import requests

BASE_URL = 'https://api.bitget.com'


class ClientBitget(object):
    def get_current_fundrate(self, symbol):
        url = f'{BASE_URL}/api/mix/v1/market/current-fundRate'

        params = {
            'symbol': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientBitget()
    print(client.get_current_fundrate(symbol='BTCUSD_DMCBL'))
    print(client.get_current_fundrate(symbol='BTCUSDT_UMCBL'))
