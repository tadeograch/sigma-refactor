#!/usr/bin/python3
"""
File containing functions to analize the predicted data
"""

def max_price(data, time):
    """
    Function to calculate the maximum price of a cryptocurrency
    """
    if len(data) == 0 or len(time) == 0:
        raise ValueError("Values must not be empty")
    max_price = 0
    for i in range(len(data)):
        if data[i] > max_price:
            max_price = data[i]
            date = time[i]
    return max_price, date

def min_price(data, time):
    """
    Function to calculate the minimum price of a cryptocurrency
    """
    if len(data) == 0 or len(time) == 0:
        raise ValueError("Values must not be empty")
    min_price = data[0]
    for i in range(len(data)):
        if data[i] < min_price:
            min_price = data[i]
            date = time[i]
    return min_price, date

def avg_price(data):
    """
    Function to calculate the average price of a cryptocurrency
    """
    if len(data) == 0:
        raise ValueError("Values must not be empty")
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    avg_price = sum / len(data)
    return avg_price

