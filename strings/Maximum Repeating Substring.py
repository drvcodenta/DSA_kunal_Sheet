sequence = "ababc"
word = "ab"
if len(sequence)<len(word):
    print('nothing')
ans = 0
k = 1
while word*k in sequence:
    ans += 1
    k += 1
print(ans)