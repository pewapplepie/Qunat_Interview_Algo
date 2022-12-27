#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:53:49 2022

@author: y56
"""
import sys
sys.setrecursionlimit(5000)

def longest_subsequence(s):
    mapping = {ch: i for i, ch in enumerate('aeiou')}
    my_cache = {}

    def dfs(subseq, i):
        # Termination check.
        if i == len(s):
            if set('aeiou') == set(subseq):
                return subseq
            else:
                return ''

        # Fetch cache.
        if subseq == '':
            last_ch = None
        else:
            last_ch = subseq[-1]
        key_for_cache = (last_ch, len(subseq), i)

        if key_for_cache in my_cache:
            return my_cache[key_for_cache]

        # Cache miss.
        if subseq == '':
            if s[i] == 'a':
                res = dfs('a', i + 1)
            else:
                res = dfs(subseq, i + 1)
        elif subseq[-1] == s[i]:
            res = dfs(subseq + s[i], i + 1)
        elif mapping[subseq[-1]] + 1 == mapping[s[i]]:
            choice_1 = dfs(subseq + s[i], i + 1)
            choice_2 = dfs(subseq, i + 1)

            if len(choice_1) > len(choice_2):
                res = choice_1
            else:
                res = choice_2
        else:
            res = dfs(subseq, i + 1)

        my_cache[key_for_cache] = res
        return res

    output = dfs('', 0)
    return len(output)

print(longest_subsequence('aeeiiouu'))
print(longest_subsequence('aeeiiaouu'))
print(longest_subsequence('aeiaaioooaauuaeiu'))
print(longest_subsequence('aeiaaiooaa'))
print(longest_subsequence('uaaauoaoiaaueaoiaioaeooeooaoiiaaeeoeoaueuioooeuiiaeuiaaeoeuieiuoouoooaoauieueaeiaaiooeeueueoooaueuaoieuieaaaouoeoeaiuuaeouoouuaoauoeieoauaeeiuaiaueeaiiooouoouuaaeiioioooaaeiiiouuiiiuuuaoieaaeuiauaeooueiiaaueoiuuuiuiaeaaoeaaouuooeeuaeiuoooaeiaoeeaueeooeoiuaueiaaaaaeaeuuaoueieoeiioeueiueioeoioiueiiaiaueuaiueooiauuiieiiiueoeeeuaaoeoieoioiuaoauiiieeaooouuueeioeoaeuiuuaeuoaaueuioueaoeiuoioiaaoaeeauioeiioueioeaeiaieaiieuooieouoaooeoeiuiaaeuaouiiuaeueaiaiiaoeiioaaaeooeieaaiiaouioauiooioeeuieaieiauuoiaioaooeiaeaaeaiuiaoiiiuuaeaouooeauiuueaoiuuuiaueoiiaoeaoeeaouieuuuaaeiouueeiaoiuauiieeaoauoaiiuaoioaiaiiaiiieoeooouaoeiaueaouaiaaaiieaiiauuieiieiuooieaououaeuoaoeiuuoeioaiaiueiuuoeeauioooueauueuieuuueoouuooiaaueaueuoaoiiaeuaeeieaeoaiuueeaiiauuueaaaeeaieeeuieaiuuoaoaaueiouaiaeeoeeueuoauieeaeaiuaaueueioaeoeeaoooooeeiuaiuaaeieuueiauuuoouiiaeaiooiiiaaoaauuaiaouaiiiueaioaeoaaoeeeoiiuaeeueeuoeaiieiuaooaiauoeuooouoouaioiaeeuuuieiaaeaoauauiaaeeeauoeeuuuooiuuiaiaaeauiiooooooiaeiuaoaoaieeaoeaeioauioeueuieeiuauooaueiieeeaoueuoauioeeaaieaiaooiooaiaaeiiuuaaaeiuoioeiuoaoueiaiieiaueiiaioaooaaeeuaaeooieeauieiuaeiaauueieaeuuieiauoeoeoouioeoaeeuuaoiuuiiueaaeuoouoaooaaieoieuieuuauoiaieoiioieoiouuioeoeeieuaiouueeuuaieoauoauoooeieieoouuiaauoauoioiuuoioouoauuueaoooaoauuaooiouuueauoaoauuiuaeaeeeuieuueeouuiiauuuieieuoaaaiauiaoeoaoiueaeuaoooaueeeoouoeiuiaouiioiuaeuiueeoeoeouoieoiooouoeaeeeoiuaouaoiooieaoeaiuiuiieeeuiooiiooeiauaueuaaouooeiaeaoieaeaeaeaaeoaieiauuieeeuoeauuoiaeiaiuuoaueuoiaueiauuiiioeoiouaeieouaeoueeeoeuiuiaeuiaiaaoeuaaaeueueuueioauuiaiueaiaeueaiiiueiieuaaeaaeeoaeeeaeeooiuiioaueeouaioaauoouoiuuaoeiiaoiieiaoeiuooiuouuaoaeiouueieuoaeeoiuaeoaoiuiaeaiiaeiuaeuioaaeeeoeaeaueaooeauuaoeiaiiueeeaoeeeeuoiuaeeueuoiaoauuoeiiuooooaeeauoeeeauooiaiauoaeaaiuoeooieaaeueeoaieaoiieueeuiaaiaioaiouuoaooaeueauiiuioaouaooeaeeuaauoeoaiaiaaouoeeaeiiiuaieeoaieuuooiiouoiaoaiuuiuuiiieuaaaaueieuuiiaeieeoeaoeuaaoaoeiiuuoioeeieaauuoauiioeiooaeaeoiuuuiuoeeiououueiiauooauaoeeoiuuaoueaooiieeiouaeooieaueeuoieiuieeieuoiueeoaouauieaeeoauaeieueeieiiooeiouuoeaoueaaioouaooaoeuaoaeiuuieuaueuaeeuoooouauaiauiaaiiuaaeuuoaauaeieaaeueuooieeeeueoiiaueoaeuuauoooouuaeuaoiuuueaaouioaiouiooaeoauoeeaeoaiaauuaoeaeiieuuaeeaauiiaueeieoueueaieieouuiaueiuoouuiooauiueoaaiuaiaaueoeoiaioeoauueoeeaeoiueeaoaiieououauoiiaeiaaiiueoiiuoaoeieeiaeoooeieeeeoaoeeeauieuaaooooioioaeuoooiiiiaaeioiuuaueoaoeeiaoaeaaueuuuioiiuouoeiaoueiiuaioaieuaeeiiaiiuiiooauuoeiaauuuauauiuooeouoeeiuoauauuuueeeoaeouuiueeauaoaoaeuoaoeeieaauiaaaioaeaaouaiueioeeaaoaeioiooiouoaooueauioueoeoiueuiaouaeuoauoeaeioaiououaeeoaeiaoeauueieooeiiuoauuueeaeooaeioeiooeoeoaoaooeeiaeoeieieuaeoieaiuauioeiiiaiuiauiaioiouauuaoioououeoeoieeoeeouaeoeeioiioeoeiauieueeeaiioaueueeoeoeeeaoeaiuueueaoaauiaoueeiieoooioeoeioaeouuoiaouuuaoeuaeoieoiuaaieeauiiaaeoaaaauaaiiiaaieoieuoiaouiuoeiouuiuaeuuaiiuuuieoaaiuaaiouooaeeaioiiiiaiuieaoaoeaeieuaiaoaeooeeaiaoaaooeouuoeuiieuieiieeeuiaeuouiuoieiiouuieauuooeoaaeoeuuiiueaieieueoaeaoaueaooaoaueuieauaoiaeuaaeoeeueueiuiuiaaiouaeeeoooeaaeaoeoieeuoueauoeaiueiaeuoouaeuiouoiaooioauuuiiaaeeaioaaaooieeeaoaeoeeuoaoaeoaueaaiaeueiioeaeeuoouoeeuiiaooueeuuoouooaouoaaoaaeuoeeooueeuiauooueaeaaeioeieoouaaiaoouaeeieoeooouuiiooioaaiuuoueoeiiiaeeuuaeauoeeeeueuueoieeouuueiiaueieeioiaueuoioouoieouuaiueeiuaaeioeaaaaouueiuoeeeeuioouoeouuiiieauuuooioaiaaeuoaoaooaoeuioueoeaoeoeoieeoeeaiooaieuaeoioiouiuieeouueoauaeiuiaiuueoiieiiiouiueaiaiiauoeiueaeuuuoueueauaueoaiuieaueeaiieuiuoiaoieaiaueeueaeoioieoioeeeaeuiieeuauiueuouiaeouiuueoeuuuaeieiueiauaaoaeaoeoeoeaaeeooaeoieooeuuauaoaaaooieeuoaooeaoeuauieiaeaeoaaiiuaiuaaueeouoaaieoueuioeoieeeuuoioauoioaaeueaeuueeoaiuoaeaoeoaiuioueeeioeeuoaueeiiiauiuuuoeeauuoeeueeoeiuuueooeaaouooaeaeuiueueoouaiaooaiauueaeooeaueiooeeuoeieiooeooioiaeiuouoauaueeiuaoeaoiiuooueaeeeaoiuaeiaaaaiouaoaioueaiooaieoaeoeuaoooeiiioeeeuiioieuaoauauaaouuiiiaiaeoeoioaouuoaueaaauiieuoeieeiiiaoaaooooiooeuouaoieeeoeoeiiuoeeaouooaiieeoaaiooooauiuiuaieiueaouioeaeaoieaoauaaiuieuioaaaieoieieeuaiaeeiouiaeeieiioaueouuieoouiieaeeoeueiiieauoueiuoeeeuieoeauauiauoieeoioieuueaooeioaoiauiiiioieaoiuuoeiouieeaouoaoaioaaeuiauiaooiouaauiaoiieiuiauiieoeaaoaioioeauuueiuauauaaeaiaiiuiaaaiooiiuouaaoaeueuaeaoeaoaeiiauiueeiaoiaoauoeuoouaaoeuuiiaoiouoouoiieeuauuaiuueiaauuuaaoeeoaooieiiooeeeiaieeaeoaaoiueaaeooauiooaaiauaaiuieeiaeooeeeeiuueauoaoaeiieaiiaoeoiiioeeaauooiaioeiuiiuaauueioauoaaoueuuoaieiooeueaoeuiiuuiaieaiiieauueuoeeaaauauauuueeiaaooaeouueeueuuioeueiueuuueouoioaieeuioeoouuaaeauaueeeieouuuoeeoeuuoeauauiiiuuaueaaouuiuiuuauioueeaiuaieoooaouoiiouuiaooeaouaieeauiaaiaoeaiiaauuuauaaiuoiouuaeieaeouioioaiieoeuieauaoiuuiuooeaioaaouaiaoueoeueioaiuieueuiioaueeiaueuaeouiiaeaiiaoueaaoeeauuoeiueaoaaueeiooiiuoueieuiiaeieuooioauuaiueeaaiiiauuioiieuoooioioeuouoaeaaiouoiauuuouuuuieiueoeeoeeiaooaooauiouauiuouauueueuaaeauoiaoeeaiioaueeeeaiiouaueaeueeeaiaueuauaaiueoaaieueueuiaiuai'))
