import streamlit as st

st.set_page_config(
    page_title="Stock Analyzer",
    page_icon="📈",
    layout="wide"
)

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
