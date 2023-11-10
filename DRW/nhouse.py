import bisect
def solution(houses, x, y):
    houses.sort()
    n = len(houses)
    for i in range(1, n):
        houses[i] += houses[i - 1]
    res = float('inf')
    for i in range(n, -1, -1):
        last = houses[n-1] if i != n else 0
        remain = houses[i-1] if i != 0 else 0
        extra = last - remain
        l = -1
        r = i - 1
        while l < r:
            m = (l + r + 1) // 2
            if houses[m] <= extra:
                l = m
            else:
                r = m - 1
        # l = bisect.bisect_left(houses[:i-1], extra)
        res = min(res, ((n - i) * y) + ((i - l - 1) * x))
    return res
print(solution([5,3,8,3,2], 2, 5)) #7
print(solution([4,2,7], 4, 100)) #12