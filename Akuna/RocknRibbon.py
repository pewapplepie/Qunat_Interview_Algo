import collections
import heapq
def rockrobbin(ribbon_len, rocks):
    dist_calc = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    numbOfPoints, collection_dic = len(rocks), collections.defaultdict(list)
    ans, n = 0, len(rocks)
    seen = set()
    vertices = [(0, (0,0))]
    while len(seen) < n:
        w, (u, v) = heapq.heappop(vertices)            
        if v in seen or ans + w >= ribbon_len: 
            continue
        if ans + w <= ribbon_len:
            ans += w
        seen.add(v)
        for j in range(n):
            if j not in seen and j!=v:
                heapq.heappush(vertices, (dist_calc(rocks[j], rocks[v]), (v, j)))
    return ans

ribbonlen = 10
rocks = [[0,0],[3,0],[3,3]]
rockrobbin(ribbonlen, rocks)