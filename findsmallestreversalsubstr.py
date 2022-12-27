# python3 code to implement the approach

# Function to return the lexicographically
# minimum string after k operations
def findStr(s, k):
    currStr = s[:k]
    
 
    # Consider all remaining substrings.
    # We consider every substring ending
    # with index i.
    st = 0
    maxstr = ""
    if currStr[::-1] + s[k:] > s:
        return currStr[::-1] + s[k:]
    for i in range(k, len(s)-k):
        currStr = currStr[1 : k] + s[i]
        currall = s[:i] + currStr[::-1] +s[i+k:]
        
        if currall > maxstr:
            maxstr = currall
        # if (lexMax < currStr):
        #     lexMax = currStr
        #     st = i
    # print(st)
    # print(s[st-k+1:st+1])
    # print(lexMax)
    return maxstr
            
    

	

# Driver Code
# if __name__ == "__main__":

	# Number of operations
K = 9

# Given string
S = "rjzrimlvumuarenexcfycebeu"

# Final answer string
ans = findStr(S, K)
print(S)
print(ans)
print("lmirzjrvumuarenexcfycebeu")

# This code is contributed by rakeshsahni
