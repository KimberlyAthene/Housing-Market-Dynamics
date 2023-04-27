import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import json 

def fill_missing_months(df, city, state):
    df_city = df[(df['City'] == city) & (df['State'] == state)]
    df_city['Month'] = df_city['Date'].dt.month
    df_city['Year'] = df_city['Date'].dt.year

    min_year = df_city['Year'].min()
    max_year = df_city['Year'].max()

    filled_records = []
    for year in range(min_year, max_year + 1):
        year_records = df_city[df_city['Year'] == year]
        average_price = year_records['Price'].mean()
        
        for month in range(1, 13):
            record = year_records[year_records['Month'] == month]
            if record.empty:
                filled_date = pd.Timestamp(year, month, 1)
                filled_records.append({'City': city, 'State': state, 'Date': filled_date, 'Price': average_price})

    filled_df = df_city.append(filled_records, ignore_index=True)
    filled_df.sort_values(by='Date', inplace=True)

    return filled_df

def predict_house_price(city, state):

    # Load Data and format Date column
    df = pd.read_csv('house_price_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    pd.options.display.float_format = "{:.2f}".format

    filled_df = fill_missing_months(df, city, state)

    # Convert the 'Date' column to a DatetimeIndex
    filled_df.index = pd.to_datetime(filled_df['Date'], format='%Y-%m-%d')

    # Drop the 'Date' column and resample the filtered dataframe to monthly frequency
    df_monthly = filled_df.drop('Date', axis=1).resample('MS').mean()

    # Define the SARIMA model parameters
    order = (1, 1, 1)
    seasonal_order = (0, 0, 0, 12)

    # Fit the SARIMA model to the resampled dataframe
    model = SARIMAX(df_monthly['Price'], order=order, seasonal_order=seasonal_order)
    results = model.fit()

    # Get the forecasted values for the next 12 months
    forecast = results.get_forecast(steps=12)
    forecast_df = forecast.predicted_mean.to_frame(name='Price')

    # Concatenate the filtered and forecasted dataframes
    combined_df = pd.concat([df_monthly, forecast_df])

    # Create a list of tuples containing the year, month, and predicted price for each of the 12 forecasted months
    forecast_tuples = [(str(date.year), str(date.month), price) for date, price in zip(combined_df.index, combined_df['Price'])]

    return json.dumps(forecast_tuples)

