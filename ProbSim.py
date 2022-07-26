import random
import numpy as np
import matplotlib.pyplot as plt 
def dice():
    return random.randint(1,6)
def dice_sim(n):
    sim = []
    i = 0
    while i < n:
        Z = dice() + dice() + dice() + dice()
        sim.append(Z)
        i += 1
    return sim
dice_dist = dice_sim(10000)
def prob_dice(arr):
    count = 0
    for el in arr:
        if el == 8:
            count += 1
        elif el == 16:
            count += 1
        elif el == 24:
            count += 1
        else:
            pass
    return count