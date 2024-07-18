n = 5
ans = [0]*n
if(n%2 == 0):
    for i in range(0, n, 2):
        ans[i] = i+1
        ans[i+1] = -(i+1)
else:
    for i in range(0, n-1, 2):
        ans[i] = i+1
        ans[i+1] = -(i+1)
print(ans)