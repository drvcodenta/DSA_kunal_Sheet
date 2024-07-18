import math
x = 8
#we need to solve the question without any use of built in functions like x**2
first = 1
last = x
while(first<=last):
    mid = first + (last-first)//2
    if(math.floor(mid*mid) == x):
        print(mid)
        break
    elif (mid*mid > x):
        last = mid - 1
    elif (mid*mid < x):
        first = mid + 1