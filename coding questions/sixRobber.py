def splittingGold(num):
    return num -  (num-1)/5 - 1
def findOriginal(guessing, splitting_time):
    remain = guessing
    while(splitting_time >= 0):
        left = splittingGold(remain)
        remain = left
        splitting_time -= 1
    #print('remain gold', remain,'\nwith extra',remain%6)
    return remain%5
# for i in range(500):
#     splittingGold(i,2)