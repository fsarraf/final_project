import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import iexfinance
from iexfinance.refdata import get_symbols 
from iexfinance.stocks import Stock
from iexfinance.altdata import get_social_sentiment
import requests


token = 'pk_b5ee16430764408b9821c3d6af15d4b3'
base_url = 'https://cloud.iexapis.com/stable'
token_request = '?token={}'.format(token)

def get_earnings():
    
    earnings = '/stock/market/today-earnings'
    earnings_today = base_url + earnings + token_request
    r = requests.get(earnings_today)
    
    bto = pd.DataFrame(earnings['bto'])
    bto_quote = bto.quote.apply(pd.Series)
    bto=bto.merge(bto_quote)
    
    
    amc = pd.DataFrame(earnings['amc'])
    amc_quote = amc.quote.apply(pd.Series)
    amc = amc.merge(amc_quote)
    
    earnings_df = pd.concat([bto, amc], sort=True, ignore_index=True )
    earnings_df.drop('quote', axis=1, inplace=True)
    
    return earnings_df

