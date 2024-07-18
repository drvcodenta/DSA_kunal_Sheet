nums = [1,2,3,4,5,6,7]
k = 3
# for i in range(1, k+1):
#     popped_value = nums.pop()
#     nums.insert(0, popped_value)
# print(nums)
# yeh kuch jyada simple nahi thaa?

if len(nums)>k:
    k = k%len(nums)

last_k_elements = nums[-k:]
print(last_k_elements)

nums[k:] = nums[:-k]
print(nums)

nums[:k] = last_k_elements
print(nums)