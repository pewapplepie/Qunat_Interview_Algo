import math
 
# A function to print all prime factors of
# a given number n
def primeFactors(n):
    res = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        res.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        
         
        # while i divides n , print i and divide n
        while n % i== 0:
            res.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        res.append(n)
        #print(n)
    return res
         
# Driver Program to test above function
 
#n = 315
primeFactors(315)