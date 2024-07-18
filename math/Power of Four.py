n = 16
# n = 5
# n = 1

#I'm thinking of solving the problem using bit manipulation
trial = n
msb = 0

while (trial != 0):
    trial = trial >> 1
    msb = msb + 1

# print(msb)

# four = 3

for i in range(msb):
    if n == 1:
        print("power of 4")
        break
    n = n >> 1
    if n == 4:
        print("yess it's a power of 4")
        break
    elif n < 4:
        print("Noo it's not a power of 4")
        break

#The above method works very bad in case of large numbers, so now writing recursion approach

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 4:
            return True
        elif n < 4:
            return False
        return (n%4 == 0 and self.isPowerOfFour(n//4))