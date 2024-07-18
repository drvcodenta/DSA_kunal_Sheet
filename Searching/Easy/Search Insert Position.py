# nums = [1,3,5,6]
# target = 5

# nums = [1,2,3,4]
# target = 2

nums = [1,3,5,6]
target = 7

first = 0
last = len(nums)-1
while(first<=last):
    mid = first + (last-first)//2
    if (nums[mid] == target):
        print(mid)
        break
    elif (nums[mid] > target):
        last = mid
    elif (nums[mid] < target):
        first = mid+1
print(first)