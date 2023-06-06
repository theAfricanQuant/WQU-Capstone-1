"""
The user is prompted to select a 'F' or 'M' on screen
This module allows the user to manually enter the tickers on screen
when selected 'M'
or upload the file containing tickers
when selevted 'F'
@author: lipi
"""
import os
import pandas as pd


def stock_entry_option():
    print ('Please note that the program supports Stocks listed in S&P500 as of now')
    r = raw_input ('Select F to choose a file of tickers\OR\Select M for manual input of tickers: ')
    StockTickerArray = []

    if r not in ['F', 'M']:
        raise ValueError("\nOops! wrong entry\Enter only F or M")

    if r == 'F':#for upload through file    
        user_input = raw_input("Enter your ticker file: ")
        assert os.path.exists(
            user_input
        ), f"I did not find the file at, {str(user_input)}"
        #open the file
        xlsx = pd.ExcelFile(user_input)
        S1 = xlsx.parse(0)
        StockTickerArray = (S1['TICKERS'].values.tolist())

    else: #to upload manually   
        StockCount = input ('Input the number of stocks in the portfolio: ')
        S1 = []
        for i in range(1,StockCount+1):
            StockTicker = raw_input(f'Enter Stock Ticker {str(i)}: ')
            StockTickerArray.append(str(StockTicker)) 

    #Broad Market Index is entered         
    StockTickerArray.append('^GSPC')
    return StockTickerArray