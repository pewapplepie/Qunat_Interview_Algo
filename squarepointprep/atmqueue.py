"""
Queue at ATM
Given an integer array amount of length n. Each amount[i] represents the amount of money required by the person i. 
There are n people numbered 1 through n standing in an ATM queue in increasing order. 
A person can withdraw at most k units of currency at one time. 
Return an array of people numbers in the order that they leave the queue, i.e. the order their needed amounts have been withdrawn.

coding 题是给定一个amount 序列比如[2,5,3,10] 是每个人要在ATM取的amount，但每次的最大可取amount为k，
比如如果k = 2那么第一个人可以顺利取完，但第二个人会剩下5-2 = 3 dollar需要留到下一次再取，这时候第二个人就会排到队尾重新排队。
最后要求的是所有人取完钱的顺序的list
"""

import heapq

def ATMQueue(amount, k):
    arr = []
    for i in range(len(amount)):
        print(amount[i],amount[i]+k-1)
        arr.append([(amount[i]) // k, i + 1])
 
    print(arr)
    arr.sort()
    arr2 = [x[1] for x in arr]
    return arr2

print(ATMQueue([2, 5, 1], 3)) #[1, 3, 2]
# print(ATMQueue([6, 1, 2, 3, 2, 7], 2)) #[2,3,5,4,1,6]