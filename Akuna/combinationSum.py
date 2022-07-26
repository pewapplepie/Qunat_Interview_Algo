# n = 8, k = 4
# ans 5
# [1,1,1,5] [1,1,2,4] [1,1,3,3] [1,2,2,3] [2,2,2,2]
def combinationSum(target, numsOfel):
    def backtrack_sum(target, numsOfel, start, temp, res):
        if (len(temp) == numsOfel) & (target== 0):
            res.append(temp[:])

        elif((len(temp) < numsOfel) & (target>0)):

            for i in range(start, target+1):    
                temp.append(i)
                backtrack_sum(target - i, numsOfel, i, temp, res)
                temp.pop()

    res = []
    backtrack_sum(target, numsOfel, 1, [], res)
    return len(res), res

        
combinationSum(8, 4)
