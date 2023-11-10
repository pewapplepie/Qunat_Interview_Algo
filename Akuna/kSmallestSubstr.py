"""
There is a string input str consisting of characters
'O' and '1' only and an integer k. 
Find a substring of string input_str such that:
• The number of '1's is equal to k
• It has the smallest length
• It is lexicographically smallest
Note: It is guaranteed that answer always exists.
Example
input str = "0101101"
k=3
Some of the possible substrings following the first condition:
• "01011"
• "1101"
• "1011"
The substring that is smallest in length and lexicographically smallest is "1011"
It can be proven that there is no other substring that is smaller than "1011 "in length and lexicographic order. 
Hence the answer is "1011".
"""

import collections


def solution(input_str, k):

    smallest = None
    windowstr = collections.deque([])
    i = 0
    while i < len(input_str): 
        while windowstr.count('1') < k:
            windowstr.append(input_str[i])
            i += 1
        if not smallest:
            smallest = ''.join(windowstr) 
        
        while windowstr and windowstr.count('1') == k:
            print(windowstr)
            currsmall = ''.join(windowstr)
            if len(currsmall) < len(smallest):
                smallest = currsmall
            elif len(currsmall) == len(smallest) and currsmall < smallest:
                smallest = currsmall
            windowstr.popleft()


    return smallest

        
print(solution('0101101', 3)) #1011