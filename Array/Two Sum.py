nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
print('no sum equal to target')