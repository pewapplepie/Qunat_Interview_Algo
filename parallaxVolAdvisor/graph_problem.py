"""
You are given an undirected graph consisting of N vertices, numbered from 1 to N, and M edges.
The graph is described by two arrays, A and B, both of length M. A pair (A[K], B[K), for K from 0 to M-1, 
describes an edge between vertex A[K] and vertex B[K].
Your task is to check whether the given graph contains a path from vertex 1 to vertex N going through all of the vertices, 
one by one, in increasing order of their numbers. All connections on the path should be direct.

Write a function:
def solution (N, A, B)
that, given an integer N and two arrays A and B of M integers each, 
returns True if there exists a path from vertex 1 to N going through all vertices, one by one, in increasing order, or
False otherwise.

1. Given N = 4, A = [1, 2, 4, 4, 3] and B = [2, 3, 1, 3, 1], the function should return True. 
There is a path (1 - 2 - 3 - 4) using edges (1, 2), (2, 3) and (4, 3).

2. Given N = 4, A = (1, 2, 1, 3] and B = [2, 4, 3, 4], the function should return False. 
There is no path (1 - 2 - 3 - 4), as there is no direct connection from vertex 2 to vertex 3.
"""

import collections


def solution(N, A, B):
    graph = collections.defaultdict(list)
    for n1, n2 in zip(A, B):
        graph[n1].append(n2)
        graph[n2].append(n1)
    que = collections.deque([1])
    visited = set()
    node = None
    while que:
        node = que.popleft()
        visited.add(node)
        for nei in graph[node]:
            if nei == node + 1 and nei not in visited:
                que.append(nei)
    return node == N

print(solution(4, [1,2,4,4,3], [2,3,1,3,1]))
print(solution(4, [1,2,1,3], [2,4,3,4]))
print(solution(6, [2,4,5,3], [3,5,6,4]))
print(solution(3, [1,3], [2,2]))