import math
import sympy
from fractions import Fraction
def simpleMarkovConsectiveDraw(p):
    x = sympy.Symbol('x')
    eq = p*(1 + p + (1-p)*(1+x)) + (1-p)*(1+x)
    sol = sympy.solveset(sympy.Eq(eq, x))
    return Fraction(float(sol.args[0])).limit_denominator()
    
print(simpleMarkovConsectiveDraw(2/5))
# print(simpleMarkovConsectiveDraw(5/8), 104/25)
# print(check_fracto_solution(5/8))

def meeting_question(t1, t2):
    total = 60*60
    t1A = 1/2*(60-t1)**2
    t2A = 1/2*(60-t2)**2
    meet = total - t1A - t2A
    print('meeting area: ', meet)

    return Fraction(float(meet/total)).limit_denominator()

print(meeting_question(12, 48))
print(meeting_question(10, 30))


# def three_coin_one_bias_problem(p, headn):

def distance_rate_problem(p1, p2, v1, v2, disrate):

