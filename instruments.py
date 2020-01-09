# Class Creation for financial instruments

import pandas as pd
import numpy as np
from alpha_vantage.techindicators import TechIndicators

class FinancialInstruments(object):

    def __init__(self,symbol,price,df):
        self.symbol = symbol
        self.price = price
        self.df = df

    def my_symbol(self):
        print('my symbol is {}'.format(self.symbol))

    def get_sma(self, window1, window2, duration=0, series='close'):
        
        df_rolling = self.df.loc[:,[series]]
        symbol=self.symbol
        df_rolling.rename(columns={series:symbol}, inplace=True)
        
        df_rolling['sma1_{}'.format(series)] = df_rolling[symbol].rolling(window=window1).mean()
        df_rolling['sma2_{}'.format(series)] = df_rolling[symbol].rolling(window=window2).mean()

        df_rolling['positions_{}'.format(series)] = np.where(df_rolling['sma1_{}'.format(series)] > df_rolling['sma2_{}'.format(series)],1,-1 )

        ax = df_rolling[[symbol,'sma1_{}'.format(series),'sma2_{}'.format(series),
                         'positions_{}'.format(series)]].iloc[duration:].plot(figsize=(12,10), 
                        secondary_y = 'positions_{}'.format(series))
        ax.get_legend().set_bbox_to_anchor((0.25,0.85))

        return df_rolling, ax

    