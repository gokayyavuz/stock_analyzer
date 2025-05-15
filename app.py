import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

st.title("Stock Analyzer")

ticker_input = st.text_input("Please enter your Stock:")

period_options = {
    "1 month": "1mo",
    "3 months": "3mo",
    "6 months": "6mo",
    "1 year": "1y",
    "3 years": "3y",
    "5 years": "5y",
}

label_to_code = {label: code for label, code in period_options.items()}
selected_label = st.selectbox("Period", options=list(period_options.keys()), index=3)
selected_code = label_to_code[selected_label]

if ticker_input:
    stock_data = yf.download(ticker_input, period=selected_code)

    if not stock_data.empty:
        st.subheader(f"{ticker_input} – Chart for {selected_code}")
        st.line_chart(stock_data['Close'])
    else:
        st.warning("No data available.")

st.divider()

st.title("Portfolio simulation")
st.caption("Simulate the performance of your past stock investment based on historical price data.")
portfolio_data = {
    "symbol": None,
    "date": datetime.today().date(),
    "amount": 0,
}

with st.form(key="portfolio_form"):
    portfolio_data["symbol"] = st.text_input("Please enter your stock:")
    portfolio_data["date"] = st.date_input("Please enter your purchase date:")
    portfolio_data["amount"] = st.number_input("Please enter the value of the purchase:")
    st.form_submit_button()

    if portfolio_data["symbol"] and portfolio_data["date"] < datetime.today().date():
        historical_data = yf.Ticker(portfolio_data["symbol"]).history(
            start=portfolio_data["date"],
            end=datetime.today().date()
        )

        print(historical_data.head())

        entry_price = historical_data['Close'].iloc[0]
        current_price = historical_data['Close'].iloc[-1]

        shares = portfolio_data["amount"] / entry_price
        portfolio_value = shares * current_price
        portfolio_profit = portfolio_value - portfolio_data["amount"]

if all(portfolio_data.values()):
    st.subheader("Chart since purchase")
    st.line_chart(historical_data['Close'])

    st.write("Price at purchase:", round(entry_price, 2))
    st.write("Current price:", round(current_price, 2))
    st.write("Shares bought:", round(shares, 2))
    st.write("Current value:", round(portfolio_value, 2))
    st.write("Profit:", round(portfolio_profit, 2))
