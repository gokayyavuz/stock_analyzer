# 📈 Stock Analyzer & Portfolio Simulator

A simple Streamlit-based web app that allows you to analyze historical stock prices and simulate the performance of past investments.

## 🚀 Features

### 🔍 Stock Analyzer
- Enter any stock ticker (e.g. `AAPL`, `GOOGL`, `TSLA`)
- Choose from various time periods (1 month to 5 years)
- Automatically fetches historical closing prices from Yahoo Finance
- Displays price trend as an interactive line chart

### 💼 Portfolio Simulation
- Simulate a past investment by entering a stock, purchase date, and amount
- Calculates number of shares bought, current value, and profit/loss
- Visualizes the stock’s performance since the purchase date

### 🔮 Stock Prediction
- Use Facebook Prophet to forecast future price trends
- Display predictive time series with trend and confidence intervals

## 🔮 Planned Features

### 📊 Stock Analyzer
- Integration of analyst ratings and opinions
- Compare multiple stocks in the same chart
- Display of key financial KPIs (P/E ratio, dividend yield, etc.)

### 💼 Portfolio Simulation
- Build a full portfolio by adding multiple positions
- Track and visualize the overall portfolio development over time

## 🧩 Built With

- [Streamlit](https://streamlit.io/) – UI framework
- [yfinance](https://ranaroussi.github.io/yfinance/) – Stock data
- [pandas](https://pandas.pydata.org/) – Data handling
- [prophet](https://facebook.github.io/prophet/) - Time series forecasting
