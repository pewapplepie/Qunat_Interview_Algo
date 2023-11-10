"""
Each day, to enter their building, employees of an e-commerce company have to type a string of numbers into a console using a 3 x 3 numeric keypad. Every day, the numbers on the keypad are mixed up.
Use the following rules to calculate the total amount of time it takes to type a string:
• It takes 0 seconds to move their finger to the first key, and it takes 0 seconds to press the key where their finger is located any number of times.
• They can move their finger from one location to any adjacent key in one second. Adjacent keys include those on a diagonal.
• Moving to a non-adjacent key is done as a series of moves to adjacent keys.

This diagram depicts the minimum amount of time it takes to move from the current location to all other locations on the keypad.
Function Description
Complete the function entryTime in the editor below.
entryTime has the following parameter(s):
string s: the string to type
string keypad: a string of 9 digits where each group of 3 digits represents a row on the keypad of the day, in order 
Returns:
int: integer denoting the minimum amount of time it takes to type the string s.

Constraints
• 1 <= |s| <= 10^5
• | keypad | = 9
• keypad[i] є [1-9]

v Sample Case O
STDIN
Function Parameters
string s = "423692"
string keypad = "923857614"
Sample Output 0
8

Calculate the time it takes to type s = 423692 as follows:
• 4: Start here, so it takes 0 seconds.
• 2: It takes 2 seconds to move from 4 - 2
3: It takes 1 second to move from 2 - 3
6: It takes 2 seconds to move from 3 - 6
9. It takes 2 seconds to move from 6 - 9
• 2. It takes 1 second to move from 9 - 2
The total time is 2 + 1 + 2 + 2 + 1 = 8.
"""

def entryTime(s, keypad):
    keyidmap = {}
    idx = 0
    for i in range(3):
        for j in range(3):
            keyidmap[keypad[idx]] = (i, j)
            idx += 1

    start = s[0]
    ttl = 0
    for ch in s[1:]:
        currx, curry = keyidmap[ch]
        prevx, prevy= keyidmap[start]
        t = max(abs(prevx - currx), abs(prevy - curry))
        print('time is {}'.format(t), ', from {0} to {1}'.format(start, ch))
        start = ch
        ttl += t
    return ttl


print(entryTime('423692', '923857614'))
print(entryTime('512', '123456789'))
print(entryTime('519', '123456789'))