nums = [-2,1,-3,4,-1,2,1,-5,4]
# list = []
# sum = 0
# for i in range(len(nums)):
#     if(nums[i] > 0):
#         sum += nums[i]
#         for j in range(i+1, len(nums)):
#             sum += nums[j]
#             # print(sum)
#             list.append(sum)
#         sum = 0
        
# print(list)

max_current = max_global = nums[0]
for i in range(1, len(nums)):
    max_current = max(nums[i], max_current + nums[i])
    if max_current > max_global:
        max_global = max_current

print(max_global)