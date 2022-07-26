from sympy import denom


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    numOfCoins = [float('inf')]*(n+1)
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(
                    numOfCoins[amount], numOfCoins[amount - denom] + 1)

    return numOfCoins[n] if numOfCoins[n] != 0 else -1


n = 7
denoms = [1]
minNumberOfCoinsForChange(n, denoms)
