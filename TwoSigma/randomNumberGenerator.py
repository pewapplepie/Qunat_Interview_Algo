import random
class randNumGen:
    def __init__(self, lowerbound, upperbound) -> None:
        self.lowerBound = lowerbound
        self.upperBound= upperbound
        self.map_lowerbound = lowerbound
        self.map_upperbound = upperbound
        self.map = {v:v for v in range(lowerbound, upperbound + 1)}
    
    def reset_range(self, lowerbound, upperbound):

        old_range = set(i for i in range(self.lowerBound, self.upperBound+1))
        new_range = set(i for i in range(lowerbound, upperbound+1))

        new_el = new_range.difference(old_range)
        new_el2 = new_range.intersection(set(self.map.values()))
        new_els = list(new_el.union(new_el2))

        self.map_lowerbound = lowerbound
        self.map_upperbound = lowerbound + len(new_els) - 1
        self.map = {k: new_els[k] for k in range(self.map_lowerbound, self.map_upperbound+1)}
        self.lowerBound = lowerbound
        self.upperBound = upperbound

    def reset(self):
        self.map_lowerbound = self.lowerBound
        self.map_upperbound = self.upperBound
        self.map = {v:v for v in range(self.map_lowerbound, self.map_upperbound+1)}

    def get_next(self):
        if self.map_lowerbound > self.map_upperbound:
            self.reset()
        
        k =  random.randint(self.map_lowerbound, self.map_upperbound)
        res = self.map.get(k, False)
        self.map[k] = self.map[self.map_upperbound]
        del self.map[self.map_upperbound]
        self.map_upperbound -= 1
        return res
    
randG = randNumGen(1, 100)
randG.get_next()