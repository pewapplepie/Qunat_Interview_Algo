"""
The following sequence is formed using words and numbers:
• The first number is 1
• In the first number, there was one 1 so the second number is 11
• In the second number, there were two 1s, so the third number is 21
• In the previous number, there was one 2 and there was one 1, so the fourth number is 1211
• The next number is 111221, one 1, one 2, two 1's.
This sequence can continue infinitely. Given an integer, q[i], determine the sum of the digits of the value in the sequence at that position. 
For example, position 4 contains the value 1211. The sum of those digits is 1 + 2 + 1 + 1 = 5.
Each test case will contain n queries passed as an integer array. 
Return an array of integers that contains answers for the queried integers. 
The th answer should correspond to the th query.

Function Description
Complete the function sumOfTheDigits in the editor below.
sumOfTheDigits has the following parameter(s):
int q[n]: array of integers that denote sequence positions to query
Returns:
int[n]: an array of integers where the th value is the answer to the th query

Constraints
• 1 ≤ n≤ 1000
• 1 ≤ q[i] ≤ 54

Sample Input
STDIN
Function
q[] size n = 3
q = [1, 2, 3]
Sample Output
[1,2,3]
Explanation
Retrieve the sums of digits in the first, the second and the third elements of the sequence. 
These elements are 1, 11, 21.
"""
def compress(chars:str) -> int:
    res = ''
    idx = 0
    while idx < len(chars):
        grouplen = 1
        while grouplen + idx < len(chars) and chars[idx + grouplen] == chars[idx]:
            grouplen += 1
        if grouplen > 1:
            num = str(grouplen)
            res += num
        else:
            res += '1'
        res += chars[idx]
        idx += grouplen
    return res


def sumOfTheDigits(q):

    n = max(q)
    dp = [0] * n 
    dp[0] = '1'
    for i in range(1, n):
        dp[i] = compress(dp[i-1])
    
    print(dp)
    out = [0] * len(q)

    for i in range(len(q)):
        numstr = dp[q[i] - 1]
        out[i] = sum([int(c) for c in numstr])

    return out

print(sumOfTheDigits([1,2,3]))
print(sumOfTheDigits([1,5,4,3]))


