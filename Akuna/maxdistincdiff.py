"""
Consider two arrays a and b where each consists of n integers.
In one operation:
1. Select two indices i and j (0 <= i,j < n)
2. Swap integers a[i]and b[i].
This operation can be performed at most k times. 
Find the maximum number of distinct elements that can be achieved in array a after at most k operations.

n= 5
a = [2,3,3,2,2]
b = [1,3,2,4,1]
k=2
To get the maximum number of distinct elements in array a:
• Select i = 2, j= 0. Swap a[2] and b[0] Now, a = [2,3,1,2,2] and b =
[3,3,2,4,1].
• Select i = 4, j= 3. Swap a[4] and b[3] Finally, a = [2,3,1,2,4] and b
= [3,3,2,2,1].
Now a = [2,3,1,2,4] contains 4 distinct elements. There can
never be more than 4 distinct elements in a.


STDIN
FUNCTION
n = 5
a = [1, 1, 4, 5, 5]
n = 5
b = [4, 4, 3, 1, 5]
Sample Output
4
Explanation
k = 2
• swap a[2] and b[3] -> a = [1,1,3,5,5] and b = [5,4,4,4,1].
• swap a[0]and b[1] -> a = [4,1,3,5,5] and b = [5,1,4,4,1].
"""
import collections
def getMaximumDistinctCount(a,b,k):
    aset = set(a)
    left = len(a) - len(aset)
    if not left:
        return len(a)
    else:
        canswap = set(b) - set(a)
        swapcnt = 0
        while k and swapcnt < left and canswap:
            canswap.pop()
            k -= 1
            swapcnt += 1
        return len(aset) + swapcnt

print(getMaximumDistinctCount([2,3,3,2,2], [1,3,2,4,1], 2))
print(getMaximumDistinctCount([1, 1, 4, 5, 5], [4, 4, 3, 1, 5], 2))
print(getMaximumDistinctCount([1,2, 3], [4, 5, 6], 5))
print(getMaximumDistinctCount([1], [4], 5))
print(getMaximumDistinctCount([1,1], [4,4], 5))
print(getMaximumDistinctCount([1,1,1], [4,4,4], 5))
print(getMaximumDistinctCount([1,1,1], [1,4,4], 5))
print(getMaximumDistinctCount([1,1,1], [2,4,4], 5))
print(getMaximumDistinctCount([1,1,1], [2,4,4], 1))




    



    
    



# def max_distinct_elements(a, b, k):
#     freq_a = {}
#     freq_b = {}
#     current_distinct = 0
    
#     # Calculate initial distinct elements in array a
#     for num in a:
#         if num not in freq_a:
#             freq_a[num] = 1
#             current_distinct += 1
#         else:
#             freq_a[num] += 1
    
#     max_distinct = current_distinct
    
#     # Iterate through array a and calculate potential distinct elements
#     for i in range(len(a)):
#         potential_distinct = current_distinct
        
#         if a[i] != b[i] and k > 0:
#             potential_distinct += 1
        
#         if freq_b.get(b[i], 0) < freq_a[a[i]]:
#             freq_b[b[i]] = freq_b.get(b[i], 0) + 1
#             potential_distinct -= 1
        
#         max_distinct = max(max_distinct, potential_distinct)
    
#     return max_distinct

# Example usage
# n = 5
# a = [2, 3, 3, 2, 2]
# b = [1, 3, 2, 4, 1]
# k = 2
# print(getMaximumDistinctCount([2, 3, 3, 2, 2], [1, 3, 2, 4, 1], 2))
# print(getMaximumDistinctCount([1,2, 3], [4, 5, 6], 5))
# print(getMaximumDistinctCount([1,1,3,5,5], [4,4,3,1,5], 2))
