""" Limit Order Book

Construct a limit order book

Assume you have an API with the following callbakcs:
    - onNewOrder(ong ID, string stockTicker, float price, int quantity, int side)    
    - onCancelledOrder(ong ID, string stockTicker, float price, int quantity, int side)    
    - onExecutedOrder(ong ID, string stockTicker, float price, int quantity, int side)    

where
    - ID is a non-negative, strictly increasing unique identifier
    - quantity is a positive integer
    - side is 1 if the order is to buy, and -1 if the order is to sell

onNewOrderr is called when someone sends an order to an exchange. 
An example may be onNewOrder (ID=1, stockTicker=AAPL, price=115.00, quantity=100, side=1)
onCancelledOrder is called when someone wishes to cancel a previously-sent order, or some portion of it.
For instance, if you receive onCancelledOrder (ID=1, quantity=10) after the onNewOrder above, it effectively means 90 shares of the order submitted above remains active.
onExecutedOrder is called when another order executes against a previously-submitted order. 
For instance, if you recieve onExecutedOrder (ID=1, quantity=50), after the onNEwOrder AND onCancelledOrder above, it effectively means 40 shares of the order remains active

Assume you are receiving a continous stream of these events.

    1. Maintain an order book of all buy and sell orders
    2. Implemet a function top(int n, string, stockTicker, int side) that provides the top n buy or sell price levels, as specified by side, from the order book.
        - The top or 0th buy level is defined as the level with the maximum price of all buy orders submitted, with the total quantitty submited for that level,
            and each order comprising that level. The 1st buy order is the one with the maximum pricess less than the 0th order, and so on.
        - For sell orders, this is revered (0th is the one with the minimum price, and so on)
        - If there are curretly fewer than n price levels on that side, return as many price levels as possible
"""

import heapq
from dataclasses import dataclass

@dataclass
class Order:
    ord_id : str
    ticker : str
    price : float 
    quantity : int
    side : int 

class LimitOrderBook:
    def __init__(self):
        self.buy_heap = []
        self.sell_heap = []

    def add_order(self, order):
        if order.side == 1:
            heapq.heappush(self.buy_heap, (-order.price, order))
        else:
            heapq.heappush(self.sell_heap, (order.price, order))

        self.execute_trades()

    def cancel_order(self, order_id):
        for heap in [self.buy_heap, self.sell_heap]:
            for i in range(len(heap)):
                node = heap[i]
                for order in node[1]:
                    if order.id == order_id:
                        node[1].remove(order)
                        if len(node[1]) == 0:
                            del heap[i]
                        self.execute_trades()
                        return
        else:
            print('No order can cancel')
            return

    def execute_trades(self):
        while len(self.buy_heap) > 0 and len(self.sell_heap) > 0 and -self.buy_heap[0][0] >= self.sell_heap[0][0]:
            buy_node = heapq.heappop(self.buy_heap)
            sell_node = heapq.heappop(self.sell_heap)

            buy_orders = buy_node[1]
            sell_orders = sell_node[1]

            while len(buy_orders) > 0 and len(sell_orders) > 0 and buy_orders[0].price >= sell_orders[0].price:
                buy_order = buy_orders[0]
                sell_order = sell_orders[0]

                if buy_order.quantity > sell_order.quantity:
                    buy_order.quantity -= sell_order.quantity
                    del sell_orders[0]
                elif buy_order.quantity < sell_order.quantity:
                    sell_order.quantity -= buy_order.quantity
                    del buy_orders[0]
                else:
                    del buy_orders[0]
                    del sell_orders[0]

            if len(buy_orders) > 0:
                heapq.heappush(self.buy_heap, (-buy_node[0], buy_node[1]))
            if len(sell_orders) > 0:
                heapq.heappush(self.sell_heap, (-sell_node[0], sell_node[1]))

class OrderBook(LimitOrderBook):
    def on_new_order(self, order_id, stock_ticker, price, quantity, side):
         order = Order(id=order_id, 
                       ticker=stock_ticker,
                       price=price,
                       quantity=quantity,
                       side=side)
         self.add_order(order)
    def on_cancelled_order(self, order_id, quantity_to_cancel):
        self.cancel_order(order_id=order_id)
    def on_executed_order(self, order_id, quantity_to_execute):
        pass


    # Return format:
    # - List of price levels (list)
    #     - Price level (tuple)
    #         - Price (float)
    #         - Total quantity (int)
    #         - List of order IDs (list of ints)
    def top(n, stock_ticker, side):
        pass



# Test case 1: empty order book
order_book = OrderBook()
assert order_book.top(5, "AAPL", 1) == []
assert order_book.top(5, "AAPL", -1) == []

# Test case 2: single order on each side
order_book = OrderBook()
order_book.onNewOrder(1, "AAPL", 100.00, 10, 1)
order_book.onNewOrder(2, "AAPL", 200.00, 20, -1)
assert order_book.top(5, "AAPL", 1) == [(100.00, 10)]
assert order_book.top(5, "AAPL", -1) == [(200.00, 20)]

# Test case 3: multiple orders on each side
order_book = OrderBook()
order_book.onNewOrder(1, "AAPL", 100.00, 10, 1)
order_book.onNewOrder(2, "AAPL", 200.00, 20, -1)
order_book.onNewOrder(3, "AAPL", 90.00, 5, 1)
order_book.onNewOrder(4, "AAPL", 210.00, 10, -1)
assert order_book.top(1, "AAPL", 1) == [(200.00, 20)]
assert order_book.top(1, "AAPL", -1) == [(210.00, 10)]
assert order_book.top(2, "AAPL", 1) == [(200.00, 20), (100.00, 10)]
assert order_book.top(2, "AAPL", -1) == [(210.00, 10), (200.00, 20)]
assert order_book.top(3, "AAPL", 1) == [(200.00, 20), (100.00, 10), (90.00, 5)]
assert order_book.top(3, "AAPL", -1) == [(210.00, 10), (200.00, 20)]

# Test case 4: cancel an order
order_book = OrderBook()
order_book.onNewOrder(1, "AAPL", 100.00, 10, 1)
order_book.onNewOrder(2, "AAPL", 200.00, 20, -1)
order_book.onCancelledOrder(1, "AAPL", 100.00, 2)
assert order_book.top(5, "AAPL", 1) == [(98.00, 8)]
assert order_book.top(5, "AAPL", -1) == [(200.00, 20)]

# Test case 5: execute an order
order_book = OrderBook()
order_book.onNewOrder(1, "AAPL", 100.00, 10, 1)
order_book.onNewOrder(2, "AAPL", 200.00, 20, -1)
order_book.onExecutedOrder(2, "AAPL", 200.00, 10)
assert order_book.top(5, "AAPL", 1) == [(100.00, 10)]
assert order_book.top(5, "AAPL", -1) == [(200.00, 10)]
