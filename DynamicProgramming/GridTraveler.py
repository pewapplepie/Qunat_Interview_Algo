def gridTraveler(n, m, memoize={}):
    """
    Given grid wiht n row, m col. Starting from left top, return how many ways to travel
    to the right bottom. Each time only can move one grid (either down or right)
    """
    key = (n, m)
    if key in memoize:
        return memoize[key]
    elif key == (1, 1):
        return 1

    elif n == 0 or m == 0:
        return 0

    memoize[key] = gridTraveler(n-1, m, memoize) + \
        gridTraveler(n, m-1, memoize)
    return memoize[key]


# test case
print(gridTraveler(1, 1))  # 1
print(gridTraveler(2, 3))  # 3
print(gridTraveler(3, 2))  # 3
print(gridTraveler(3, 3))  # 6
print(gridTraveler(18, 18))  # 2333606220
