'''
2. Design a calculator that the user can define its own operators instead of + - * /
The second interviewer ask me one question:
There are two functions in this API:. check 1point3acres for more.
Set(string s, int m)
Sample(). 
Here is the example:
Set('a',1)// We set the string 'a' with weight 1.
Then if we do sample(), we will always return 'a'
Then if we
Set('b',2)//We set the string 'b' with weight 2.
Then if we sample it, there is 1/3 probability that it will return 'a' and 2/3 probability that it will return b.
If I set(“c”,3) and then sample there is 1/6 that it return a and 1/3 it return b and ½ it return c.
If I again set('a',2) and the I sample there is 2/7 that it return a and 3/7 that it return b and 2/7 that it return c.
Design an API to solve this problem
'''

import random
class API:
    def __init__(self) -> None:
        self.weights = []
        self.ttl_weights = 0

    def set(self, element, wei):
        if wei <= 0:
            raise ValueError
        self.ttl_weights += wei
        self.weights.append((self.ttl_weights, element))

    def sample(self):
        rand_n = random.randint(1, self.ttl_weights)
        lp, rp = 0, len(self.weights)
        while lp < rp:
            mid = lp + (rp - lp)//2
            if rand_n > self.weights[mid][0]:
                lp = mid + 1
            else:
                rp = mid
        
        return self.weights[lp][1]
import collections
# def test_1():
#     calc = Calculator()
#     calc.set('a', 1)
#     calc.set('b', 2)
#     testing = [calc.sample() for _ in range(1000)]
#     print(testing.count('a')/1000, 1/3)
#     print(testing.count('b')/1000, 2/3)

import unittest
from random import randint
def ttt():
    api = API()
    api.set('a', 1)
    api.set('b', 2)
    api.set('c', 3)
    samples = []
    for i in range(10000):
        samples.append(api.sample())
    print(f'a : {samples.count("a")}| b : {samples.count("b")} | c :{samples.count("c")}')
    print(f'a : {samples.count("a")/10000}| b : {samples.count("b")/10000} | c :{samples.count("c")/10000}')
    print(f'a : {1/6} | a: {2/6} | c: {3/6}')

def tt2():
    api = API()
    api.set('a', 1)
    api.set('b', 2)
    api.set('c', 3)
    api.set('a', 3)
    samples = []
    for i in range(10000):
        samples.append(api.sample())
    print(f'a : {samples.count("a")}| b : {samples.count("b")} | c :{samples.count("c")}')
    print(f'a : {samples.count("a")/10000}| b : {samples.count("b")/10000} | c :{samples.count("c")/10000}')
    print(f'a : {4/9} | a: {2/9} | c: {3/9}')
ttt()
tt2()
        
class TestAPI(unittest.TestCase):
    def test_set(self):
        api = API()
        api.set('a', 1)
        api.set('b', 2)
        api.set('c', 3)
        samples = []
        for i in range(10000):
            samples.append(api.sample())
        self.assertGreater(samples.count('b'), samples.count('a'))
        self.assertGreater(samples.count('c'), samples.count('b'))
        
    def test_set_and_sample(self):
        api = API()
        api.set('a', 1)
        api.set('b', 2)
        api.set('c', 3)
        api.set('a', 2)
        samples = []
        for i in range(10000):
            samples.append(api.sample())
        self.assertGreater(samples.count('a'), samples.count('b'))
        self.assertGreater(samples.count('c'), samples.count('b'))
        
    def test_set_with_negative_weight(self):
        api = API()
        with self.assertRaises(ValueError):
            api.set('a', -1)
            
    def test_set_with_zero_weight(self):
        api = API()
        with self.assertRaises(ValueError):
            api.set('a', 0)
            
    def test_sample_with_no_weights_set(self):
        api = API()
        with self.assertRaises(ValueError):
            api.sample()
            
# if __name__ == '__main__':
#     unittest.main()
 