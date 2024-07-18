list = [1,2,3,4,4,3,2,1]
ans = []
n = len(list)

l = n//2

for i in range(0,l):
    ans.append(list[i])
    ans.append(list[i+l])

print(ans)