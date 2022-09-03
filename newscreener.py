import yfinance as yf
import pandas as pd

# k=yf.Ticker("AAPL").info <-- To get all the info about a single company

# we are using dow johns as example
df = pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')[1]
tickers = df.Symbol.to_list()

infos = []

for i in tickers:
    infos.append(yf.Ticker(i).info)

# these are the parameters.
fundamentals = ['pegRatio', 'earningsQuarterlyGrowth', 'trailingPE', 'forwardPE']

df2 = pd.DataFrame(infos)
df2 = df2.set_index('symbol')

# this prints the whole dow johns list.
dow_list = df2[df2.columns[df2.columns.isin(fundamentals)]]

print(dow_list)

print('\n'*3)

# TO FIND THE BEST 3 STOCKS FROM THE WHOLE LIST ON THE BASIS OF pegRatio(we can change it to anything).
best = df2['pegRatio'].nlargest(3)
print(best)
