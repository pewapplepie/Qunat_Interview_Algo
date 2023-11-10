"""
Each character of the lowercase English alphabet has been mapped to digits as shown in the figure. 
The numerical value corresponding to each letter is its mapped value.
1 . 2 . 3
ab. cde. fgh
4 . 5 . 6 . 
ijk. lmn. opq
7 . 8 . 9 . 
rst. uvw. xyz
An extraordinary substring is one whose sum of the mapped values of each letter is divisible by its length. 
Given string input_str, count its total number of non-empty extraordinary substrings.

input_str = 'asdf'
All non-empty substrings of input_str are tested in the table.
+------------+---------+-----+--------+--------------+
| String     | Mapped  | Sum | Length | Is divisible |
+------------+---------+-----+--------+--------------+
| a          | 1       | 1   |   1    |     Yes      |
| s          | 7       | 7   |   1    |     Yes      |
| d          | 2       | 2   |   1    |     Yes      |
| f          | 3       | 3   |   1    |     Yes      |
| as         | 1,7     | 8   |   2    |     Yes      |
| sd         | 7,2     | 9   |   2    |      No      |
| df         | 2,3     | 5   |   2    |      No      |
| asd        | 1,7,2   | 10  |   3    |      No      |
| sdf        | 7,2,3   | 12  |   3    |     Yes      |
| asdf       | 1,7,2,3 | 13  |   4    |      No      |
+------------+---------+-----+--------+--------------+

There are 6 extraordinary substrings.

Function Description
Complete the function countSubstrings in the editor.
countSubstrings has the following parameter(s):
string input_str: a string of length n
Returns
int: the number of non-empty extraordinary substrings
Constraints
• 1 ≤ n ≤ 2000
• All characters of input_str are lowercase English letters.

Sample Input For Custom Testing
input_str = "bdh"
Sample Output
4
Explanation
The extraordinary substrings are 'b', 'd', 'h' and 'bdh'.

Sample Input For Custom Testing
---
input_str = "abcd"
Sample Output
6
Explanation
The extraordinary substrings are: 'a', 'b', 'c', 'd', 'ab' and 'cd'.
"""

def converter(ch):

    ordnum = ord(ch) - ord('a')
    if ordnum <= 1:
        return 1
    else:
        remain = (ordnum - 2) // 3
        return 2 + remain
    
    # num_map = {
    #     1:'ab',
    #     2:'cde',
    #     3:'fgh',
    #     4:'ijk',
    #     5:'lmn',
    #     6:'opq',
    #     7:'rst',
    #     8:'uvw',
    #     9:'xyz',
    # }
def countSubstring(input_str):
    n = len(input_str)
    dp = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(i, n):
            if i == 0:
                dp[i][j] = converter(input_str[j]) 
                cnt += 1

            else:
                dp[i][j] = dp[i-1][j-1] + converter(input_str[j])
                cnt += dp[i][j] % (i+1) == 0
    
    return cnt



print(countSubstring('abcd')) #6
print(countSubstring('bdh')) #4