# nums = [5,7,7,8,8,10]
# target = 8

# nums = [5,7,7,8,8,10]
# target = 6

nums = [1,3]
target = 1
ans = [-1,-1]

if len(nums)>1:
    for i in range(len(nums)):
        if nums[i] == target and ans[0] == -1:
            ans[0] = i
            ans[1] = i
        elif nums[i] == target and ans[1] == i-1:
            ans[1] = i
        else:
            continue
elif len(nums) == 1:
    if nums[0] == target:
        ans[0] = 0
        ans[1] = 0


print(ans)

# this method does work in all test cases, it was created by me!