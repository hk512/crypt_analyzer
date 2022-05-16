from argparse import ArgumentParser
from datetime import datetime

from flask import Flask
from flask import jsonify
from flask import render_template
import numpy as np
import pandas as pd

from api_client.client_binance import ClientBinance
from get_derivatives_status import get_btc_derivative_statuses
from get_long_short_ratio import get_btc_long_short_ratio
from get_kairi import get_btc_index_price_kairi
from get_kairi import get_btc_mark_price_kairi
from get_funding_rate_history import get_btc_funding_rate_history
from const import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html'), 200


@app.route('/derivative_statuses', methods=['GET'])
def get_derivative_statuses():
    return jsonify(get_btc_derivative_statuses()), 200


@app.route('/derivative_statuses_table', methods=['GET'])
def get_derivative_statuses_table():
    data = get_btc_derivative_statuses()
    return render_template('derivative_statuses_table.html', data=data), 200


@app.route('/get_price', methods=['GET'])
def get_price():
    client = ClientBinance()
    symbol = 'BTCUSDT'
    period = '15m'
    response_data = client.get_f_api_klines(symbol=symbol, period=period, limit=500)

    columns = [
        'Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
        'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore.'
    ]

    data = pd.DataFrame(response_data, columns=columns)
    data['Close'] = round(data['Close'].astype(float), 1)

    return jsonify({
        'labels': [datetime.fromtimestamp(value/1000).strftime(TIME_FORMAT) for value in data['Open time'].values],
        'datasets': [{
            'label': f'{BINANCE}_{symbol}',
            'data': data['Close'].to_list(),
            'borderColor': 'red',
            'borderWidth': 1,
            'pointRadius': 0,
            'spanGaps': True
        }]
    }), 200


@app.route('/long_short_ratio', methods=['GET'])
def get_account_status():
    return jsonify(get_btc_long_short_ratio()), 200


@app.route('/index_price_kairi', methods=['GET'])
def get_index_price_kairi():
    return jsonify(get_btc_index_price_kairi()), 200


@app.route('/mark_price_kairi', methods=['GET'])
def get_mark_price_kairi():
    return jsonify(get_btc_mark_price_kairi()), 200


@app.route('/funding_rate_history', methods=['GET'])
def get_funding_rate_history():
    data = get_btc_funding_rate_history()

    data = data.iloc[-126:, :]

    datasets = []

    for column in data.columns:
        data[column] = round(data[column].astype(float) * 100, 4)
        data[column] = data[column].fillna(method='bfill')
        data[column] = data[column].replace([np.nan], [None])
        datasets.append({
            'label': column,
            'data': data[column].to_list(),
            'borderColor': FUNDING_RATE_COLOR_TABLE[column],
            'borderWidth': 1,
            'pointRadius': 0,
            'spanGaps': True

        })

    return jsonify({
        'labels': [value[5:] for value in data.index],
        'datasets': datasets
    }), 200


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.config['port'] = port

    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
