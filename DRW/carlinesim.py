import numpy as np


def choose_lane(prob):
    return np.random.choice([1, 0], p=[prob, 1-prob])

def can_lane_sim(n):
    dp = np.zeros((n, 2))

    dp[0, 0] = 1


    for r in range(1, n):
        if dp[r-1][0]:
            staylane = choose_lane(0.5)
            dp[r][0] = staylane
            dp[r][1] = 1 - staylane
        elif dp[r-1][1]:
            staylane = choose_lane(0.3)
            dp[r][1] = staylane
            dp[r][0] = 1 - staylane
    staytime = np.sum(dp, axis=0)
    return staytime[0]/n

print(can_lane_sim(100000))