import pytest
def solution(source):
    ttlcnt, currcnt, in_block_comment = 0, 0 , False
    for line in source:
        i = 0
        while i < len(line):
            char = line[i]
            if char == '/' and (i + 1) < len(line) and line[i+1] == '/' and not in_block_comment:
                i = len(line)
            elif char == '/' and (i + 1) < len(line) and line[i+1] == '*' and not in_block_comment:
                in_block_comment = True
                i += 1
            elif char == '*' and (i + 1) < len(line) and line[i+1] == '/' and in_block_comment:
                in_block_comment = False
                i += 1
            elif not in_block_comment and char != ' ':
                currcnt += 1
            i+= 1 
        if currcnt > 0 and not in_block_comment:
            ttlcnt += currcnt
            currcnt = 0
    return ttlcnt

solution([
            "int a = 2;",
            "int b = 47;/*37;*///41;",
            "int c = 3/*4//5*/;",
            "return a / b * c/*a /*b / c*/;"
        ]) # == 34
        


solution([
            "var a = 2;",
            "/*",
            "var b = 2;",
            "if (a === b) {",
            "  b = a + 1;",
            "  //b = a * 2 - 1;",
            "}",
            "*/",
            "var b = 3;",
            "return a * b;"
        ])# == 24

# def test_case2():
#     assert solution([1,2,3,4],15) == [-1, -1]

# def test_case3():
#     assert solution([1],1) == [0, 0]