import streamlit as st
from datetime import datetime
import yfinance as yf

st.set_page_config(
    page_title="Portfolio simulation",
    page_icon="💼",
    layout="wide"
)

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
