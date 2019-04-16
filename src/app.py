from flask import Flask
from .cbr import CBRFetcher


app = Flask(__name__)
cbr_fetcher = CBRFetcher()


@app.route("/")
def get_json_data():
    return cbr_fetcher.currency_rates()
