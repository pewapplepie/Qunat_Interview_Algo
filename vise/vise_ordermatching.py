"""
Given a stream of incoming "buy" and "sell" orders (as lists of limit price, quantity, and side, like

["155", "3", "buy"]), determine the total quantity (or number of "shares") executed.

A "buy" order can be executed if there is a corresponding "sell" order with a price that is less than or

equal to the price of the "buy" order.

Similarly, a "sell" order can be executed if there is a corresponding "buy" order with a price that is

greater than or equal to the price of the "sell" order.

It is possible that an order does not execute immediately if it isn't paired to a counterparty. In that 

case, you should keep track of that order and execute it at a later time when a pairing order is found.

You should ensure that orders are filled immediately at the best possible price. That is, an order 

should be executed when it is processed, if possible. Further, "buy" orders should execute at the 

lowest possible price and "sell" orders at the highest possible price at the time the order is handled.

Note that orders can be partially executed.

--- Sample Input ---

orders = [
  ['150', '5', 'buy'],    # Order A

  ['190', '1', 'sell'],   # Order B

  ['200', '1', 'sell'],   # Order C

  ['100', '9', 'buy'],    # Order D

  ['140', '8', 'sell'],   # Order E

  ['210', '4', 'buy'],    # Order F

]


200 1
190 1
140 8

210 4
150 5
100 9

Sample Output

9

[execution time limit] 3 seconds (java)

[input] array.array.string orders

[output] integer



Order Book

Buys: ['100', '9', 'buy']

Sells: , ['200', '1', 'sell']

Total Shares: 5 + 3 + 1 = 9
"""

from dataclasses import dataclass
import heapq

@dataclass
class Order:
    price: float
    quantity: int
    side: str

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # List of buy orders: [(price, quantity)]
        self.sell_orders = []  # List of sell orders: [price, quantity]
        self.total_shares = 0

    def execute_order(self, price, quantity, side):
        if side == 'buy':
            if not self.sell_orders or price < self.sell_orders[0][0]:
                heapq.heappush(self.buy_orders, (-price, quantity))
            else:
                execute_shares = 0
                while self.sell_orders and price >= self.sell_orders[0][0] and quantity > 0:
                    prc, quant = heapq.heappop(self.sell_orders)
                    execute_shares += quant
                    quantity -= quant
                
                if quantity > 0:
                    heapq.heappush(self.buy_orders, (-price, quantity))

                else:
                    quant = abs(quantity)
                    execute_shares -= quant
                    heapq.heappush(self.sell_orders, (prc, quant))
                
                self.total_shares += execute_shares

        elif side =='sell':
            if not self.buy_orders or price > abs(self.buy_orders[0][0]):
                heapq.heappush(self.sell_orders, (price, quantity))
            else:
                execute_shares = 0
                while self.buy_orders and price <= abs(self.buy_orders[0][0]) and quantity > 0:
                    prc, quant = heapq.heappop(self.buy_orders)
                    prc = abs(prc)
                    execute_shares += quant
                    quantity -= quant
               
                if quantity > 0:
                    heapq.heappush(self.sell_orders, (price, quantity))
                else:
                    quant = abs(quantity)
                    execute_shares -= quant
                    heapq.heappush(self.buy_orders, (-prc, quant))
                
                self.total_shares += execute_shares
        
        return self.total_shares

def total_executed_shares(orders):
    order_book = OrderBook()
    for order in orders:
        price, quantity, side = int(order[0]), int(order[1]), order[2]
        order_book.execute_order(price, quantity, side)
    return order_book.total_shares

orders = [
    ['150', '5', 'buy'],
    ['190', '1', 'sell'],
    ['200', '1', 'sell'],
    ['100', '9', 'buy'],
    ['140', '8', 'sell'],
    ['210', '4', 'buy']
]

print(total_executed_shares(orders))