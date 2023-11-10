def maxProduct(arr, n):
 
    if (n < 2):
        print("No pairs exists")
        return
 
    if (n == 2):
        print(arr[0] ," " , arr[1])
        return
 
    # Initialize maximum and
    # second maximum
    posa = 0
    posb = 0
 
    # Initialize minimum and
    # second minimum
    nega = 0
    negb = 0
 
    # Traverse given array
    for i in range(n):
     
        # Update maximum and second
        # maximum if needed
        if (arr[i] > posa):
            posb = posa
            posa = arr[i]
         
        elif (arr[i] > posb):
            posb = arr[i]
 
        # Update minimum and second
        # minimum if needed
        if (arr[i] < 0 and abs(arr[i]) > abs(nega)):
            negb = nega
            nega = arr[i]
         
        elif(arr[i] < 0 and abs(arr[i]) > abs(negb)):
            negb = arr[i]
 
    if (nega * negb > posa * posb):
        print("Max product pair is {" ,
                nega ,", ", negb , "}")
    else:
        print( "Max product pair is {" ,
                 posa ,", " ,posb , "}")

maxProduct([3,2,1], 3)
maxProduct([-1, 1], 2)
maxProduct([-100,0,1], 3)
maxProduct([3,2,1,-1,5,0,100], 7)