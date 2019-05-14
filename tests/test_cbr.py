import requests_mock
from src.cbr import CBRFetcher


def test_cbr_fetcher():
    with requests_mock.Mocker() as m:
        m.get(CBRFetcher.url, text=_get_xml_response())
        cbr_fetcher = CBRFetcher()
        currency_rates = cbr_fetcher.currency_rates()

    expected = {
        "AUD": {
            "code": "AUD", 
            "name": "Австралийский доллар",
            "rate": 45.8946
        },
        "AZN": {
            "code": "AZN", 
            "name": "Азербайджанский манат",
            "rate": 37.8675
        },
        "GBP": {
            "code": "GBP",
            "name": "Фунт стерлингов Соединенного королевства",
            "rate": 84.0738,
        },
    }
    assert expected == currency_rates


def _get_xml_response():
    return """
    <ValCurs Date="17.04.2019" name="Foreign Currency Market">
        <Valute ID="R01010">
            <NumCode>036</NumCode>
            <CharCode>AUD</CharCode>
            <Nominal>1</Nominal>
            <Name>Австралийский доллар</Name>
            <Value>45,8946</Value>
            </Valute>
            <Valute ID="R01020A">
            <NumCode>944</NumCode>
            <CharCode>AZN</CharCode>
            <Nominal>1</Nominal>
            <Name>Азербайджанский манат</Name>
            <Value>37,8675</Value>
            </Valute>
            <Valute ID="R01035">
            <NumCode>826</NumCode>
            <CharCode>GBP</CharCode>
            <Nominal>1</Nominal>
            <Name>Фунт стерлингов Соединенного королевства</Name>
            <Value>84,0738</Value>
        </Valute>
    </ValCurs>"""
