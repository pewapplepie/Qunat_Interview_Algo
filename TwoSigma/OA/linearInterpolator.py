'''
1. Linear Interpolator
You are asked to implement a linear interpolator. Namely you are given n points on a 2-dimensional coordinate system (known as the knot points). When these points are sorted by their x coordinates and then connected together using straight lines (in their sorting order), they define a piecewise-linear function LI(x) known as the linear interpolation. When x is outside the range of all knot points, LI(x) is defined by extrapolation i.e. extending the straight line connecting its two nearest knot points.
You have to complete a function linear_interpolate(n: int, x_knots: List[float], y_knots: List[float], x_input: float) -> float where x_knots and y_knots give you x- and y-coordinate of knot points. Your function should return LI(x_input). Below is a graph of this calculation for Sample Case 0.
(-2, 0), (-1, 10), (0, 15), (1, 0), (2, 5)
Linear Interpolation
x_input: -0.3
output: 13.5

In case multiple knot points share the same x-coordinate x, when x_input <= x, we break the tie by using the smallest y-coordinate among those points. When x_input>x, we break the tie by using the largest y-coordinate among those points.
Further Notes
• 1 <n<= 100,000
• x_knots and y_knots are guaranteed to have the same length
• No guarantee that x_knots and y_knots are pre-sorted in any way
• For this question we expect an implementation "by hand." Please do not utilize a lib
has linear interpolation implemented.
• Floating-points numbers in all our tests have at most three decimal places (i.e. they are multiples of 0.001) so equality between them is unambiguous
1. friend circle num
2. longest strin‍‌‌‌‌‍‌‍‍‍‌‍‌‌‌‍‍‍‍‌g chain
3. game of life
'''

from typing import List
import bisect

def linear_interpolate(n: int, 
                       x_knots: List[float], 
                       y_knots: List[float], 
                       x_input:float):
    pts = zip(x_knots, y_knots)
    pts = sorted(pts)
    print(pts, f'and insert {x_input}')
    lp, rp = 0, n
    ans = 0
    while lp < rp:
        # mid = lp + (rp - lp)//2
        mid = (rp + lp)//2
        # print(lp, rp, 'mid is : ',mid, 'value is :', pts[mid][0])
        if pts[mid][0] >= x_input:
            rp = mid
        else:
            lp = mid + 1
    # print(f'choose index :  {lp - 1}')
    lp = lp - 1 if lp > 0 else lp
    # print(f'builtin index: {bisect.bisect_left(sorted(x_knots), x_input) - 1}')
    if pts[lp][0] == x_input:
        ans = pts[lp][1]
    else:
        xdist = x_input - pts[lp][0]
        if lp < n - 1:
            m = (pts[lp + 1][1]- pts[lp][1])/(pts[lp + 1][0] - pts[lp][0])
            ans = pts[lp][1] + xdist*m
            return ans
        if lp >= n - 1:
            m = (pts[lp + 1][1]- pts[lp][1])/(pts[lp + 1][0] - pts[lp][0])
            ans = pts[lp][1] + xdist*m
    return round(ans, 3)

test_case_0 = linear_interpolate(5, [-2, -1, 0, 1, 2], [0, 10, 15, 0, 5], -0.3) #Output 13.5
test_case_1 = linear_interpolate(5, [0, 2, 1, 3, 4], [0, 5, 2, 1, 8], 1.5) # 3.5
test_case_2 = linear_interpolate(4, [-1, 0, 1, 2], [3, 1, 4, 2], 0.5) #2.5
test_case_3 = linear_interpolate(6, [-3, -2, 0, 1, 3, 4], [4, 2, 1, 3, 6, 5], -1.5) # 1.75 
print('test 0 ',test_case_0)
print('test 1 ',test_case_1)
print('test 2 ',test_case_2)
print('test 3 ',test_case_3)
# print('testcase1', test_case_1)
# print(test_case_2)
# print(test_case_3)

