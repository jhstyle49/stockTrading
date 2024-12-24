import yfinance as yf

result=yf.download('AAPL',start = '2024-09-01')
print(result)