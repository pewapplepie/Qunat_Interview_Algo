import datetime
import pandas as pd
import numpy as np

A = pd.read_csv("stockA.csv")
B = pd.read_csv("stockB.csv")

def price_chg_signal(stk: pd.DataFrame, c):
    print('get price change')
    prices = stk['price'].astype(float)
    active = [0] * len(prices)

    prev = prices[0]
    for i, p in enumerate(prices[1:]):
        if abs(p - prev) > c:
            active[i] = 1
        prev = p
    stk['active'] = active
    print('ttl active : ', sum(active))
    return stk

def get_ms_time(stk:pd.DataFrame):
    print('convert time')
    stk['timestamp'] = pd.to_datetime(stk['timestamp'])
    stk['ms'] = stk['timestamp'].astype(int)//10**6
    return stk

def mark_nxt_traded_time(stk: pd.DataFrame, baseStk:pd.DataFrame, m):
    print('mark trade')
    try:
        print('check stk len: ', len(stk),', marking from len', len(baseStk))
        activeBaseStk = baseStk[baseStk['active'] == 1]
        signal_time= activeBaseStk['ms'].values
        print('signal timing total : ', len(signal_time))
        trade_time = [0]*len(stk['ms'])

        stkms = stk['ms']
        i = 0
        trade_position = 0
        while i < len(stkms):
            if trade_position < len(signal_time) and stkms[i] >= signal_time[trade_position] + m:
                trade_position += 1
                trade_time[i] = 1
            if trade_time[i] == 1 and i + 1 < len(stkms):
                trade_time[i + 1] = -1
                i += 1
            i += 1
        stk['trade_time'] = trade_time
        print('end signal position : ', trade_position)
        print('end trade position : ', i)

    except Exception as e1:
        print('some error: ', e1)
    return stk

def calc_profit(stk):
    prices = stk['price'].values
    position = stk['trade_time'].values
    profits = prices * position
    print('senity check, ttl marked position : ', sum(position!=0), '|ttl profit position', sum(profits != 0))
    return sum(profits)


def trading_algo(stkA, stkB, m, c):
    try:
        stkA = price_chg_signal(stkA, c)
        stkB = price_chg_signal(stkB, c)
    except Exception as e:
        print(e)

    try:
        stkA = get_ms_time(stkA)
        stkB = get_ms_time(stkB)
    except Exception as e:
        print(e)
    

    stkA = mark_nxt_traded_time(stkA, stkB, m)
    # stkB = mark_nxt_traded_time(stkB, stkA, m)

    profitA = calc_profit(stkA)
    # profitB = calc_profit(stkB)
    return profitA 
print(trading_algo(A, B, 40, 4))

