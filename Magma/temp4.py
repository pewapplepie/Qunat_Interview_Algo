#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:46:23 2022

@author: y56
"""


def longest_subsequence(s):
    n = len(s)

    dp = [[0] * 5 for _ in range(n)]

    if s[0] == 'a':
        dp[0][0] = 1

    for i in range(1, n):
        if s[i] == 'a':
            dp[i][0] = 1 + dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0]

        if s[i] == 'e':
            if dp[i - 1][1] != 0:
                dp[i][1] = 1 + dp[i - 1][1]
            if dp[i - 1][0] != 0:
                dp[i][1] = max(dp[i][1], 1 + dp[i - 1][0])
        else:
            dp[i][1] = dp[i - 1][1]

        if s[i] == 'i':
            if dp[i - 1][2] != 0:
                dp[i][2] = 1 + dp[i - 1][2]
            if dp[i - 1][1] != 0:
                dp[i][2] = max(dp[i][2], 1 + dp[i - 1][1])
        else:
            dp[i][2] = dp[i - 1][2];

        if s[i] == 'o':
            if dp[i - 1][3] != 0:
                dp[i][3] = 1 + dp[i - 1][3]
            if dp[i - 1][2] != 0:
                dp[i][3] = max(dp[i][3], 1 + dp[i - 1][2])
        else:
            dp[i][3] = dp[i - 1][3]
            
        if s[i] == 'u':
            if dp[i - 1][4] != 0:
                dp[i][4] = 1 + dp[i - 1][4];
            if dp[i - 1][3] != 0:
                dp[i][4] = max(dp[i][4], 1 + dp[i - 1][3])
        else:
            dp[i][4] = dp[i - 1][4]

    return dp[n - 1][4]

def longest_sub_vowels(ss):
    n = len(ss)
    dp = [[0]*n for _ in range(5)]
    
    """
      aeiioau
    a 1000010
    e 1111111
    i 1123333
    o 1123444
    u 
    """
    if ss[0] == 'a':
        dp[0][0] = 1

    for i in range(1, n):
        if ss[i] == 'a':
            dp[0][i] = dp[0][i-1] + 1
        else:
            dp[0][i] = dp[0][i-1]
        
        if ss[i] == 'e':
            if dp[1][i-1] != 0: # a != 0
                dp[1][i] = dp[1][i-1] + 1
            if dp[0][i-1] != 0: # a != 0
                dp[1][i] = max(dp[0][i-1] + 1, dp[1][i])
            else: # a == 0
                dp[1][i] = max(dp[0][i-1], dp[1][i-1])
        if ss[i] == 'i':
            if dp[1][i-1] != 0:
                dp[2][i] = 1 + dp[2][i-1]
            else:
                dp[2][i] = max(dp[1][i-1], dp[2][i-1])
        if ss[i] == 'o':
            if dp[2][i-1] != 0:
                dp[3][i] = 1 + dp[3][i-1]
            else:
                dp[2][i] = max(dp[2][i-1], dp[3][i-1])
        if ss[i] == 'u':
            if dp[3][i-1] != 0:
                dp[4][i] = 1 + dp[3][i-1]
            else:
                dp[4][i] = max(dp[3][i-1], dp[4][i-1])
    return dp
longest_sub_vowels('aeiouu')

# print(longest_subsequence('aeiou'))
# print(longest_subsequence('aeeiiaouu'))
# print(longest_subsequence('aeiaaioooaauuaeiu'))
# print(longest_subsequence('aeiaaiooaa'))
# print(longest_subsequence('uaaauoaoiaaueaoiaioaeooeooaoiiaaeeoeoaueuioooeuiiaeuiaaeoeuieiuoouoooaoauieueaeiaaiooeeueueoooaueuaoieuieaaaouoeoeaiuuaeouoouuaoauoeieoauaeeiuaiaueeaiiooouoouuaaeiioioooaaeiiiouuiiiuuuaoieaaeuiauaeooueiiaaueoiuuuiuiaeaaoeaaouuooeeuaeiuoooaeiaoeeaueeooeoiuaueiaaaaaeaeuuaoueieoeiioeueiueioeoioiueiiaiaueuaiueooiauuiieiiiueoeeeuaaoeoieoioiuaoauiiieeaooouuueeioeoaeuiuuaeuoaaueuioueaoeiuoioiaaoaeeauioeiioueioeaeiaieaiieuooieouoaooeoeiuiaaeuaouiiuaeueaiaiiaoeiioaaaeooeieaaiiaouioauiooioeeuieaieiauuoiaioaooeiaeaaeaiuiaoiiiuuaeaouooeauiuueaoiuuuiaueoiiaoeaoeeaouieuuuaaeiouueeiaoiuauiieeaoauoaiiuaoioaiaiiaiiieoeooouaoeiaueaouaiaaaiieaiiauuieiieiuooieaououaeuoaoeiuuoeioaiaiueiuuoeeauioooueauueuieuuueoouuooiaaueaueuoaoiiaeuaeeieaeoaiuueeaiiauuueaaaeeaieeeuieaiuuoaoaaueiouaiaeeoeeueuoauieeaeaiuaaueueioaeoeeaoooooeeiuaiuaaeieuueiauuuoouiiaeaiooiiiaaoaauuaiaouaiiiueaioaeoaaoeeeoiiuaeeueeuoeaiieiuaooaiauoeuooouoouaioiaeeuuuieiaaeaoauauiaaeeeauoeeuuuooiuuiaiaaeauiiooooooiaeiuaoaoaieeaoeaeioauioeueuieeiuauooaueiieeeaoueuoauioeeaaieaiaooiooaiaaeiiuuaaaeiuoioeiuoaoueiaiieiaueiiaioaooaaeeuaaeooieeauieiuaeiaauueieaeuuieiauoeoeoouioeoaeeuuaoiuuiiueaaeuoouoaooaaieoieuieuuauoiaieoiioieoiouuioeoeeieuaiouueeuuaieoauoauoooeieieoouuiaauoauoioiuuoioouoauuueaoooaoauuaooiouuueauoaoauuiuaeaeeeuieuueeouuiiauuuieieuoaaaiauiaoeoaoiueaeuaoooaueeeoouoeiuiaouiioiuaeuiueeoeoeouoieoiooouoeaeeeoiuaouaoiooieaoeaiuiuiieeeuiooiiooeiauaueuaaouooeiaeaoieaeaeaeaaeoaieiauuieeeuoeauuoiaeiaiuuoaueuoiaueiauuiiioeoiouaeieouaeoueeeoeuiuiaeuiaiaaoeuaaaeueueuueioauuiaiueaiaeueaiiiueiieuaaeaaeeoaeeeaeeooiuiioaueeouaioaauoouoiuuaoeiiaoiieiaoeiuooiuouuaoaeiouueieuoaeeoiuaeoaoiuiaeaiiaeiuaeuioaaeeeoeaeaueaooeauuaoeiaiiueeeaoeeeeuoiuaeeueuoiaoauuoeiiuooooaeeauoeeeauooiaiauoaeaaiuoeooieaaeueeoaieaoiieueeuiaaiaioaiouuoaooaeueauiiuioaouaooeaeeuaauoeoaiaiaaouoeeaeiiiuaieeoaieuuooiiouoiaoaiuuiuuiiieuaaaaueieuuiiaeieeoeaoeuaaoaoeiiuuoioeeieaauuoauiioeiooaeaeoiuuuiuoeeiououueiiauooauaoeeoiuuaoueaooiieeiouaeooieaueeuoieiuieeieuoiueeoaouauieaeeoauaeieueeieiiooeiouuoeaoueaaioouaooaoeuaoaeiuuieuaueuaeeuoooouauaiauiaaiiuaaeuuoaauaeieaaeueuooieeeeueoiiaueoaeuuauoooouuaeuaoiuuueaaouioaiouiooaeoauoeeaeoaiaauuaoeaeiieuuaeeaauiiaueeieoueueaieieouuiaueiuoouuiooauiueoaaiuaiaaueoeoiaioeoauueoeeaeoiueeaoaiieououauoiiaeiaaiiueoiiuoaoeieeiaeoooeieeeeoaoeeeauieuaaooooioioaeuoooiiiiaaeioiuuaueoaoeeiaoaeaaueuuuioiiuouoeiaoueiiuaioaieuaeeiiaiiuiiooauuoeiaauuuauauiuooeouoeeiuoauauuuueeeoaeouuiueeauaoaoaeuoaoeeieaauiaaaioaeaaouaiueioeeaaoaeioiooiouoaooueauioueoeoiueuiaouaeuoauoeaeioaiououaeeoaeiaoeauueieooeiiuoauuueeaeooaeioeiooeoeoaoaooeeiaeoeieieuaeoieaiuauioeiiiaiuiauiaioiouauuaoioououeoeoieeoeeouaeoeeioiioeoeiauieueeeaiioaueueeoeoeeeaoeaiuueueaoaauiaoueeiieoooioeoeioaeouuoiaouuuaoeuaeoieoiuaaieeauiiaaeoaaaauaaiiiaaieoieuoiaouiuoeiouuiuaeuuaiiuuuieoaaiuaaiouooaeeaioiiiiaiuieaoaoeaeieuaiaoaeooeeaiaoaaooeouuoeuiieuieiieeeuiaeuouiuoieiiouuieauuooeoaaeoeuuiiueaieieueoaeaoaueaooaoaueuieauaoiaeuaaeoeeueueiuiuiaaiouaeeeoooeaaeaoeoieeuoueauoeaiueiaeuoouaeuiouoiaooioauuuiiaaeeaioaaaooieeeaoaeoeeuoaoaeoaueaaiaeueiioeaeeuoouoeeuiiaooueeuuoouooaouoaaoaaeuoeeooueeuiauooueaeaaeioeieoouaaiaoouaeeieoeooouuiiooioaaiuuoueoeiiiaeeuuaeauoeeeeueuueoieeouuueiiaueieeioiaueuoioouoieouuaiueeiuaaeioeaaaaouueiuoeeeeuioouoeouuiiieauuuooioaiaaeuoaoaooaoeuioueoeaoeoeoieeoeeaiooaieuaeoioiouiuieeouueoauaeiuiaiuueoiieiiiouiueaiaiiauoeiueaeuuuoueueauaueoaiuieaueeaiieuiuoiaoieaiaueeueaeoioieoioeeeaeuiieeuauiueuouiaeouiuueoeuuuaeieiueiauaaoaeaoeoeoeaaeeooaeoieooeuuauaoaaaooieeuoaooeaoeuauieiaeaeoaaiiuaiuaaueeouoaaieoueuioeoieeeuuoioauoioaaeueaeuueeoaiuoaeaoeoaiuioueeeioeeuoaueeiiiauiuuuoeeauuoeeueeoeiuuueooeaaouooaeaeuiueueoouaiaooaiauueaeooeaueiooeeuoeieiooeooioiaeiuouoauaueeiuaoeaoiiuooueaeeeaoiuaeiaaaaiouaoaioueaiooaieoaeoeuaoooeiiioeeeuiioieuaoauauaaouuiiiaiaeoeoioaouuoaueaaauiieuoeieeiiiaoaaooooiooeuouaoieeeoeoeiiuoeeaouooaiieeoaaiooooauiuiuaieiueaouioeaeaoieaoauaaiuieuioaaaieoieieeuaiaeeiouiaeeieiioaueouuieoouiieaeeoeueiiieauoueiuoeeeuieoeauauiauoieeoioieuueaooeioaoiauiiiioieaoiuuoeiouieeaouoaoaioaaeuiauiaooiouaauiaoiieiuiauiieoeaaoaioioeauuueiuauauaaeaiaiiuiaaaiooiiuouaaoaeueuaeaoeaoaeiiauiueeiaoiaoauoeuoouaaoeuuiiaoiouoouoiieeuauuaiuueiaauuuaaoeeoaooieiiooeeeiaieeaeoaaoiueaaeooauiooaaiauaaiuieeiaeooeeeeiuueauoaoaeiieaiiaoeoiiioeeaauooiaioeiuiiuaauueioauoaaoueuuoaieiooeueaoeuiiuuiaieaiiieauueuoeeaaauauauuueeiaaooaeouueeueuuioeueiueuuueouoioaieeuioeoouuaaeauaueeeieouuuoeeoeuuoeauauiiiuuaueaaouuiuiuuauioueeaiuaieoooaouoiiouuiaooeaouaieeauiaaiaoeaiiaauuuauaaiuoiouuaeieaeouioioaiieoeuieauaoiuuiuooeaioaaouaiaoueoeueioaiuieueuiioaueeiaueuaeouiiaeaiiaoueaaoeeauuoeiueaoaaueeiooiiuoueieuiiaeieuooioauuaiueeaaiiiauuioiieuoooioioeuouoaeaaiouoiauuuouuuuieiueoeeoeeiaooaooauiouauiuouauueueuaaeauoiaoeeaiioaueeeeaiiouaueaeueeeaiaueuauaaiueoaaieueueuiaiuai'))
