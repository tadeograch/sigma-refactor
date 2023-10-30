import pytest
from objects import Coin
import yfinance as yf
from symbol_checker import symbol_checker

class TestClass:
    def test_closing_price(self):
        """ Test last closing price """
        coin = Coin("BTC-USD")
        assert coin.last_closing_price() == yf.download(tickers="BTC-USD", period='1d').Close[0]

    def test_open_price(self):
        """ Test last open price """
        coin = Coin("BTC-USD")
        assert coin.last_open_price() == yf.download(tickers="BTC-USD", period='1d').Open[0]
    
    def test_highest_price(self):
        """ Test last highest price """
        coin = Coin("BTC-USD")
        assert coin.last_highest_price() == yf.download(tickers="BTC-USD", period='1d').High[0]

    def test_lowest_price(self):
        """ Test last lowest price """
        coin = Coin("BTC-USD")
        assert coin.last_lowest_price() == yf.download(tickers="BTC-USD", period='1d').Low[0]

    def test_symbol_checker(self):
        """ Test symbol checker function """
        assert symbol_checker("BTC-USD") == True
        assert symbol_checker("ETH-USD") == True
        assert symbol_checker("USDT-USD") == True
        assert symbol_checker("AMZN") == False
        assert symbol_checker("TSLA") == False
        assert symbol_checker("AAPL") == False