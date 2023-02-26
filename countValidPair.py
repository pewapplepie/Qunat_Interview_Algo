# def count_pairs(numbers, k):
#     pairs = set()
#     for a in numbers:
#         for x in range(1, len(numbers)+1):
#             b = (a + k) ** x
#             if b in numbers:
#                 pairs.add((a, b))
#     return len(pairs)


# count_pairs([1,2,1728,5,6,10, 1331, 9], 2)
def cal(rets, n):
    drawdowns = []
    curr = 1
    peak = curr
    valley = curr

    for ret in rets:
        curr *= (1 + ret)
        if curr > peak:
            if peak != valley:
                drawdown = (peak - valley)/peak
                drawdowns.append(drawdown)
            peak = curr
            valley = peak
        elif curr < valley:
            valley = curr

    if peak != valley:
        drawdown = (peak - valley)/peak
        drawdowns.append(drawdown)
    drawdowns.sort(reverse=True)
    print(drawdowns)
    if n > len(drawdowns):
        return len(drawdowns)
    return round(drawdowns[n-1] * -1, 4)

t = [0.01, -0.01, 0.01, 0.01, 0.01, -0.02, 0.01, -0.03, 0.02, -0.04, 0.005, -0.01, 0.01, 0.01, 0.01, -0.02, 0.005, -0.01, 0.01, 0.01, -0.01, 0.01]
cal(t, 2)