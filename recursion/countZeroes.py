n = 2020200

def countZeroes(n: int):
    return helper(n, c = 0)
def helper(n: int, c):
    if (n == 0):
        return c
    if (n%10 == 0):
        return helper(n//10, c=c+1)
    else:
        return helper(n//10, c)
print(countZeroes(n)) 