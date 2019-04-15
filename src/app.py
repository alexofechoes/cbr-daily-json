from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def get_json_data():
    return utils.get_valutes()