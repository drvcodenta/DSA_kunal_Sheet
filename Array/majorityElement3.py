nums = [0,0,0]

def majorityElement(nums):
    oneThird = len(nums)//3
    # print(oneThird)
    dictionary = {}
    ans = set()
    if len(nums) == 1 or len(nums) == 2:
        return list(set(nums))
    for i in range(len(nums)):
        dictionary[nums[i]] = dictionary.get(nums[i], 0) + 1
        if dictionary[nums[i]] > oneThird:
            ans.add(nums[i])
        # print(ans)
    return list(ans)

print(majorityElement(nums))