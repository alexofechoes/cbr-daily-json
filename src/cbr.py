import requests
import json
from bs4 import BeautifulSoup


class CBRFetcher():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def currency_rates(self):
        xml = self._request_cbr_data()
        currencies = self._parse_xml(xml)
        return [self._mapping_currency(currency) for currency in currencies]


    def _mapping_currency(self, currency):
        return {
            'code': currency['charcode'],
            'name': currency['name'],
            'rate': self._calculate_rate(currency)
        }


    def _calculate_rate(self, currency):
        value = float(currency['value'].replace(',', '.'))
        nominal = float(currency['nominal'])
        return value / nominal


    def _request_cbr_data(self):
        res = requests.get(self.url)
        return res.text


    def _parse_xml(self, xml_data):
        bs = BeautifulSoup(xml_data, features="lxml")
        currencies = bs.find_all('valute')
        return [{e.name: e.string for e in currency} for currency in currencies]
