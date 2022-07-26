from math import sqrt
from itertools import count, islice
import enum
import math
from re import I
from tracemalloc import start

from black import diff


class Goldman:
    ##############################
    # LC.724
    def pivotIndex(self, nums):
        ttl = sum(nums)
        lsum = 0
        for idx, val in enumerate(nums):
            if lsum == (ttl - lsum - val):
                return idx
            lsum += val
        return -1

    def pivotIndexTest(self):
        assert self.pivotIndex([1, 7, 3, 6, 5, 6]) == 3, "Calculation Error"
        assert self.pivotIndex([1, 2, 3]) == -1, "Calculation Error"
        assert self.pivotIndex([-1, -1, 0, 0, -1, -1]
                               ) == 2, "Calculation Error"
        return "All Case Complete"
    ##############################
    # LC. 1041

    def isRobotBounded(instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R':
                dx, dy = dy, -dx
            if i == 'L':
                dx, dy = -dy, dx
            if i == 'G':
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)

    def isRobotBoundedTest(self):
        assert self.isRobotBounded('GGLLGG') == True, "Failed"  # true
        assert self.isRobotBounded('GG') == False, "Failed"  # false
        assert self.isRobotBounded('GL') == True, "Failed"  # true
        return "All Case Complete"
    ##############################
    # LC. 3

    def lengthOfLongestSubstring(self, s):
        seen = {}
        maxLen, start = 0, 0
        for idx, el in enumerate(s):
            if el in seen and start <= seen[el]:
                start = seen[el] + 1
            else:
                maxLen = max(maxLen, idx - start + 1)
            seen[el] = idx
        return maxLen

    ##############################
    # Longest K-interspace Substring
    def longestKSubstring(self, s, k):
        # def gap(a,b):
        #     return abs(ord(a) - ord(b))
        # temp,max="",""
        # for i in range(len(s)-1):
        #     temp+=s[i]
        #     if gap(s[i],s[i+1])>k:
        #         max=max if len(max)>len(temp) else temp
        #         temp=""
        # return max
        currSub = ''
        maxSub = ''
        currOrd = ord(s[0])
        for idx, val in enumerate(s):
            if abs(currOrd - ord(val)) <= k:
                currSub += val
            else:
                maxLen = max(maxLen, len(currSub))
                currSub = ''
                currOrd = ord(val)
        return
    ##############################
    # LC.829 Consecutive Sum

    def consecutiveSum(self, num):
        count = 0
        upperlimit = math.ceil((2*num + .25) ** .5 - 0.5) + 1
        for k in range(1, upperlimit):
            num -= k
            if num % k == 0:
                count += 1
        return count


def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

# Double on Match


def doubleOnMatch(arr, num):
    seen = {}
    for idx, el in enumerate(arr):
        seen[el] = idx
    while num in seen:
        num = num*2

    return num


doubleOnMatch([1, 2, 4, 11, 12, 8], 2)  # 16
doubleOnMatch([1, 2, 3, 1, 2], 1)  # 4
# Counting Analogous Array


def countingAnalogArr(diffs, lower, upper):
    start = lower
    countAnalog = 0
    for i in range(lower, upper+1):
        comb = [i]
        curr = i
        for el in (diffs):
            curr -= el
            if curr >= lower and curr <= upper:
                comb.append(curr)
            else:
                break
        if len(comb) == (len(diffs) + 1):
            countAnalog += 1

    return countAnalog


countingAnalogArr([-2, -1, -2, 5], 3, 10)  # 3


def firstNonRepeatingCharacter(string):
    # Write your code here.
    seen = {}
    for c in string:
        seen[c] = seen.get(c, 0) + 1
    for idx, c in enumerate(string):
        if seen[c] == 1:
            return idx
    return -1


firstNonRepeatingCharacter('faadabcbbebdf')


def runLengthEncoding(string):
    # Write your code here.
    seen = {}
    res = ""
    curr = string[0]
    countstr = 0
    for idx, c in enumerate(string):
        if c == curr:
            countstr += 1
            if countstr >= 10:
                res += str(countstr - 1)
                res += curr
                countstr = 1
            if idx == len(string) - 1:
                res += str(countstr)
                res += curr
            
        else:
            res += str(countstr)
            res += curr
            curr = c
            countstr = 1
            if idx == len(string) - 1:
                res += '1'
                res += c


    return res
runLengthEncoding('AAAAAAAAAAAAABBCCCCDD')


# def wordCompression(word, k):
#     seen = {}
#     for idx

#     return ret


def removeDuplicates(word, k):
    res = []
    for c in word:
        print(c)
        all_the_same = True
        if len(res) >= k-1:
            for i in range(k-1):
                all_the_same &= (res[-1-i] == c)
                print(all_the_same)

            if all_the_same:
                for i in range(k-1):
                    res.pop()
            else:
                res.append(c)
        else:
            res.append(c)
        print(res)
    return "".join(res)


word = 'abbcccb'
k = 3
removeDuplicates(word, k)
word = 'aba'
k = 2
removeDuplicates(word, k)

word = 'baac'
k = 2
removeDuplicates(word, k)

