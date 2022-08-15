import collections
import functools
import itertools
from typing import List
class Solution:
    def countSolvable(self, words: List[str], result: str) -> bool:
        self.count = 0
        allWords = words + [result]
        firstChars = set(word[0] for word in allWords if len(word) > 1)
        n = max(map(len, allWords))
        if len(result) < n: return False
        def dfs(charIdx, wordIdx, carry, visited, char2digit):
            if charIdx == n: return carry == 0
            if wordIdx == len(allWords):
                # time to check the final status for the current digit
                sums = sum(char2digit[word[-charIdx - 1]] if charIdx < len(word) else 0 for word in words) + carry
                if sums % 10 == char2digit[result[-charIdx - 1]]:
                    return dfs(charIdx + 1, 0, sums // 10, visited, char2digit)
                else:
                    return False # prune. To support this, using -charIdx - 1 to visit from right/low to left/high
            # current word length is too short to check, move to check next word
            if wordIdx < len(words) and charIdx >= len(words[wordIdx]):
                return dfs(charIdx, wordIdx + 1, carry, visited, char2digit)

            c = allWords[wordIdx][-charIdx-1]
            if c in char2digit:
                # if current word's current char already map to a digit, continue with next word
                return dfs(charIdx, wordIdx + 1, carry, visited, char2digit)
            else:
                # otherwise try all possibilities via dfs
                firstDigit = 1 if c in firstChars else 0
                for digit in range(firstDigit, 10):
                    if digit not in visited:
                        visited.add(digit)
                        char2digit[c] = digit
                        if dfs(charIdx, wordIdx + 1, carry, visited, char2digit.copy()): 
                            # return True
                            self.count += 1
                            return
                        visited.remove(digit) # restore visited and char2digit by discarding the copy
                return False
        aa =  {}
        dfs(0, 0, 0, set(), aa)
        print(aa)
        return self.count
# Solution().countSolvable(["SEND","MORE"], "MONEY") # == 1
Solution().countSolvable(["GREEN","BLUE"], "BLACK") # == 12