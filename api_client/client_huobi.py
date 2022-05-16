import requests

BASE_URL = 'https://api.hbdm.com'


class ClientHuobi(object):
    def get_swap_funding_rate(self, symbol):
        url = f'{BASE_URL}/swap-api/v1/swap_funding_rate'
        params = {
            'contract_code': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_swap_historical_funding_rate(self, symbol, page_index):
        url = f'{BASE_URL}/swap-api/v1/swap_historical_funding_rate'
        params = {
            'contract_code': symbol,
            'page_index	': page_index,
            'page_size': 50
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_linear_swap_funding_rate(self, symbol):
        url = f'{BASE_URL}/linear-swap-api/v1/swap_funding_rate'
        params = {
            'contract_code': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_linear_swap_historical_funding_rate(self, symbol, page_index):
        url = f'{BASE_URL}/linear-swap-api/v1/swap_historical_funding_rate'
        params = {
            'contract_code': symbol,
            'page_index	': page_index,
            'page_size': 50
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientHuobi()
    print(client.get_swap_funding_rate(symbol='BTC-USD'))
    print(client.get_swap_historical_funding_rate(symbol='BTC-USD'))
    print(client.get_linear_swap_funding_rate(symbol='BTC-USDT'))
    print(client.get_linear_swap_historical_funding_rate(symbol='BTC-USDT'))
