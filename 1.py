import math

def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x

def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

for i in range(1,10000000 ):
    if (isFibonacci(i)==True):
        print (i,'is a Fibonacci Number')
    else:
        pass


        

