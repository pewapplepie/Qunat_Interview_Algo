from cgitb import reset
import collections
from distutils.command.build_scripts import first_line_re
import functools
import itertools
from os import stat
import re
from typing import List
class Solution:
    def countSolvable(self,word1: str, word2: str, result: str):
        cnt = 0
        for sol in self.faster_solve(word1, word2, result):
            print(sol)
            cnt += 1
        return cnt

    def faster_solve(self, word1: str, word2: str, result: str):
        """Given a formula like 'NUM + BER == PLAY', fill in digits to solve it.
        This version precompiles the formula and generates all digit-filled-in strings."""
        fn, letters = self.compile_formula(word1, word2, result)
        formula = word1 + '+' + word2 + '=' + result
        cat = ''.join
        for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
            try:
                if fn(*digits):
                    yield formula.translate(str.maketrans(letters, cat(map(str, digits))))
            except ArithmeticError: 
                pass
    def complie_formula(self, word1: str, word2: str, result: str) -> bool:
        # allWords = words + [result]
        # letters = set()
        letters = ''.join(set(itertools.chain(result, word1, word2)))
        initial_letters = sorted(set([word1[0], word2[0],
         result[0]]))
        # print(initial_letters)
        formula = word1 + '+' + word2 + '=' + result
        body = re.sub('[A-Z]+', self.compile_word, formula)
        body         = ' and '.join(initial_letters + [body])
        fn = 'lambda {}: {}'.format(','.join(letters), body)
        return eval(fn), letters
        # print(letters)
        # formula = words[0]
        # for digits in itertools.permutations('1234567890', len(letters)):
        #     print(digits)
    def compile_word(self, matchobj):
        "Compile the word 'YOU' as '(100*Y + 10*O + U)'."
        word = matchobj.group()
        terms = reversed([self.mult(10**i, L) for (i, L) in enumerate(reversed(word))])
        return '(' + '+'.join(terms) + ')'

    def mult(factor, var): 
        return var if factor == 1 else str(factor) + '*' + var
# Solution().countSolvable(["SEND","MORE"], "MONEY") # == 1
Solution().countSolvable("GREEN","BLUE", "BLACK") # == 12

# def compile_formula(formula, verbose=False):
#     """Compile formula into a function.   Also return letters found, as a str,
#     in same order as parms of function. For example, 'YOU == ME**2' returns
#     (lambda E,M,O,U,Y: M and Y and ((100*Y+10*O+U) == (10*M+E)**2), 'YMEUO'"""
#     formula      = formula.replace(' = ', ' == ')
#     letters      = cat(sorted(set(re.findall('[A-Z]', formula))))
#     firstletters = sorted(set(re.findall(r'\b([A-Z])[A-Z]', formula)))
#     print(letters, firstletters)
#     body         = re.sub('[A-Z]+', compile_word, formula)
#     # print(body)
#     body         = ' and '.join(firstletters + [body])
#     fn = 'lambda {}: {}'.format(','.join(letters), body)
    
    # if verbose: print(fn)
    # assert len(letters) <= 10
    # return eval(fn), letters



# cat = ''.join # Function to concatenate strings
    
# leading_zero = re.compile(r'\b0[0-9]').search # Function to check for illegal number