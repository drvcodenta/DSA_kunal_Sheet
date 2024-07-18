import math
n = 1234
#reverse the number using recursion


def reverseNumber(n: int):
    if(n//10 == n):
        return n
    dis = int(math.log10(n))
    return (n%10)*pow(10, dis) + reverseNumber(n//10)

# len = int(math.log10(n))
# print(len)
# print(n % pow(10, len))
# print(n//10)
# print(n%10)
print(reverseNumber(n))