from flask import Flask, request, jsonify
import pandas as pd
from data_fetch import download_historical_data
from flask_cors import CORS
from nifty_data import nifty_data
from trading import strategy_build
app = Flask(__name__)
CORS(app)



@app.route('/', methods=['POST' , 'GET'])
def login():
    return " this is login page"




@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    data = request.json

    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Download historical data
    df = download_historical_data(symbol, start_date, end_date)
    
    result = df.to_dict(orient='records')

    return jsonify(result)


@app.route('/nifty_stock', methods=['POST'])
def get_stock():
    data = request.json
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # nifty 50 data 
    df = nifty_data(start_date, end_date)
    
    result = df.to_dict(orient='records')

    return jsonify(result)


# @app.route('/arbritage', methods=['POST'])
# def arbritage():
#     data = request.json

#     symbol = data.get('symbol')
#     start_date = data.get('start_date')
#     end_date = data.get('end_date')

#     # Download historical data
#     df, df2 = arbitrage_fetcher(symbol, start_date, end_date)
    
#     result = {
#         'symbol_data': df.to_dict(orient='records'),
#         'symbol_bo_data': df2.to_dict(orient='record')
#     }

#     return jsonify(result)


@app.route('/stock_trend', methods=['POST'])
def stock_trend():
    data = request.json
    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # nifty 50 data 
    df = strategy_build(symbol, start_date, end_date)
    
    result = df.to_dict(orient='records')

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)




