def maxSubarray(arr, i, j):
    t = arr[0]
    vmax = arr[0]
    tmin = min(0, t)
    for k in range(1, len(arr)):
        t +=arr[k]
        if t - tmin > vmax:
            vmax = t - tmin
            j = k 
        if t < tmin:
            tmin = t
            i = k+1 if k+1<j else j
    return vmax