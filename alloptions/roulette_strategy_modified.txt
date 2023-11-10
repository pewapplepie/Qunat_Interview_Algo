import random

"""
roulette here we assume the roulette has 18 black, 18 red and 1 greeen
and it gives us 18/37 of winning probility of betting black
"""

BET = 10
TARGET_PROFIT = 20

def betting_black_with_budget(initial_budget):
    spin_results = ['r'] * 18 + ['b'] * 18 + ['g'] * 1
    current_bet = BET
    budget = initial_budget
    while budget >= current_bet and budget < initial_budget + TARGET_PROFIT:
        roll = random.choice(spin_results)

        if roll == 'r':
            budget += current_bet
            current_bet = BET
        else:
            budget -= current_bet
            current_bet *= 2
    return budget


def betting_black_infinite_budget():
    spin_results = ['r'] * 18 + ['b'] * 18 + ['g'] * 1
    current_bet = BET
    position = 0
    while position < TARGET_PROFIT:
        roll = random.choice(spin_results)
        if roll == 'r':
            position += current_bet
            current_bet = BET
        else:
            position -= current_bet
            current_bet *= 2
    return position 
    
def roulette_betting_w_budget_simulation(n_sim=100000):
    total = 0
    initial_budget = 100
    for _ in range(n_sim):
        total += betting_black_with_budget(initial_budget)
    
    ev = total / n_sim
    return ev

def roulette_betting_wo_budget_simulation(n_sim=100000):
    total = 0 
    for _ in range(n_sim):
        total += betting_black_infinite_budget()
    ev = total / n_sim
    return ev
    

print(f'Q1. Expected Value with 100€ budget: €{roulette_betting_w_budget_simulation():.3f}') # ~= 98.5
print(f'Q2. Expected Value with 100€ budget: €{roulette_betting_wo_budget_simulation()}') #= 20