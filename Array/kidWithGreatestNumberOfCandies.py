candies = [4,2,1,1,2]
extraCandies = 1
ans = []
maxCandies = max(candies)
l = len(candies)
for i in range(0, l):
    candies[i] = candies[i] + extraCandies
    if candies[i] >= maxCandies:
        ans.append(True)
    else:
        ans.append(False)

print(ans)