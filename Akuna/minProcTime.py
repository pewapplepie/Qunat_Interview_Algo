def minCostTime(n, proce, task):
    task.sort()
    max_cost = 0
    i = 0
    
    while i < len(task):
        j = 0
        while(j <4):
            max_cost = max(task[i +j] + proce[n-1], max_cost)
            j += 1
        i += j 
        n -= 1
    return max_cost
processor = [8, 10]
tasks = [2,2,3,1,8,7,4,5]
minCostTime(2, processor, tasks)



    


