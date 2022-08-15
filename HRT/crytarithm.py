import collections
import functools
import itertools

class solution(object):
    def countSolvable(self, words, result):
        @functools.lru_cache(None)
        def helper(i, total, nums):

            if i == len(chars):
                return total == 0

            if i - 1 in checkpoints:
                t = str(abs(total))[::-1]
                for j in checkpoints[i-1]:
                    if (j < len(t)) and (t[j] != '0'):
                        return False

            for j in range(len(nums)):
                if (nums[j] == 0) and (chars[i] not in not_zero) and helper(i+1, total, nums[:j]+nums[j+1:]):
                    return True
                elif (nums[j] != 0) and helper(i+1, total + nums[j] * mult[chars[i]], nums[:j] + nums[j+1:]):
                    return True

            return False

        # 1. Check the lengths of each word and result
        longest_word = len(max(words, key = len))
        if (len(result) < longest_word) or (len(result) > longest_word + 1):
            return False

        # 2. Check if result is in words
        if result in words:
            return len(words) < 3 and all(word == result or len(word) == 1 for word in words)

        # 3. Leading letters cannot be zero unless the length of the word is 1
        not_zero = set((word[0] for word in words if len(word) > 1))
        if len(result) > 1: not_zero.add(result[0])

        # 4. Set of all letters
        chars = set(result + ''.join(words))

        # 5. Letters in words add to the total
        mult = {char:0 for char in chars}
        groups = collections.defaultdict(set)
        for word in words:
            for i,char in enumerate(reversed(word)):
                mult[char] += 10**i
                groups[i].add(char)

        # 6. And letters in result subtract from the total
        for i,char in enumerate(reversed(result)):
            mult[char] -= 10**i
            groups[i].add(char)

        # 7. Letters that add and subtract the same amount can be any number, so ignore them.
        chars = {char for char in chars if mult[char]}
        for g in groups:
            groups[g] = groups[g].intersection(chars)
        chars = list(chars)

        # 8. All letters that occur later in the word may affect letters ealrier in the word
        for g in range(1, len(groups)):
            groups[g] |= groups[g-1]
        chars.sort(key = lambda c: min(g for g in range(len(groups)) if c in groups[g]))

        # 9. Once a number has been assigned to all the letters in a group
        #    the digit in total at position 10**i must be zero for a solution to exist
        checkpoints = collections.defaultdict(list)
        seen = set()
        checked = set()
        for i,char in enumerate(chars):
            seen.add(char)
            for g in groups:
                if (g not in checked) and groups[g].issubset(seen):
                    checked.add(g)
                    checkpoints[i].append(g)

        return helper(0, 0, tuple(range(10)))
solution().countSolvable(["SEND","MORE"], "MONEY") # == 1
# solution().countSolvable(["GREEN","BLUE"], "BLACK") # == 12