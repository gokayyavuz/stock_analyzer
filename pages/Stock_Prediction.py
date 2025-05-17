import streamlit as st
from model import Prediction
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Stock Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title('Stock Prediction')

ticker_input = st.text_input("Please enter your Stock to predict: ")

if ticker_input:
    
    st.subheader('Prediction with Linear Regression')
    pp = Prediction(ticker_input)
    pp.train_linear_model()
    tomorrow = datetime.today() + timedelta(days=1)
    pp.predict_linear(tomorrow)
    pp.plot_linear_forecast()

    st.subheader('Prediction with Prophet')
    pp.train_prophet()
    pp.plot_prophet_forecast()