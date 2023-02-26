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


# rets = [0.01, -0.01, 0.004, -0.02, 0.01]
# n = 1
# # print(cal(rets, n))  # Output: -0.0259
# print(nth_largest_drawdown(rets, n))

# rets = [0.01, -0.04, 0.05, -0.01, -0.01, 0.01]
# n = 3
# # print(cal(rets, n))  # Output: 2
# print(nth_largest_drawdown(rets, n))

# rets = [0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04,
#         0.005, -0.01, 0.01, 0.01, 0.01, -0.02, 0.005, -0.01, 0.01, 0.01, -0.01, 0.01]
# n = 2
# # print(cal(rets, n))  # Output: -0.0249
# print(nth_largest_drawdown(rets, n))
# num = (0.9928340334643394 - 0.9680638171634375) / 0.9928340334643394
# round(num, 4)
# print(round(num, 4))
