import yfinance
import pandas as pd

class Stock:
    
    def __init__(self, ticker):
        self.ticker = yfinance.Ticker(ticker=ticker)


    def get_analyst_price_targets(self):
        analyst_price_targets = self.ticker.analyst_price_targets
        current = analyst_price_targets['current']
        high = analyst_price_targets['high']
        low = analyst_price_targets['low']
        mean = analyst_price_targets['mean']
        median = analyst_price_targets['median']

        return print(high)

    def get_history(self, period):
        history = self.ticker.history(period=period).reset_index()
        return print(history)

    def get_year_high(self):
        pass

    def get_year_low(self):
        pass

    def get_financials(self):
        pass

    def get_earnings(self):
        pass

    def get_news(self):
        news = self.ticker.news
        titles = []
        for report in news:
            titles.append(report['content']['title'])
        return print(titles)

    def get_news_summary(self):
        pass
    



s1 = Stock('PLTR')
s1.get_analyst_price_targets()#
s1.get_history('1y')
s1.get_news()