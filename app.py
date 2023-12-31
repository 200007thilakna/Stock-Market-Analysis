# -*- coding: utf-8 -*-
"""myApp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LB8iUySmCEPGocucDR4SqTq75VEvmr-C
"""

# pip install streamlit

# pip install yfinance

import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu
from statsmodels.tsa.seasonal import seasonal_decompose


st.set_page_config(layout='wide')
# Header of the web 
st.title("Stock Market Overview")
st.write("""
    ## Welcome, Thilakna!

   Here is an overview of your stocks!
    """
)

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    return data

# Select the security

tickerSymbol = st.selectbox('Select Stock ',['AAPL','TSLA'])
# st.sidebar.header("Hello")


tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2005-5-31', end='2023-5-31', auto_adjust=False)
tickerDf.reset_index(inplace=True)
tickerDf = tickerDf.reset_index()
tickerDf['Date'] = pd.to_datetime(tickerDf['Date'])

# Create a Streamlit app
st.title("Open stock price across months")

# Get the column names
column_names = tickerDf.columns

# Now, 'column_names' contains a list of the column names in your DataFrame 'df'
print(column_names)
print(tickerDf.head())

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# Create a Streamlit app
st.title("Seasonal Decomposition")

# Add the DataFrame to your Streamlit app
st.dataframe(tickerDf)
# Perform seasonal decomposition with specified period
result = seasonal_decompose(tickerDf['Open'], model='multiplicative', period=365)

# Create and display the seasonal decomposition plots
st.subheader("Original Time Series")
st.line_chart(tickerDf['Open'])

st.subheader("Trend Component")
st.line_chart(result.trend)

st.subheader("Seasonal Component")
st.line_chart(result.seasonal)

st.subheader("Residual Component")
st.line_chart(result.resid)

