n = 0b00000010100101000001111010011100

# result = n & 1
# print(result)

# n = n >> 1

# ans = 0

# ans = ans << 1

# ans = ans or result

# print(ans)
ans = 0
for i in range(32):
    result = n & 1
    n = n >> 1
    ans = ans << 1
    ans = ans | result
print(ans)