"""
Paper Sheets
Description
Given a rectangular shape having dimensions h x w, where h is the height and w is the width, fold the shape so its dimensions are h1 x w1 in the minimum number of moves. 
The rectangle can only be folded parallel to its edges, and after folding, the dimensions should be integers.
Example
Given h = 8 and w = 4, fold the rectangle until it is (h1, w1) = (6, 1). 
First, fold along the long edge 6 units from a side, resulting in a
rectangle that is 6 x 4. Next, fold along the width 2 units from the 4 unit edge to have 6 x 2. 
Fold along the center of the 2 unit edge to achieve a 6 x 1 rectangle in three folds.
Function Description
Complete the function minMoves in the editor below.
minMoves has the following parameters:
int h: the initial height int w: athe initial width int h1: the final height int w1: the final width
Returns:
int: an integer that denotes the minimum number of moves in which the task can be achieved
"""
import math

def minMoves(h, w, h1, w1):
    if h < h1 or w < w1:
        return -1
    
    def fold(start, end):
        count = 0
        while start > end:
            if start /2 < end:
                start = end
            else:
                start = math.ceil(start/2)
            count += 1
        return count
    return fold(h, h1) + fold(w, w1)

print(minMoves(8, 4, 6, 1)) # 3
print(minMoves(10, 4, 7, 3)) # 2
print(minMoves(5, 5, 2, 5)) # 2
print(minMoves(6, 4, 3, 4)) # 1
print(minMoves(7, 6, 4, 4)) # 2
print(minMoves(10, 4, 2, 1)) # 5
# print(minMoves(7, 6, 4, 4)) # 4
# print(minMoves(8, 4, 5, 2)) # 5
# print(minMoves(8, 8, 7, 7)) # 4


def minMoves2(h, w, h1, w1):
# Write your code here
    def minFold(start, target):
        count = 0
        while start > target:
            count += 1
            start = start // 2 + int(start % 2 != 0)
        return count
    return minFold(h, h1) + minFold(w, w1)
print("="*10)
print(minMoves2(8, 4, 6, 1)) # 3
print(minMoves2(10, 4, 7, 3)) # 2
print(minMoves2(5, 5, 2, 5)) # 2
print(minMoves2(6, 4, 3, 4)) # 1
print(minMoves2(7, 6, 4, 4)) # 2
print(minMoves2(10, 4, 2, 1)) # 5


def sumBRV(n):
    bucks = [n/(i + 1) for i in range(n)]
    return sum(bucks)