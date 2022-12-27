
def expected_red_black(r, b):
    dp = [[0]*(b+1) for _ in range(r+1)]
    for i in range(1, r+1):
        dp[i][0] = 0
    for j in range(1, b+1):
        dp[0][j] = j
    for row in range(1, r+1):
        for col in range(1, b+1):
            dp[row][col] = max(col-row,
            col/(col+row)*dp[row][col-1] + row/(col+row)*dp[row-1][col])
    return dp[-1][-1]
def E(r,b):
    if r==0: return 0
    if b==0: return r
    return max([0,r/(r+b)*(1+E(r-1,b))+b/(r+b)*(-1+E(r,b-1))])    
print(expected_red_black(26,26))
print(expected_red_black(3,3))