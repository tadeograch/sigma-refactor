#!/usr/bin/python3
"""
Main file
"""

from objects import Coin
from predictions import predict


def main():
    """ Main function """
    symbol = "RIVN"
    ticker = Coin(symbol)
    print("Last closing price: {}".format(ticker.last_closing_price()))
    print("Last open price: {}".format(ticker.last_open_price()))
    print("Last highest price: {}".format(ticker.last_highest_price()))
    print("Last lowest price: {}".format(ticker.last_lowest_price()))

    ticker.get_prediction()

    

if __name__ == "__main__":
    main()
