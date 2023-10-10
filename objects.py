#!/usr/bin/python3
"""
File containing the Coin class
"""

import yfinance as yf
from predictions import predict

class Coin:
    """ Class Coin """
    def __init__(self, ticker):
        """ Init function """
        self.ticker = ticker
        self.data = yf.download(tickers=ticker, period='1d')

    def last_closing_price(self):
        """Returns last closing price"""
        return self.data.Close[0]
    
    def last_open_price(self):
        """Returns last open price"""
        return self.data.Open[0]
    
    def last_highest_price(self):
        """Returns todays highest price"""
        return self.data.High[0]
    
    def last_lowest_price(self):
        """Returns todays lowest price"""
        return self.data.Low[0]
    
    def get_prediction(self):
        """Returns price prediction"""
        return predict(self.ticker)



