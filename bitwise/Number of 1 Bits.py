n = 11
k = bin(n)
print(k)
print(len(k))
count = 0
for i in range(len(k)-2):
    res = n & 1
    n = n >> 1
    if res == 1:
        count += 1
print(count)