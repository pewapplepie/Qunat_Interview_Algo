from numpy import roll


def dicegame(rolls):
    if rolls == 1:
        return 3.5
    payoff = [0] * (rolls )
    payoff[-1] = 3.5
    for i in range(rolls-2, -1, -1):
        #print(i, 'hi')
        payoff[i] = payoff_dice(payoff[i+1])
    return payoff[0]

def payoff_dice(curr_ev):
    ret = 0
    for i in range(1, 7):
        if curr_ev < i:
            ret += 1/6*(i)
        else:
            ret += 1/6*(curr_ev)
    return ret

dicegame(2)
dicegame(3)