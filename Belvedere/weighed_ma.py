import sys

def process_trade(trade):
    key, value, quantity, sequence = trade.split(',')
    value = float(value)
    quantity = int(quantity)
    sequence = int(sequence)
    return key, value, quantity, sequence


import random
import numpy as np

def generate_mock_data(rows):
    data = []
    for _ in range(rows):
        row_data = [str(random.randint(1, 1000)) for _ in range(4)]
        data.append(','.join(row_data))
    return data

from sklearn.linear_model import LinearRegression

def asset_impact():
    data = generate_mock_data(10)
    inputs = []
    for line in data:
        a,b,c,pnl = map(float, line.split(','))
        inputs.append([a,b,c,pnl])
    
    data_array = np.array(inputs)

    X = data_array[:, :3]
    y = data_array[:, 3]

    model = LinearRegression()
    model.fit(X=X, y=y)
    
    coefs = model.coef_
    print(coefs)

asset_impact()
    



