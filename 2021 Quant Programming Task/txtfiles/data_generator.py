import csv
import os
import random
from datetime import datetime
from random import randrange
import datetime
import shutil

def random_date(start):
    curr = start
    curr += datetime.timedelta(minutes=randrange(10))
    curr += datetime.timedelta(milliseconds=randrange(1000))
    return curr


def random_vol(prc):
    vol = random.randrange(int(-.05 * prc), int(.05 * prc))
    # flt = float(random.randrange(-99, 99) / 100)
    return vol

import glob
# stock_symbol = ['AAPL', 'GOOG', 'AMZN', 'TSLA', 'BRK', 'MSFT', 'TSM']
files = glob.glob('/Users/jeffreychen/c++ developer/BestEx Case Study/Case Study/Case Study/stktxt/*')
if files:
    for f in files:
        os.remove(f)
for i in range(10000):
    fname = f'stock_{i}.txt'
    exchanges = ['NYSE_ARCA', 'NSX', 'NYSE', 'NASDAQ', 'CBOE']

    side = ['Ask', 'Bid']
    count = 0
    with open(f'/Users/jeffreychen/c++ developer/BestEx Case Study/Case Study/Case Study/stktxt/{fname}', 'w', newline='') as f:
    # with open(f'/Users/jeffreychen/c++ developer/BestEx Case Study/Case Study/Case Study/test_txt/{fname}', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Timestamp', 'Price', 'Size', 'Exchange', 'Type'])
        startDate = datetime.datetime(2021, 3, 5, 9, 30, 1)
        prc = random.randint(50, 1000)
        for _ in range(1000):
            ts = random_date(startDate)
            tsstr = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            try:
                prc += random_vol(prc)
                prc = round(prc, 2)
            except Exception as e:
                prc = prc
                count += 1
            size = random.randint(1, 100)
            exchange = random.choice(exchanges)
            trade = random.choice(side)
            writer.writerow([tsstr, f'{prc}', f'{size}', f'{exchange}', f'{trade}'])
            startDate = ts
    print(f'Wrote {fname}, with total erro {count}')

# Timestamp, Price, Size, Exchange, Type
# 2021-03-05 10:00:00.123, 46.14, 120, NYSE_ARCA, Ask
# 2021-03-05 10:00:00.123, 46.13, 110, NSX, Bid
# 2021-03-05 10:00:00.130, 46.13, 120, NYSE, TRADE
# 2021-03-05 10:00:00.131, 46.14, 120, NYSE_ARCA, Ask
#
# Symbol, Timestamp, Price, Size, Exchange, Type
# CSCO, 2021-03-05 10:00:00.123, 46.14, 120, NYSE_ARCA, Ask
# CSCO, 2021-03-05 10:00:00.123, 46.13, 110, NSX, Bid
# MSFT, 2021-03-05 10:00:00.123, 228.5, 120, NYSE, Ask
# MSFT, 2021-03-05 10:00:00.123, 228.4, 110, NASDAQ, Bid
# CSCO, 2021-03-05 10:00:00.130, 46.13, 120, NYSE, TRADE
# CSCO, 2021-03-05 10:00:00.131, 46.14, 120, NYSE_ARCA, Ask
# MSFT, 2021-03-05 10:00:00.133, 228.5, 120, NYSE, TRADE
# MSFT, 2021-03-05 10:00:00.134, 228.5, 120, NYSE_ARCA, Ask
