def arrayChallenge(arr):
    k = arr[0]
    currmedian = []
    ans = ''
    for i in range(1, len(arr)):
        if i<k:
            currmedian.append(arr[i])
            print('curr len',len(currmedian))

            ans += str(findMedian(currmedian))
            
        else:
            currmedian.append(arr[i])
            print('curr len',len(currmedian))
            ans += str(findMedian(currmedian))
            del currmedian[0]
        if i != len(arr) -1 :
                ans += ','
    return ans


def findMedian(arr):
    n = len(arr)
    arr = sorted(arr)
    return arr[n//2] if n&1 == 1 else (arr[n//2] + arr[n//2 - 1])/2

arrayChallenge([5,2,4,6])
#arrayChallenge([3,0,0,-2,0,2,0,-2])
