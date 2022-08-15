

def solution(l, t):
    currsum = 0
    start = 0
    for idx, n in enumerate(l):
        currsum += n
        if currsum == t:
            return [start, idx]
        while currsum > t and start <= idx:
            currsum -= l[start]
            start += 1
    return [-1, -1]

