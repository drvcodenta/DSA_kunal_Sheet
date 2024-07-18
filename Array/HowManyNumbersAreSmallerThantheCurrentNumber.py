nums = [8,1,2,2,3]
ans = []
sorted_nums = sorted(nums)
for i in range(0, len(nums)):
    num = nums[i]
    # print(num)
    ans.append(sorted_nums.index(num))

print(ans)