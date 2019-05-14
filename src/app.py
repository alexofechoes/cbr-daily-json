from flask import Flask, jsonify
from flask_caching import Cache
from .cbr import CBRFetcher


app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)
cbr_fetcher = CBRFetcher()
CACHE_TIME = 60 * 5


@app.route("/")
@cache.cached(timeout=CACHE_TIME)
def get_json_data():
    currency_rates = cbr_fetcher.currency_rates()
    return jsonify(currency_rates)
