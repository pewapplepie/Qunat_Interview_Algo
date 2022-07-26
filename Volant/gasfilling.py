from cmath import inf
from multiprocessing.connection import wait
from os import stat
from sqlalchemy import true


def solution2(A, X, Y, Z):
    waittime = [0 for _ in range(len(A))]
    stations = [X, Y, Z]
    occupied_time = [0, 0, 0]
    for idx, fuel in enumerate(A):
        canfill = False
        minidx = -1
        minoccupied = inf
        for i in range(3):
            if stations[i] >= fuel:
                canfill = True
                if occupied_time[i] < minoccupied:
                    minidx = i
                    minoccupied = occupied_time[i]

        if canfill:
            if idx == 0:
                waittime[idx] = occupied_time[minidx]
                occupied_time[minidx] = fuel

            else:
                currtime = waittime[idx - 1]

                if occupied_time[minidx] > currtime:
                    waittime[idx] = occupied_time[minidx]
                    occupied_time[minidx] += fuel
                else:
                    waittime[idx] = waittime[idx - 1]
                    occupied_time[minidx] += fuel

            stations[minidx] -= fuel

        if not canfill:
            return -1
    return max(waittime)


print(solution2([2, 8, 4, 3, 2], 7, 11, 3))
print(solution2([1, 2, 3, 4, 5, 6], 100, 5, 0))
print(solution2([5], 4, 0, 3))
