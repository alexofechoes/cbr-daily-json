import requests
import json
from bs4 import BeautifulSoup


class CBRFetcher():
    def currency_rates(self):
        xml = self._request_cbr_data()
        return self._parse_xml(xml)


    def _request_cbr_data(self):
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        res = requests.get(url)
        return res.text


    def _parse_xml(self, xml_data):
        bs = BeautifulSoup(xml_data, features="lxml")
        currencies = bs.find_all('valute')
        return [{e.name: e.string for e in currency} for currency in currencies]
