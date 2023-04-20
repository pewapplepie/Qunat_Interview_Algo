# from math import factorial
def stringpatter(wordlen, maxVowels):
    mod = 1000000007
    memo = [[[0 for _ in range(2)] for _ in range(maxVowels+1)] for _ in range(wordlen+1)]

    def solve_recursively(word_len, vowels, char_type, memo):
        if vowels < 0 or word_len < 0:
            return 0
        v = 21 if char_type == 1 else 5
        if word_len == 0:
            return v
        if memo[word_len][vowels][char_type] != 0:
            return memo[word_len][vowels][char_type]
        res = 0
        if vowels == 0:
            res1 = solve_recursively(word_len - 1, maxVowels, 1, memo)
            res = (res1 * v) % mod
        else:
            res1 = solve_recursively(word_len - 1, vowels, 1, memo)
            res2 = solve_recursively(word_len - 1, vowels - 1, 0, memo)
            res = ((res1 + res2) % mod) * v % mod
        memo[word_len][vowels][char_type] = res
        return res
    return (solve_recursively(wordlen - 1, maxVowels, 1, memo) + solve_recursively(wordlen - 1, maxVowels - 1, 0, memo)) % mod

from functools import lru_cache
from collections import deque

class Item:
    def __init__(self, length, num_vowels, count):
        self.length = length
        self.num_vowels = num_vowels
        self.count = count

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.length == other.length and self.num_vowels == other.num_vowels
        return False

    def __hash__(self):
        return hash((self.length, self.num_vowels))

def solveWithBFS(wordLen, maxVowels):
    if wordLen == 0:
        return 0

    mod = 1000000007
    q = deque()
    q.append(Item(1, 0, 21))
    if maxVowels > 0:
        q.append(Item(1, 1, 5))

    for l in range(1, wordLen+1):
        qs = len(q)
        m = {}
        while qs > 0:
            item = q.popleft()
            count = 0
            if item.num_vowels + 1 <= maxVowels:
                count = (item.count * 21) % mod
                next_item = Item(item.length + 1, item.num_vowels, count)
                if next_item not in m:
                    m[next_item] = next_item
                    q.append(next_item)
                else:
                    m[next_item].count = (m[next_item].count + count) % mod
                count = (item.count * 5) % mod
                next_item = Item(item.length + 1, item.num_vowels + 1, count)
                if next_item not in m:
                    m[next_item] = next_item
                    q.append(next_item)
                else:
                    m[next_item].count = (m[next_item].count + count) % mod
            else:
                count = (item.count * 21) % mod
                next_item = Item(item.length + 1, 0, count)
                if next_item not in m:
                    m[next_item] = next_item
                    q.append(next_item)
                else:
                    m[next_item].count = (m[next_item].count + count) % mod
            qs -= 1

    ans = 0
    while q:
        ans = (ans + q.popleft().count) % mod

    return ans
# 21,5,828001349
# 37, 20, 589194521
# print(StringPattern().getNumOfUniqueWords(37, 20))
print(solveWithBFS(37, 20))
# stringpatter(wordlen=4, maxVowels=1)
# def getMaxBarrier(initialEnegy, th):
#     lp = 0
#     rp = max(initialEnegy)
#     def finalEnergy(barrier):
#         valid_energy = [eng-barrier for eng in initialEnegy if eng-barrier > 0]
#         return sum(valid_energy)
        
#     while lp < rp:
#         mid = lp + (rp - lp)//2
#         if finalEnergy(mid) > th:
#             lp = mid + 1
#         else:
#             rp = mid
#     return lp - 1


# print(getMaxBarrier([5,2,13,10], 8)) # 7
# print(getMaxBarrier([3,9,7,6], 6)) #5
# print(getMaxBarrier([4,8,7,1,2], 9)) #3