import collections
import numpy as np
from typing import DefaultDict, Callable

class NumberGame:
    def __init__(self, maxround: int=1000) -> None:
        self.number_pair = set()
        self.max_round = maxround
        self.round = 0

    def _generate_numbers(self, n: int):
        for i in range(1, n):
            for j in range(i, n):
                self.number_pair.add((i, j))
        self.number_pair = sorted(self.number_pair)
        print("="*5, "generated item map", "="*5)

    def _process(self, ops: Callable):
        guyname = ops.__name__.upper()
        pairmap: DefaultDict = collections.defaultdict(list)
        for pair in self.number_pair:
            (a, b) = pair
            out = ops(a,b)
            pairmap[out].append(pair)
        
        rd_candidate = set()
        if self.round == self.max_round:
            for ps in pairmap.values():
                if len(ps) == 1:
                    rd_candidate.add(ps[0])
            if len(rd_candidate) >= 1:
                print(f'{guyname}: At last round {self.round}, I know the number: ', rd_candidate.pop())
            else:
                print(f'{guyname}: At last round {self.round}, I still dont know the number', rd_candidate)
            return True
        
        for k, ps in pairmap.items():
            if len(ps) == 1:
                candi = pairmap[k][0]
                rd_candidate.add(candi)
        for candi in rd_candidate:
            self.number_pair.remove(candi)

        if len(rd_candidate) == 1:
            print(f'{guyname}: {self.round} round, I could know the number: ', rd_candidate.pop())
            return True
        elif len(rd_candidate) > 1:
            print(f'{guyname}: {self.round} round, I dont know the number')
            return False
        print(f'{guyname}: {self.round} round, I dont know the number')
        return False

    def process_sum(self):
        self.round += 1
        def Sally(x, y):
            return x+y
        return self._process(Sally)

    def process_mul(self):
        self.round += 1
        def Peter(x, y):
            return x*y
        return self._process(Peter)

    def guess_number_game(self, n:int):
        self._generate_numbers(n)
        print("="*10,"start guessing ", "="*10)
        know_the_number = False
        while self.round < self.max_round:
            know_the_number = self.process_mul()
            if self.round == self.max_round:
                break
            know_the_number = self.process_sum()
        print('Check leftover', len(self.number_pair))

NumberGame(15).guess_number_game(100)