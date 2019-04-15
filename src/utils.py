import requests
import json
from bs4 import BeautifulSoup


def get_valutes():
    xml = request_cbr_data()
    return parse_xml_to_json(xml)


def request_cbr_data():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = requests.get(url)
    return res.text


def parse_xml_to_json(xml_data):
    bs = BeautifulSoup(xml_data, features="lxml")
    valutes = bs.find_all('valute')
    res = [{e.name: e.string for e in valute} for valute in valutes]
    
    return json.dumps(res)
