from math import factorial


def evenKSum(arr):
    ans = 0
    return ans 

# print(28+29+31+35)
# x = factorial(10)*(1 -1 +1/2 - 1/factorial(3) + 1/factorial(4) -1/factorial(5) + 1/factorial(6) -1/factorial(7) + 1/factorial(8) - 1/factorial(9) + 1/factorial(10))


import math
 
# This function receives an integer
# n, and returns the number of
# digits present in n!
 
 
def findDigits(n):
 
    # factorial exists only for n>=0
    if (n < 0):
        return 0
 
    # base case
    if (n <= 1):
        return 1
 
    # else iterate through n and
    # calculate the value
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)
 
    return math.floor(digits) + 1