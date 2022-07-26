def firstDuplicateValue(arr):
    seen = dict()
    for idx, val in enumerate(arr):
        if val in seen:
            return val
        else:
            seen[val]= idx
    return -1