"""
1. Calculate the Drawdown
A portfolio drawdown is the total return of an investment from peak (highest performance)
trough (lowest subsequent performance). The drawdown period is the time after the peak
date to (including) the trough date of the drawdown.
The first largest drawdown is the drawdown which has the largest magnitude. The second
largest drawdown is the largest drawdown in the time either before or after the first largest
drawdown. Drawdowns cannot overlap. The following illustration shows drawdowns for an
example stock:
1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1/10
Example Stock Performance
min
M
3rd Largest
Drawdown
1/11 1/12 1/13
1/14
Largest
Drawdown
1/15 1/16
2nd Largest
Drawdown
1/17
In this exercise you will build a function that takes in a list of returns, rets and an integer n;
and return the nth largest drawdown.
To complete this challenge, write a function in the editor that takes two parameters: a list o
period returns, returns and an integer n, and then returns the nth largest drawdown as a
float rounded to 4 decimal places (i.e. -0.1234 = -12.34%). Returns are expressed in
decimal form, i.e. 0.01 in the list = 1% fund return, and ordered from earliest to latest.

In this exercise you will build a function that takes in a list of returns, rets and an integer n; and return the nth largest drawdown.
To complete this challenge, write a function in the editor that takes two parameters: a list of period
returns, returns and an integer n, and then returns the nth largest drawdown as a float rounded to 4 decimal places (i.e. -0.1234 = -12.34%). Returns are expressed in decimal form, i.e. 0.01 in the list = 1% fund return, and ordered from earliest to latest.
In the case of ties, the function should return the same drawdown for each case (ie if the second and third largest drawdowns are the same, the function should return the same value for n=2 and n=3).
14
15
16
# The function is expected to return a FLOAT. 
# The function accepts following parameters: 
# 1. FLOAT_ARRAY rets
If the nth largest drawdown doesn't exist, the function should return the total number of drawdowns identified in the full time-series (0 if no drawdown exists).
"""

import matplotlib.pyplot as plt
import numpy as np


def cal(rets, n):
    curr = 1
    peak = 1
    valley = 1
    drawdowns = []
    prices = []
    stack = []

    for i, ret in enumerate(rets):
        # calculate curr price with return
        curr *= (1 + ret)
        # print(i, curr)
        prices.append(curr)
        if curr >= peak:
            # curr price higher than the all time peak
            while len(stack) > 0:
                temp_peak, temp_valley = stack.pop()
                drawdown = (temp_peak - temp_valley) / temp_peak
                drawdowns.append(drawdown)
            # set the new peak as the curr price
            peak = curr
            valley = peak  # reset valley as well
            stack.append((curr, curr))
        elif curr <= valley:
            # curr price is lower than previous valley
            valley = curr  # update valley
            stack = []  # reset the stack
            stack.append((peak, valley))
        else:
            # curr price is between the previous peak and valley
            if stack[-1][0] > curr and stack[-1][1] < curr:
                stack.append((curr, curr))
            else:
                temp_peak, temp_valley = stack[-1]
                if curr >= temp_peak:
                    # curr price higher than the previous peak in stack
                    while curr >= temp_peak:
                        stack.pop()
                        drawdown = (temp_peak - temp_valley) / temp_peak
                        drawdowns.append(drawdown)
                        temp_peak, temp_valley = stack[-1]
                    stack.append((curr, curr))
                elif curr < temp_valley:
                    # curr price higher than the previous valley in stack
                    while curr < stack[-1][1]:
                        temp_peak, temp_valley = stack.pop()
                    stack.append((temp_peak, curr))

    while len(stack):
        temp_peak, temp_valley = stack.pop()
        drawdown = (temp_peak - temp_valley) / temp_peak
        drawdowns.append(drawdown)

    drawdowns.sort(reverse=True)
    while drawdowns[-1] == 0:
        drawdowns.pop()
    # print(drawdowns)
    if n > len(drawdowns):
        return len(drawdowns)
    return round(drawdowns[n-1] * -1, 4)


rets = [0.01, -0.01, 0.004, -0.02, 0.01]
n = 1
print(cal(rets, n))  # Output: -0.0259
# print(nth_largest_drawdown(rets, n))

rets = [0.01, -0.04, 0.05, -0.01, -0.01, 0.01]
n = 3
print(cal(rets, n))  # Output: 2
# print(nth_largest_drawdown(rets, n))

rets = [0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04,
        0.005, -0.01, 0.01, 0.01, 0.01, -0.02, 0.005, -0.01, 0.01, 0.01, -0.01, 0.01]
n = 2
print(cal(rets, n))  # Output: -0.0249
# print(nth_largest_drawdown(rets, n))
# num = (0.9928340334643394 - 0.9680638171634375) / 0.9928340334643394
# round(num, 4)
# print(round(num, 4))


# # test case 1
# rets = [0.01, -0.01, 0.004, -0.02, 0.01]
# n = 1
# print(nth_largest_drawdown(rets, n))  # -0.0259

# # test case 2
# rets = [0.01, -0.04, 0.05, -0.01, -0.01, 0.01]
# n = 3
# print(nth_largest_drawdown(rets, n))  # 2

# # test case 3
# rets = [0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04,
#         0.005, -0.01, 0.01, 0.01, 0.01, -0.02, 0.005, -0.01, 0.01, 0.01, -0.01, 0.01]
# n = 2
# print(nth_largest_drawdown(rets, n))  # -0.0249