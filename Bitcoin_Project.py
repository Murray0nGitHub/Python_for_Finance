import yfinance as yf
data = yf.Ticker("BTC-USD")

print(data.info['description'])

