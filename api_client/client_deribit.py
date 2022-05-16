import requests

BASE_URL = 'https://deribit.com/api'


class ClientDeribit(object):
    def get_book_summary_by_instrument(self, symbol):
        url = f'{BASE_URL}/v2/public/get_book_summary_by_instrument'
        params = {
            'instrument_name': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data

    def get_index_price(self, symbol):
        url = f'{BASE_URL}/v2/public/get_index_price'
        params = {
            'index_name': symbol,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientDeribit()
    print(client.get_book_summary_by_instrument(symbol='BTC-PERPETUAL'))
    print(client.get_index_price(symbol='btc_usd'))
