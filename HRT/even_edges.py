graph = [[False, True, False, False],
         [True, False, True, False],
         [False, True, False, True],
         [False, False, True, False]]

def addEven(graph):
    n, m = len(graph), len(graph[0])
    odd = 0
    odd_vertice = []
    for i in range(n):
        deg = sum(graph[i][j] for j in range(m))
        # for j in range(m):
        #     if graph[i][j] == True:
        #         deg += 1
        if deg % 2 == 1:
            odd += 1
            odd_vertice.append(i)
    if odd == 0:
        return True
    # elif odd == 2:

