from audioop import add
from glob import glob
from inspect import trace
from math import comb
from operator import sub
from turtle import Turtle, left, st
from matplotlib.pyplot import step
from pandas import array


def minCoinFlip(coins):
    steps = min(
        sum(n == i % 2 for i, n in enumerate(coins)),
       sum(n == (i + 1) % 2 for i, n in enumerate(coins)), )
    return steps

minCoinFlip([1,0,1,0,1,1]) #2
minCoinFlip([1,0,1,1,1,1]) #2
minCoinFlip([1,1,0,1,1])#2
minCoinFlip([0,1,0])#0
minCoinFlip([0,1,1,0])#2
###############
def distinctedGenerator(N):
    odd = N % 2 == 1
    even = N % 2 == 0
    if even:
        return [x for x in range(1,N//2+1)] + [-x for x in range(1, N//2 + 1)]
    if odd:
        return [x for x in range(1, N//2+1)] +[0] + [-x for x in range(1, N//2 + 1)]

distinctedGenerator(4)
(distinctedGenerator(11))
###############
def crossValidation(indicies, K):
    even = len(indicies) % K == 0
    def get_train(arr, i, j):
        front = arr[:i]
        nxt = arr[j:]
        return front+nxt
    folds = []
    if even:
        step = len(indicies)//K
        i = 0
        while i < len(indicies):
            test = indicies[i:i + step]
            train = get_train(indicies, i, i+step)
            folds.append(train)
            folds.append(test)
            i += step
            
    else:
        step = len(indicies)//K
        additions = len(indicies)%K
        i = 0
        while i < len(indicies):
            if additions > 0:
                test = indicies[i:i+step + 1]
                train = get_train(indicies, i, i+step + 1)
                folds.append(train)
                folds.append(test)
                i += step + 1
                additions -= 1
            else:
                test = indicies[i:i+step]
                train = get_train(indicies, i, i+step)
                folds.append(train)
                folds.append(test)
                i += step

    return folds
crossValidation([1,2,3], 2)
crossValidation([1,2,3,4,5, 6,7,8], 3)
###############
def stringValidate(str):
    for i in range(1, len(str)):
        if str[i] == 'a' and str[i-1] == 'b':
            return False
    return True
stringValidate('aaabbb')
stringValidate('aaab')
###############
def findSubsetMax(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    P = 0
    Q = 0
    subset = dict()
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            Q = i
            if i == len(arr) - 1:
                subset[P] = Q - P + 1
        else:
            #print(Q, P)
            subset[P] = Q - P + 1
            P = i
            Q = i
    maxidx = max(subset, key=subset.get)
    #print(maxidx, subset[maxidx])
    return max(subset, key=subset.get)
findSubsetMax([2,2,2,2,1,2,-1,2,3,3])
findSubsetMax([2,2,1,2,-1,2,3,3])
findSubsetMax([2,1,2,-1,2,1,3,4])
findSubsetMax([2,1,2,3,-10,1,2,3])
findSubsetMax([30,20,10])
###############
def stephelper(int, step):
    if int == 0:
        return step
    else:
        odd = int % 2 == 1
        if odd:
            return stephelper(int-1, step + 1)
        else:
            return stephelper(int/2, step + 1)
def binarySteps(str):
    num = int(str, 2)
    return stephelper(num, 0)
binarySteps('011100')
###############
class VelocityCheck():
    def numbOfStableVel(self, arr) -> int:
        if len(arr) < 3:
            return 0
        stableCount = 0
        i = 1
        while i < len(arr): 
            stableLen = 0
            currVel = arr[i] - arr[i-1]    
            for j in range(i + 1, len(arr)):
                velocity = arr[j]  - arr[j - 1]
                if velocity != currVel:
                    break
                stableLen += 1
            if stableLen > 0:
                stableCount += stableLen*(stableLen+1)/2
                i += stableLen
            else:
                i += 1

        return stableCount

A = VelocityCheck()
A.numbOfStableVel([2,2,2,2]) #3
A.numbOfStableVel([-1,1,3,3,3,2,3,2,1,0]) #5
A.numbOfStableVel([2,2,2,2,2]) #6
bigarr = [2]*10000
A.numbOfStableVel(bigarr)
###############
def evenKSum(array, k):
    if k == len(array):
        return sum(array) if sum(array)%2 == 0 else -1
    if len(array) < k:
        return -1
    global maxEvenSum
    maxEvenSum = float('-inf')
    def dfs_helper(arr, combo, start, k):
        if k < 0:
            return
        if k == 0:
            currsum = sum(combo)
            if currsum % 2 == 0:
                global maxEvenSum
                maxEvenSum = max(maxEvenSum, currsum)
                return
        for i in range(start, len(arr)):
            combo.append(arr[i])
            dfs_helper(arr, combo, i + 1, k - 1)
            combo.pop()

    dfs_helper(array, [], 0, k)

    return maxEvenSum
evenKSum([4,9,8,2,6], 3)
# backtracking
def largest_even_sum(arr, k):
    if len(arr) < k: return -1
    global res
    res = float('-inf')
    def backtrack(level, start, k):
        if k < 0:
            return
        if k == 0 and not (lsum := sum(level)) & 1:
            global res
            res = max(res, lsum)
            return
        for i in range(start, len(arr)):
            level.append(arr[i])
            backtrack(level, i + 1, k - 1)
            level.pop()

    backtrack([], 0, k)
    return res
largest_even_sum([4,9,8,2,6], 3)

class Combinations:
    def combine(self, n: int, k: int) -> list:
        ret = []
        self.dfs_helper(n+1, ret, [], 1, k)
        return ret
    
    def dfs_helper(self, n, ret, combo, start, k):
        if k < 0:
            return 
        if k == 0:
            print(combo)
            ret.append(combo)
            return
        else:
            for i in range(start, n):
                #combo.append(i)
                self.dfs_helper(n, ret, combo + [i], i+1, k-1)
                #combo.pop()
comb = Combinations()
comb.combine(4,2)