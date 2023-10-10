#!/usr/bin/python3
"""
Main file
"""

from objects import Coin
from predictions import predict
from analytics import max_price, min_price, avg_price


def main():
    """ Main function """
    symbol = "RIVN"
    ticker = Coin(symbol)
    print("Last closing price: {}".format(ticker.last_closing_price()))
    print("Last open price: {}".format(ticker.last_open_price()))
    print("Last highest price: {}".format(ticker.last_highest_price()))
    print("Last lowest price: {}".format(ticker.last_lowest_price()))

    data,time = ticker.get_prediction()
    max_p, max_t = max_price(data, time)
    min_p, min_t = min_price(data, time)

    print("Max price: {} at {}".format(max_p, max_t))
    print("Min price: {} at {}".format(min_p, min_t))
    print("Avg price: {}".format(avg_price(data)))

if __name__ == "__main__":
    main()
