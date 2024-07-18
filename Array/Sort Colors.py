nums = [2,0,2,1,1,0]
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if (nums[i] > nums[j]):
#             print(f'{nums[i]} is greater than {nums[j]}')
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
# print(nums)

l = 0
r = len(nums) - 1
i = 0
while (i <= r):
    if (nums[i] == 0):
        temp = nums[i]
        nums[i] = nums[l]
        nums[l] = temp
        l = l + 1
    elif (nums[i] == 2):
        temp = nums[i]
        nums[i] = nums[r]
        nums[r] = temp
        r = r-1
    i = i + 1

print(nums)