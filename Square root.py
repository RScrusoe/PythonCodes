while(1):
    try:
        #Bisection method
        x = float(input("Enter a number to find the square root : "))
        epsilon = 0.001
        low = 0
        high = x
        ans = (low + high)/2.0
        numGuesses = 0

        while abs(ans**2-x)>=epsilon:
            #print("not final but near  " + str(ans))
            if abs(ans**2)<x:
                low = ans
            else:
                high=ans
            ans = (low+high)/2.0
            numGuesses+=1
        print("Number of guesse = "+ str(numGuesses))
        print("Final square root is  :  " + str(ans)+'\n')
    except:
        print("Failed !")




















'''x =float(input("Enter a number to find square root : "))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans+=step
    numGuesses+=1
print("Number of guesse : "+ str(numGuesses))
if abs(ans**2)-x>=epsilon:
    print("Failed!!")
else:
    print("Square root is "+ str(ans))
'''