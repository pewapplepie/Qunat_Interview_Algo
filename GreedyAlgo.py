from dis import dis


def validStartingCity(distances, fuel, mpg):

    # Write your code here.
    N_city = len(distances)
    for i in range(len(distances)):
        j = i
        myfuel = 0
        total_dist = sum(distances)
        print('current',i)
        while total_dist > 0:
            j = j % N_city 
            myfuel += fuel[j]
            cango = myfuel*mpg
            if cango < distances[j]:
                print('break',j)
                break
            total_dist -= distances[j]
            myfuel -= distances[j]/10
            j += 1
        print('dist left',total_dist)
        if total_dist == 0:
            return i

    return -1


test1 = {
    "distances": [5, 25, 15, 10, 15],
    "fuel": [1, 2, 1, 0, 3],
    "mpg": 10
}
test2 = {
  "distances": [10, 20, 10, 15, 5, 15, 25],
  "fuel": [0, 2, 1, 0, 0, 1, 1],
  "mpg": 20
}
# validStartingCity(test1["distances"],
#                   test1["fuel"],
#                   test1["mpg"])
validStartingCity(
    test2["distances"],
    test2["fuel"],
    test2["mpg"]
)