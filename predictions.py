#!/usr/bin/python3
"""
File containing the prediction function
"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, GRU
from sklearn.preprocessing import MinMaxScaler

from datetime import datetime, timedelta


def predict(ticker):
    # Define the cryptocurrency symbol and time frame (e.g., BTC-USD for Bitcoin)
    crypto_symbol = ticker
    start_date = "2015-01-01"
    end_date = datetime.now().strftime("%Y-%m-%d")

    # Fetch historical cryptocurrency price data using yfinance
    crypto_data = yf.download(crypto_symbol, start=start_date, end=end_date)

    # Ensure the DataFrame has 'Date' and 'Close' columns
    crypto_data = crypto_data[['Close']].reset_index()

    # Use the 'Close' prices as the target variable 'y'
    y_target = crypto_data['Close'].values.reshape(-1, 1)

    # Normalize the data using Min-Max scaling
    scaler = MinMaxScaler()
    y_scaled = scaler.fit_transform(y_target)

    # Create sequences for time series data
    sequence_length = len(y_scaled) - 5  # You can adjust this value based on your data
    X = []
    y = []
    for i in range(sequence_length, len(y_scaled)):
        X.append(y_scaled[i - sequence_length:i, 0])
        y.append(y_scaled[i, 0])
    X, y = np.array(X), np.array(y)

    # Split the data into training and testing sets
    split_ratio = 0.8
    split_index = int(len(X) * split_ratio)
    X_train, X_test, y_train, y_test = X[:split_index], X[split_index:], y[:split_index], y[split_index:]

    # Build a Sequential model
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(sequence_length,)))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

    # Predict future cryptocurrency prices
    num_days_to_predict = 360  # Change this to predict a different number of days into the future

    # Use the last sequence_length days of data to predict the future
    last_sequence = X[-1]

    future_predictions = []

    for _ in range(num_days_to_predict):
        prediction = model.predict(last_sequence.reshape(1, -1))[0, 0]
        future_predictions.append(prediction)
        last_sequence = np.roll(last_sequence, shift=-1)
        last_sequence[-1] = prediction

    # Inverse transform the scaled predictions to the original scale
    future_predictions_original = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

    # Create date range for future predictions
    last_date = crypto_data['Date'].values[-1]
    future_dates = pd.date_range(start=last_date, periods=num_days_to_predict + 1, inclusive='right')

    # Visualize the future price predictions
    plt.figure(figsize=(12, 6))
    plt.plot(crypto_data['Date'][-360:], crypto_data['Close'][-360:], label='Historical Prices', color='blue')
    plt.plot(future_dates, future_predictions_original, label='Predicted Prices', color='green')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.title(f'{crypto_symbol} Future Price Prediction')
    plt.show()