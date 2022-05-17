import requests

BASE_URL = 'https://api.gateio.ws/api/v4'


#
class ClientGate(object):
    def get_futures_tickers(self, settle, contract):
        url = f'{BASE_URL}/futures/{settle}/tickers'

        params = {
            'contract': contract,
        }

        response = requests.get(url, params=params)
        response_data = response.json()

        return response_data


if __name__ == '__main__':
    client = ClientGate()
    print(client.get_futures_tickers(settle='usdt', contract='BTC_USDT'))
    print(client.get_futures_tickers(settle='usd', contract='BTC_USD'))
