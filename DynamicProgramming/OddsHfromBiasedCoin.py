
from typing import List

# Probability of getting an odd number of heads if n biased coins are tossed once. the kth coin having probability of 1/(2k+1)


class Solution:
    def getOddsHeadNthTossed(self, nbiasedcoins: int) -> int:
        p_oddshead = [0 for i in range(nbiasedcoins)]
        p_oddshead[0] = 0
        for i in range(1, nbiasedcoins):
            p_oddshead[i] = p_oddshead[i-1] * \
                (1-1/(2*i+1)) + (1-p_oddshead[i-1])*(1/(2*i+1))
        return p_oddshead[-1]


# n = 20
# Ans = Solution()
# print(Ans.getOddsHeadNthTossed(20))
# print("analytical check:", (n/(2*n+1)))

powerlist = [i**2 for i in range(2, 13)]
power2list = [i for i in range(2, 13) if i & (i-1) == 0]
print(power2list)
