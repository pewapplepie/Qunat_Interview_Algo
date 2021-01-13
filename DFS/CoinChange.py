from typing import Callable, Dict, List, Tuple


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0 for i in range(amount+1)]
        ways[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if coin <= i:
                    ways[i] += ways[i - coin]
        return ways[amount]


Ans = Solution()
print(Ans.change(5, [1, 2, 5]))
print(Ans.change(500, [3, 5, 7, 8, 9, 10, 11]))
