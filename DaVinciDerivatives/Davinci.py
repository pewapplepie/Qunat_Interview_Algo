import numpy as np
import pandas as pd
from datetime import timedelta
from scipy import optimize


class Solution:
    def cln_df(self, df):
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['price'] = df['price'].astype(float)
        return df

    def findTtlProfit(self, c, M, stockA, stockB, sortedStock = False):
        idxA = 0
        idxB = 0
        profit = 0
        sortedStocks = pd.DataFrame(columns=stockB.columns)
        while idxA < len(stockA) and idxB < len(stockB):
            if idxA/1000 == idxA//1000:
                print("A",idxA,end=",")
            if idxB/1000 == idxB//1000:
                print("B",idxB,end=",")
            currTimeA = stockA.iloc[idxA]['timestamp']
            currTimeB = stockB.iloc[idxB]['timestamp']
            # print(idxA, idxB)
            if currTimeA == currTimeB:
                print('same!')
                idxA+=1
                idxB += 1
            elif currTimeA < currTimeB and idxA < len(stockA) - 1:
                sortedStocks.loc[idxA] = stockA.iloc[idxA,:]
                idxA += 1
                if (stockA.iloc[idxA, 1] - stockA.iloc[idxA - 1, 1]) >= c:
                    # print('hitA')
                    buyTime = stockA.iloc[idxA, 0] + timedelta(milliseconds=M)
                    profit += self.make_transaction(stockB,
                                                    idxB, buyTime, 'long')
                elif (stockA.iloc[idxA, 1] - stockA.iloc[idxA - 1, 1]) <= -c:
                    buyTime = stockA.iloc[idxA, 0] + timedelta(milliseconds=M)
                    profit += self.make_transaction(stockB,
                                                    idxB, buyTime, 'short')

            elif currTimeA > currTimeB and idxB < len(stockB) - 1:
                sortedStocks.loc[idxB] = stockB.iloc[idxB,:]
                idxB += 1
        if sortedStock == True:
            return profit, sortedStocks
        else:
            return profit

    def make_transaction(self, stock, currTime, buyTime, ls):
        if buyTime > stock.iloc[currTime, 0]:
            # check inbound
            if currTime > len(stock):
                return 0
            if ls == 'long':
                return - stock.iloc[currTime, 1] + stock.iloc[currTime + 1, 1]
            elif ls == 'short':
                return stock.iloc[currTime, 1] - stock.iloc[currTime + 1, 1]
        elif buyTime < stock.iloc[currTime, 0]:
            if ls == 'long':
                return stock.iloc[currTime + 1, 1] - stock.iloc[currTime, 1]
            elif ls == 'short':
                return stock.iloc[currTime, 1] - stock.iloc[currTime + 1, 1]
        

    def findLargestM(self, c, stockA, stockB):
        def f(x):
            return self.findTtlProfit(c, x, stockA, stockB) - 0
        try:
            largestM = optimize.newton(f, 80, maxiter=1000, tol=1e-2)
        except RuntimeError:
            pass
        try:
            largestM = optimize.newton(f, 100, maxiter=1000, tol=1e-2)
        except RuntimeError:
            pass
        try:
            largestM = optimize.newton(f, 500, maxiter=1000, tol=1e-2)
        except RuntimeError:
            pass
        try:
            largestM = optimize.newton(f, 1000, maxiter=1000, tol=1e-2)
        except RuntimeError:
            largestM = 0
        return largestM


if __name__ == "__main__":
    stockA = pd.read_csv('stockA.csv')
    stockB = pd.read_csv('stockB.csv')
    solution = Solution()
    stockA = solution.cln_df(stockA)
    stockB = solution.cln_df(stockB)
    c = 4
    M = 40
    profit = solution.findTtlProfit(c, M, stockA, stockB)
    print(profit)
    # 681.22129
    #largestM = solution.findLargestM(c, stockA, stockB)
    # couldnt finish
