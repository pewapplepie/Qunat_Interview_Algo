"""
Given a matrix of N * M. Find the maximum path sum in matrix. The maximum path is sum of all elements from first row to last row where 
you are allowed to move only down or diagonally to left or right. You can start from any element in first row.

Examples:

Input : mat[][] = 10 10  2  0 20  4
                   1  0  0 30  2  5
                   0 10  4  0  2  0
                   1  0  2 20  0  4
Output : 74
The maximum sum path is 20-30-4-20.

Input : mat[][] = 1 2 3
                  9 8 7
                  4 5 6
Output : 17
The maximum sum path is 3-8-6.
"""

def findMaxPath(mat):
    n, m = len(mat), len(mat[0])
    dp = [[0]*m for _ in range(n)]
    for i in range(m):
        dp[0][i] = mat[0][i]
    
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = max(dp[i-1][j]+mat[i][j], dp[i-1][j+1]+mat[i][j])
            elif j == m-1:
                dp[i][j] = max(dp[i-1][j]+mat[i][j], dp[i-1][j-1]+mat[i][j])
            else:
                dp[i][j] = max(dp[i-1][j]+mat[i][j], dp[i-1][j+1]+mat[i][j], dp[i-1][j-1]+mat[i][j])
    ans = max(dp[-1][:])
    return ans
    
def maxEnergy (mat):
    # Write your code here
    cost = mat[0]
    for i in range(1, len (mat)):
        curr = []
        curr.append(max(cost[:2]) + mat[i][0])
        for j in range(1, len(mat[0])-1):
            curr.append(max(cost[j-1:j+2]) + mat[i][j])
        curr.append(max(cost[-2:]) + mat[i][-1])
        cost = curr
    return max(cost)


mat = ([[ 10, 10, 2, 0, 20, 4 ], 
        [ 1, 0, 0, 30, 2, 5 ], 
        [ 0, 10, 4, 0, 2, 0 ], 
        [ 1, 0, 2, 20, 0, 4 ]]) 
                
print(findMaxPath(mat)) #74
print(maxEnergy(mat)) #74

mat = ([[1,2,3],
        [9,8,7],
        [4,5,6]])

print(findMaxPath(mat)) #17
print(maxEnergy(mat))