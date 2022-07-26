import pandas as pd
import numpy as np

def dynamic_card_game(b, r):
    dp = [[0]*b for _ in range(r)]
    #dp[0][0] = 0
    for i in range(b):
        dp[0][i] = i
    for i in range(r):
        dp[i][0] = 0
    
    for col in range(1,b):
        for row in range(1, r):
            remain = row+col
            dp[row][col] = max(col-row, col/remain*dp[row][col-1]+row/remain*dp[row-1][col])
    #print(pd.DataFrame(dp))    
    return dp[b-1][r-1]
    # if r == 0:
    #     return b
    # if b == 0:
    #     return 0
    # return max(b-r, b/(b+r)*dynamic_card_game(b-1, r) + r/(b+r)*dynamic_card_game(b, r-1))

dynamic_card_game(27,27)
    