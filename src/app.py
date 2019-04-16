from flask import Flask, jsonify
from .cbr import CBRFetcher


app = Flask(__name__)
cbr_fetcher = CBRFetcher()


@app.route("/")
def get_json_data():
    currency_rates = cbr_fetcher.currency_rates()
    return jsonify(currency_rates)
