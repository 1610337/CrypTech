from pandas_datareader import data as pdr

import fix_yahoo_finance as yf

yf.pdr_override()  # <== that's all it takes :-)

def main():
    print("Update Data in res folder")

    # download dataframe
    #data = pdr.get_data_yahoo("AMZN", start="1970-01-01", end="2017-04-30")

    print(yf.get_components_yahoo("AMZN"))

    # download Panel
    #data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")

    p#rint(data)


main()