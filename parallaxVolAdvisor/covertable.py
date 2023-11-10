# A is a list of holes
# we need to use two boards to cover all holes
# the boards can be placed at any hole
# return the minimum length of the boards
def solution(A):
    # deal with edge cases
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
    # sort the list
    A.sort()
    # split the holes into two groups
    # so that in each group the difference between the largest and smallest hole is minimized
    diff = A[-1] - A[0]
    for i in range(len(A) - 1):
        diff = min(diff, max(A[i] - A[0], A[-1] - A[i + 1]))

    return diff


# create some test cases
A = [11, 20, 15]
print(solution(A))

A = [15, 20, 9, 11]
print(solution(A))

A = [0, 44, 32, 30, 42, 18, 34, 16, 35]
print(solution(A))

A = [9]
print(solution(A))