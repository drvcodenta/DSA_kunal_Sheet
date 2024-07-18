nums = [0,1,2,3,4]
index = [0,1,2,2,1]

# for i in range(0, len(index)):
#     num = nums[i]
#     index = index[i]

target = []
for i,n in zip(index, nums):
    target.insert(i, n)
print(target)