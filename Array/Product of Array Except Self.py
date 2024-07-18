nums = [-1,1,0,-3,3]
ans = []
# prod = 1
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if j == i:
#             continue
#         else:
#             prod = prod * nums[j]
#     ans.append(prod)
#     prod = 1
# print(ans)

# above approach is time taking process

prefix_prod = 1
suffix_prod = 1

prefix_arr = []
suffix_arr = []
for i in range(len(nums)):
    prefix_arr.append(prefix_prod)
    prefix_prod = prefix_prod * nums[i]
for i in range(len(nums)-1, -1, -1):
    suffix_arr.append(suffix_prod)
    suffix_prod *= nums[i]

result = [0]*len(nums)
print(result)
print(prefix_arr)
print(suffix_arr)
n = len(result)
for i in range(n):
    result[i] = prefix_arr[i] * suffix_arr[n-i-1]
print(result)