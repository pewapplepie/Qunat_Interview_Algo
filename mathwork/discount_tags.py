
# def max_even_sum(tags, index, current_sum, memo):
#     if index == len(tags):
#         return 0 if current_sum % 2 == 1 else current_sum
    
#     if (index, current_sum) in memo:
#         return memo[(index, current_sum)]
    
#     include_current = max_even_sum(tags, index + 1, current_sum + tags[index], memo)
#     exclude_current = max_even_sum(tags, index + 1, current_sum, memo)
    
#     memo[(index, current_sum)] = max(include_current, exclude_current)
#     return memo[(index, current_sum)]

# def getMaxiumEvenSum(tags):
#     memo = {}
#     return max_even_sum(tags, 0, 0, memo)    



def getMaxiumEvenSum(vals):
    dp = [[0 for _ in range(len(vals))] for _ in range(2)]
    even = 0
    odd = 1
    if vals[0]%2 == 0:
        dp[even][0] = vals[0]
        dp[odd][1] = vals[0]

    for i in range(1, len(vals)+1):
        if vals[i-1] % 2 == 0:
            dp[even][i] = max(dp[even][i-1], dp[even][i-1] + vals[i-1])
            dp[odd][i] = max(dp[odd][i-1], dp[odd][i-1] + vals[i-1])
        # else:
        #     dp[even][i] = max(dp[even][i-1], dp[odd][i-1] + vals[i-1])
        #     dp[odd][i] = max(dp[odd][i-1], dp[even][i-1] + vals[i-1])
        print(dp)
    return dp[even][-1]

        




print(getMaxiumEvenSum([2,3,6,-5,10,1,1])) #22
print(getMaxiumEvenSum([-1, -2, -3, 8, 7])) #14
print(getMaxiumEvenSum([6,3,4,-1,9,17])) #38