from collections import Counter

def func(text, k):
    words = text.split()
    leftidx = {}
    for i, word in enumerate(words):
        if word not in leftidx:
            leftidx[word] = i
    
    candidates = [word for word, count in Counter(words).items() if count >= k]

    return sorted(candidates, key=lambda x: leftidx[x])
print('hi')
print(func('a b c c b a d', 2))