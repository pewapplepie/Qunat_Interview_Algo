import collections
from unicodedata import name

def bestAvgGrade(allgrades):
    name_d = collections.defaultdict(list)
    
    for el in allgrades:
        name_d[el[0]].append(el[1])
    
    lastlen = 0
    lastsum = 0
    runningAvg = 0
    bestAvg = 0
    for k, val in name_d.items():
        val = [float(x) for x in val]
        currAvg = sum(val)/len(val)
        runningAvg = max(currAvg, (sum(val) + lastsum)/(len(val) + lastlen))
        bestAvg = max(bestAvg, runningAvg)
        
        lastlen = len(val)
        lastsum = sum(val)
     
    return bestAvg


input = [["Bob","87"], ["Mike", "35"],["Bob", "52"], ["Jason","35"], ["Mike", "55"], ["Jessica", "99"]]
input2 = [["Bobby","87"],["Charles", "100"],["Eric","64"],["Charles","22"]]
bestAvgGrade(input)
bestAvgGrade(input2)
