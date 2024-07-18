a = "11"
b = "1"

i = len(a)-1
j = len(b)-1
carry = 0
ans = []
while i>=0 or j>=0 or carry:
    if i >= 0:
        carry += int(a[i])
        i = i-1
    if j >= 0:
        carry += int(b[j])
        j = j-1
    ans.append(str(carry%2))
    carry //=2

print("".join(reversed(ans)))