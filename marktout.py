import pandas as pd
import numpy as np

def cal_maxt(timeS1, timeS2, horizon):
    pass


def calculateMarkout(trades, prices, horizon):
    trades_df = pd.DataFrame(trades, columns=['Symbol', 'Trade_Time', 'Trade_Price'])
    trades_df[['Trade_Time', 'Trade_Price']] = trades_df[['Trade_Time', 'Trade_Price']].astype(float)
    
    prices_df = pd.DataFrame(prices, columns=['Symbol', 'Time', 'Price'])
    prices_df[['Time', 'Price']] = prices_df[['Time', 'Price']].astype(float)
    
    trades_df['Trade_Time_p_Horizon'] = trades_df['Trade_Time'] + horizon
    
    ttl_marktout = 0
    for ticker, trade_per_ticker in trades_df.groupby('Symbol'):
        price_per_ticker = prices_df[prices_df['Symbol'] == ticker].copy()
        merged_ticker = pd.merge_asof(trade_per_ticker, price_per_ticker, left_on='Trade_Time_p_Horizon', right_on='Time')
        merged_ticker['Markout'] = merged_ticker['Price'] - merged_ticker['Trade_Price']
        ttl_marktout += merged_ticker['Markout'].values.sum()*100
        
    return int(ttl_marktout)
    # trades_df = pd.DataFrame(trades, columns=['Symbol', 'Trade_Time', 'Trade_Price'])
    # trades_df[['Trade_Time', 'Trade_Price']] = trades_df[['Trade_Time', 'Trade_Price']].astype(float)
    
    # prices_df = pd.DataFrame(prices, columns=['Symbol', 'Time', 'Price'])
    # prices_df[['Time', 'Price']] = prices_df[['Time', 'Price']].astype(float)
    
    # tickers = trades_df['Symbol'].unique() # type: ignore 
    # ttl_marktout = 0

    # for ticker in tickers:
    #     print(ticker)
    #     trade_per_ticker = trades_df[trades_df['Symbol'] == ticker].copy()
    #     price_per_ticker = prices_df[prices_df['Symbol'] == ticker].copy()
    #     trade_per_ticker['Trade_Time_p_Horizon'] = trade_per_ticker['Trade_Time'] + horizon
    #     merged_ticker = pd.merge_asof(trade_per_ticker, price_per_ticker, left_on='Trade_Time_p_Horizon', right_on='Time')
    #     merged_ticker['Markout'] = merged_ticker['Price'] - merged_ticker['Trade_Price']
    #     ticker_markout = merged_ticker['Markout'].values.sum()*100
    #     ttl_marktout += ticker_markout
    #     print(ticker_markout)
    #     print('======')
        
    # return int(ttl_marktout)


if __name__ == '__main__':
    # print('Hiii')
    with open('markout_input000.txt', 'r') as f:
        content = f.readlines()

    arrays = []
    i = 0
    while i < len(content):
        size = int(content[i].strip())
        i += 1
        array = []
        if i >= len(content):
            arrays.append(size)
            break
        for _ in range(size):
            line = content[i].strip()
            items = line.split(',')
            array.append(items)
            i += 1
        arrays.append(array)

    
    out = calculateMarkout(arrays[0], arrays[1], arrays[2])
    print(out) #-162
    # clean_input = [
    #     int(t.strip('\n'))
    #     for t in inputs
    # ]
    # print(inputs) # 458