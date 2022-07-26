from sympy import subsets


def powerset(array):
    subsets = [[]]
    for el in array:
        for i in range(len(subsets)):
            currSubset = subsets[i]
            print(currSubset + [el])
            subsets.append(currSubset + [el])
        
    return subsets