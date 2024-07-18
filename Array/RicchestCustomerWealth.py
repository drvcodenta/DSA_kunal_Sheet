accounts = [[1,2,3],[3,2,1],[8,2,3],[3,2,3]]

for i in range(len(accounts)):
    target = 0
    for j in accounts[i]:
        target = target + j
    accounts[i] = target

print(max(accounts))