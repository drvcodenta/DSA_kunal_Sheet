nums = [1,2,4,5,6,3]

prefix = []

target = 0

for i in range(len(nums)):
    target = nums[i] + target
    prefix.append(target)

print(prefix)