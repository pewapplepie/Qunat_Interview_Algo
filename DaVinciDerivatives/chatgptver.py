import pandas as pd

# Load the data for stocks A and B
data_a = pd.read_csv('stockA.csv')
data_b = pd.read_csv('stockB.csv')
data_a['price'] = data_a['price'].astype(float)
data_b['price'] = data_b['price'].astype(float)
data_a['timestamp'] = pd.to_datetime(data_a['timestamp'])
data_b['timestamp'] = pd.to_datetime(data_b['timestamp'])
# Initialize variables
M = 40  # transfer time in milliseconds
c = 4.0  # threshold for price change
bought_b = False  # flag to indicate if we have bought stock B
prev_a_price = None  # previous price of stock A
total_profit = 0
# Loop through the data for stock A
for i in range(1, len(data_a)):
    curr_a_price = data_a['price'][i]
    curr_a_time = pd.to_datetime(data_a['timestamp'][i])

    # Check if the price of stock A has changed by more than the threshold
    if prev_a_price is not None and abs(curr_a_price - prev_a_price) > c:
        # Calculate the time to buy/sell stock B
        trade_time = curr_a_time + pd.Timedelta(milliseconds=M)

        # Buy or sell stock B depending on the direction of price change in stock A
        if curr_a_price > prev_a_price:
            if not bought_b:
                bought_b = True
                b_price = data_b[data_b['timestamp'] >= trade_time]['price'].iloc[0]
                print(f"Bought B at {trade_time} for {b_price}")
        else:
            if bought_b:
                bought_b = False
                s_price = data_b[data_b['timestamp'] >= trade_time]['price'].iloc[0]
                profit = s_price - b_price
                total_profit += profit
                print(f"Sold B at {trade_time} for {s_price} and made a profit of {profit}")

    prev_a_price = curr_a_price
print(f"Total profit of this trading algo is {total_profit}")

# import pandas as pd
# import numpy as np

# # Load data for stocks A and B
# data_A = pd.read_csv('stockA.csv')
# data_B = pd.read_csv('stockB.csv')

# # Convert timestamps to Timestamp objects
# data_A['timestamp'] = pd.to_datetime(data_A['timestamp'])
# data_B['timestamp'] = pd.to_datetime(data_B['timestamp'])

# # Set parameters
# c = 4.0
# M = pd.Timedelta('40ms')

# # Initialize variables
# B_position = 0
# B_last_price = 0
# total_profit = 0

# # Loop through data for stock A
# for index_A, row_A in data_A.iterrows():
#     # Check if price of stock A has changed by more than c
#     if index_A > 0:
#         price_change_A = abs(row_A['price'] - data_A.iloc[index_A-1]['price'])
#         if price_change_A >= c:
#             # Execute trade in stock B
#             trade_time = row_A['timestamp'] + M
#             data_B_after_trade = data_B.loc[data_B['timestamp'] >= trade_time]
#             if len(data_B_after_trade) > 0:
#                 price_change_B = data_B_after_trade.iloc[0]['price'] - B_last_price
#                 if price_change_A > 0:
#                     # Buy B
#                     if price_change_B > 0:
#                         profit = price_change_B
#                     else:
#                         profit = -price_change_B
#                     total_profit += profit
#                     B_position = 1
#                 else:
#                     # Sell B
#                     if price_change_B < 0:
#                         profit = -price_change_B
#                     else:
#                         profit = price_change_B
#                     total_profit += profit
#                     B_position = -1
#                 B_last_price = data_B_after_trade.iloc[0]['price']
            
# # Print total profit
# print("Total profit: ", round(total_profit, 2))