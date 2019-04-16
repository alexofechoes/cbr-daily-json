import requests
import json
from bs4 import BeautifulSoup


class CBRFetcher():
    def currency_rates(self):
        xml = self._request_cbr_data()
        return self._parse_xml_to_json(xml)


    def _request_cbr_data(self):
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        res = requests.get(url)
        return res.text


    def _parse_xml_to_json(self, xml_data):
        bs = BeautifulSoup(xml_data, features="lxml")
        valutes = bs.find_all('valute')
        res = [{e.name: e.string for e in valute} for valute in valutes]
        return json.dumps(res)
