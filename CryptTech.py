import numpy
import talib
import pandas as pd
import numpy as np

# params
winnig_border = 0.02


'''
Basic Setup
'''
stock_DF = pd.read_csv("C:\\Users\\Tim\\Documents\\CrypTech\\res\\" + "GOOG.csv")
stock_DF["AVG_Price"] = (stock_DF["Open"] + stock_DF["Close"])/2

#stock_DF["AVG_Price_Offset_10"] = stock_DF["AVG_Price"]
#stock_DF.AVG_Price_Offset_10 = stock_DF.AVG_Price_Offset_10.shift(10)

'''
Creating Features
'''

# RSI
# TODO  Time-Period is chosen to be 14 without any particular reason yet. It is the default value
stock_DF["RSI"] = talib.RSI(stock_DF["Close"], timeperiod=14)

# MACD
stock_DF["MACD"], stock_DF["MACD_Signal"], macdhist = talib.MACD(stock_DF["Close"], fastperiod=12, slowperiod=26, signalperiod=9)
print(macdhist)

'''
Winning Criteria
'''

'''
Normalize OHCL Data

stock_DF["Open"] = stock_DF["Open"]/stock_DF["High"]
stock_DF["Low"] = stock_DF["Low"]/stock_DF["High"]
stock_DF["Close"] = stock_DF["Close"]/stock_DF["High"]
stock_DF["High"] = stock_DF["High"]/stock_DF["High"]
'''

stock_DF["Winning_Percent_10Days"] = (stock_DF["AVG_Price"].pct_change(periods=-10))*-1
stock_DF["Winning"] = np.where(stock_DF["Winning_Percent_10Days"] > winnig_border, "TRUE", "FALSE")

print(stock_DF.head())
stock_DF.to_csv("google.csv", index=False)

#atr = talib.ATR(df["High"],df["Low"], df["Close"], timeperiod=2)
#atr = talib.ATR(high[0],low[0], close[0], timeperiod=5)

#print(atr)
