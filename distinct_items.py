# 3, [2,0,1,2], [8,7,6,9] -> 21
# 2, [0,1,0,1,1] [4,74,47,744,7] -> 11

# aacbd -> aabcd
import collections


def minCost(numproj, projid, bid):
    if len(set(projid)) != numproj:
        return -1
    seen = {}
    for idx, b in enumerate(bid):
        if projid[idx] not in seen:
            seen[projid[idx]] = b
        else:
            if b < seen[projid[idx]]:
                seen[projid[idx]] = b
    mincost = sum(seen.values())
    return mincost

# minCost(3, [2,0,1,2], [8,7,6,9])
minCost(2, [0,1,0,1,1], [4,74,47,744,7])
