import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import as_strided

def window_view(x, window_size):
    y = as_strided(x, shape=(x.size - window_size + 1, window_size),
                   strides=(x.strides[0], x.strides[0]))
    return y
def drawdown_window(values, window_size=7):
    # values = pd.Series(values)
    # returns = values.pct_change()
    # cum_ret = returns.cumsum().to_numpy()
    # y = window_view(cum_ret, window_size=window_size)
    # running_max_y = np.maximum.accumulate(y, axis=1)
    # dd = y - running_max_y
    # dd = dd.min(axis=1)
    # # print(running_max)

    # prc = (1 + dd)
    series = pd.Series(values)
    # Calculate the rolling maximum value with a window size of 7
    print(values)
    reverse = series[::-1]
    last_window = reverse.rolling(window=window_size, min_periods=1).max()[:window_size][::-1]
    rolling_max = reverse.rolling(window=window_size).max()
    rolling_max = rolling_max[::-1]
    rolling_max = rolling_max.fillna(np.nan)
    # print(last_window[1:])
    # print(rolling_max[-10:])
    rolling_max = [val for val in rolling_max if not np.isnan(val)]
    # print(len(last_window))
    rolling_max.extend(last_window[1:])
    # print(rolling_max)
    # Calculate the daily drawdown
    drawdown = (series - rolling_max) / series 
    # # Calculate the maximum drawdown
    max_drawdown = min(drawdown) 
    # # Multiply by 10000 and floor the result
    max_drawdown_percentage = np.floor(max_drawdown * 10000)
    # return max_drawdown_percentage.min()
    return nt99


if __name__ == '__main__':
    # print('Hiii')
    with open('dd_input001.txt', 'r') as f:
        inputs = f.readlines()
    
    clean_input = [
        int(t.strip('\n'))
        for t in inputs
    ]
    out = drawdown_window(clean_input[1:])
    print(out) # 458