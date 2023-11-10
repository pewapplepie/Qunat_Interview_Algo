from heapq import heappop, heappush
def getResult(arrival, direction):

    ascending = []
    descending = []

    lastpass = None
    for i, eta in enumerate(arrival):
        if direction[i] == 1:
            heappush(ascending, (eta, i))
        else:
            heappush(descending, (eta, i))
            lastpass = 1
    
    # ans = [0] * len(arrival)
    time = 0
    ans = {}
    while len(ans) < len(arrival):
        # if descending and (lastpass is None or lastpass == 0) and descending[0][0] <= ascending[0][0]:
        if not lastpass:
            if descending and ascending and descending[0][0] <= ascending[0][0]:
                eta, i = heappop(descending)
                ans[i] = eta
                lastpass = 1
                time = eta
            elif descending and ascending and descending[0][0] > ascending[0][0]:
                eta, i = heappop(ascending)
                ans[i] = eta
                lastpass = 0
                time = eta
            elif ascending:
                eta, i = heappop(ascending)
                ans[i] = eta
                lastpass = 0 
                time = eta
            else:
                eta, i = heappop(descending)
                ans[i] = eta
                lastpass = 1
                time = eta
            continue

        elif lastpass == 1:
            if descending and descending[0][0] <= time:
                eta, idx = heappop(descending)
                ans[idx] = eta
                lastpass = 1
            elif not descending:
                lastpass = 0
            else:
                lastpass = None
                time += 1
        else:
            if ascending and ascending[0][0] <= time:
                eta, idx = heappop(ascending)
                ans[idx] = eta 
                lastpass = 0
            elif not ascending:
                lastpass = 1
            else:
                lastpass = None
                time += 1
    
    res = [ans[i] for i in range(len(arrival))]

    return res



    

print(getResult([0,0,1,4],[0,1,1,0])) #[2,0,1,4]
print(getResult([0,1,1,3,3],[0,1,0,0,1])) #[0,2,1,4,3]