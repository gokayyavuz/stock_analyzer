import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from prophet import Prophet
import streamlit as st

class Prediction:
    def __init__(self, ticker: str, start_date: str = '2022-01-01'):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = datetime.today().strftime('%Y-%m-%d')
        self.data = self.load_data()
        self.model_lr = None
        self.prophet_model = None
        self.forecast = None

    def load_data(self):
        data = yf.download(tickers=self.ticker, start=self.start_date, end=self.end_date)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        return data

    def train_linear_model(self):
        self.data['DateOrdinal'] = pd.to_datetime(self.data.index).map(pd.Timestamp.toordinal)
        X = self.data[['DateOrdinal']]
        y = self.data['Close']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)
        self.model_lr = LinearRegression()
        self.model_lr.fit(X_train, y_train)

        y_pred = self.model_lr.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"{self.ticker} MSE (Linear Regression): {mse:.2f}")

    def predict_linear(self, future_date: datetime):
        date_ordinal = pd.to_datetime(future_date).toordinal()
        pred = self.model_lr.predict([[date_ordinal]])
        print(f"[{self.ticker}] Prognose am {future_date.date()}: {float(pred[0]):.2f} USD")
        return pred[0]

    def plot_linear_forecast(self, days: int = 180):
        last_date = self.data.index[-1]
        future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days, freq='D')
        future_ordinals = future_dates.map(pd.Timestamp.toordinal).to_frame(name='DateOrdinal')
        future_preds = self.model_lr.predict(future_ordinals).ravel()
        future_df = pd.DataFrame({'Date': future_dates, 'Predicted Close': future_preds})

        fig, ax = plt.subplots(figsize=(14, 7))
        ax.plot(self.data.index, self.data['Close'], label='Real Chart')
        ax.plot(future_df['Date'], future_df['Predicted Close'], label='Linear Prediction', linestyle='--')
        ax.set_title(f'{self.ticker.upper()} Prediction (Linear Regression)')
        ax.set_xlabel('Date')
        ax.set_ylabel('in USD')
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    def train_prophet(self):
        df = self.data.copy()

        if 'Date' not in df.columns:
            df = df.reset_index()

        if 'Date' not in df.columns or 'Close' not in df.columns:
            raise KeyError("Column 'Date' and/or 'Close' are missing.")

        df = df[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})

        if 'ds' not in df.columns or 'y' not in df.columns:
            raise KeyError("Column 'ds' and/or 'y' are missing after renaming.")

        df = df.dropna(subset=['ds', 'y'])

        self.prophet_model = Prophet(daily_seasonality=True)
        self.prophet_model.fit(df)



    def plot_prophet_forecast(self, days: int = 180):
        future = self.prophet_model.make_future_dataframe(periods=days)
        self.forecast = self.prophet_model.predict(future)
        fig = self.prophet_model.plot(self.forecast)
        fig.suptitle(f'Prediction for {self.ticker.upper()} (Prophet)', fontsize=14)
        
        st.pyplot(fig)

