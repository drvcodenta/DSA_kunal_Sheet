a= [1, 4, 3, -5, -4, 8, 6]
def getMin(a, n):
    if n == 1:
        return a[0]
    return min(a[n-1], getMin(a, n-1))
def findMinRec(A, n): 
      
    # if size = 0 means whole array 
    # has been traversed 
    if (n == 1): 
        return a[0] 
    return min(a[n - 1], findMinRec(a, n - 1)) 
def getMax(a, n):
    if n == 1:
        return a[0]
    return max(a[n-1], getMax(a, n-1))
def getMinMax( a, n):
    minimum = getMin(a, n)
    maximum = getMax(a, n)
    return minimum, maximum
    
# print(getMinMax(a, len(a)-1))
# print(getMax(a, len(a)-1))
# print(findMinRec(a, len(a)))
# print(getMin(a, len(a)))
# print(getMax(a, len(a)))
print(getMinMax(a, len(a)))