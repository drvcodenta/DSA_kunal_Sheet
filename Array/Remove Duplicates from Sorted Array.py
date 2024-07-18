nums = [1,1,2]
j = 0
i = 0

for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[i-1] = nums[i]
        j = j + 1
print(j)