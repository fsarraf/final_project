import pandas as pd 
import numpy as np 
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt 
import instruments as ins



key='VD9R5Z3AFPXN93I0'
news_key='bax5hiv4byoig9decchsjhqvfmff9ld1qyhbvefv'


def get_daily(symbol, size='full'):
    
    ''' 
    DOCSTRING:

    get_daily retrieves the dail Open, High, Low, Close and volume of a specified
    stock.
    symbol : ticker symbol, default = 'AAPL'
    size: data set size. default  = 'full'
        full: 20 years of data
        compact: latest 100 data points
    '''
    # creating a Timeseries (ts) object and API call  that out puts a pandas DataFrame and
    # meta-data dictionary
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize=size)

    # Changing the column headers 
    headers = ['open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(data)
    df.columns = headers

    # sorting the DataFrame in ascending order of date
    df.sort_index(axis=0, ascending=True, inplace=True)

    # The function return the datafram and meta-data dictionary.
    return df, meta_data

def get_daily_close(symbol, size='full'):
    
    '''
    DOCSTRING:


    '''
#     if df != None:
#         df_close = df['close'].to_frame()
        
#     else:
#         print('getting info')
    df, _ = get_daily(symbol, size='full')
    df_close = df[['close']]
    

    return df_close

def get_multi_close(symbols, size='full'):
    
    df_lst=[]
    for i in range(0,len(symbols)):
        print(symbols[i])
        df = get_daily_close(symbols[i])
        df_lst.append(df)
    
    df = pd.concat(df_lst, axis=1)
    df.columns = symbols

    return df_lst, df

def create_fi(symbol, size='full'):
    df, meta = get_daily(symbol, size)
    price = df.close[-1]
    symbol = ins.FinancialInstruments(symbol,price,df)

    return symbol

from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt


ti = TechIndicators(key=key, output_format='pandas')

def get_adx(symbol = 'WBA'):
    data, meta_data = ti.get_adx(symbol=symbol, interval='daily', time_period=60)

    return data, meta_data

def get_macd(symbol = 'WBA', series = 'close'):
    data, meta_data = ti.get_macd(symbol=symbol ,interval='daily', series_type=series)

    return data, meta_data

def get_rsi(symbol = 'JNJ', series = 'close'):
    data, meta_data = ti.get_rsi(symbol= symbol, interval='daily', time_period=60, series_type='close')

    return data, meta_data

def get_obv(symbol = 'JNJ'):
    data, meta_data = ti.get_obv(symbol= symbol, interval='daily', )

    return data, meta_data

def get_vwap(symbol = 'JNJ'):
    data, meta_data = ti.get_vwap(symbol= symbol, interval='15min' )

    return data, meta_data

def get_intraday(symbol='JNJ', interval ='5min', size='full'):
    ts = TimeSeries(key=key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol= symbol,interval=interval, outputsize=size)
    
    return data, meta_data
    