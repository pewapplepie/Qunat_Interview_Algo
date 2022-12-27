import os
import pandas as pd
from typing import Dict, List
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sn


path = "/Users/jeffreychen/Qunat_Interview_Algo/2021 Quant Programming Task/mkt_data"
dir_list = os.listdir(path)
all_data = []
for file in dir_list[:2]:
    all_data.append(pd.read_csv(path + '/' + file))


#
def cln_df(df: pd.DataFrame):
    cols: List[str] = df.columns
    for col in cols:
        if ' ' in col:
            col_name = col.strip()
            df[col_name] = df[col]
            del df[col]
    return df


data1: pd.DataFrame = cln_df(all_data[0])
data1.index = pd.to_datetime(data1['timestamp'], unit='ms')
data1['bidask_spread'] = data1['ask_price'] - data1['bid_price']
# data1_min = data1.resample("15min").agg({'bidask_spread':['mean']})
avg_sprd_15min = data1.resample("15min")['bidask_spread'].mean()
avg_vol_15min = data1.resample("15min")['volume'].mean()/data1['volume'][-1]
avg_vwap_15min = data1.resample("15min")['vwap'].mean()

# def plot_15_min(df:pd.DataFrame):
    