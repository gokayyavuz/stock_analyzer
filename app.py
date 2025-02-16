import streamlit as st
from stock import Stock


st.header('Stock Analyzer')

st.subheader('Das ist nur ein Test')
st.write(Stock('PLTR').get_analyst_price_targets())