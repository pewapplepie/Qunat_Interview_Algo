from struct import pack


def selectPackages(truckSpace, packageSpace):
    target = truckSpace - 30
    seen = {}
    allpair = {}
    ismax = 0
    for i in range(len(packageSpace)):
        potential = target - packageSpace[i]
        if potential in seen:
            currmax = potential if potential > packageSpace[i] else packageSpace[i]
            ismax = max(currmax, ismax)
            allpair[currmax] = [seen[potential], i]
        else:
            seen[packageSpace[i]] = i
    return allpair[ismax] if len(allpair) != 0 else [-1, -1]

truckSpace = 90
packageSpace = [1,10,25,35,60]
selectPackages(truckSpace, packageSpace)

# def minimizeCost(connections):
#     connected = {}
#     for connect in connections:
#         for el in connect:
