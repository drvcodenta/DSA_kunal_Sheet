n = 16

def isPowerofTwo(n):
    if (n==1):
        return True
    if (n%2 == 0):
        return isPowerofTwo(n/2)
    else:
        return False

print(isPowerofTwo(3))

# print(n//3)