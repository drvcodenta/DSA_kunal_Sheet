def BS(nums, f, l, target):
    if (f<=l):
        mid = f + (l-f)//2
        if (nums[mid] == target):
            return mid
        elif (nums[mid]>target):
            return BS(nums, f, mid-1, target)
        elif (nums[mid]<target):
            return BS(nums, mid+1, l, target)
    else:
        return -1
def main():
    nums = [-1,0,3,5,9,12] 
    target = 9
    #the target is to locate the target in the nums array
    f = 0
    l = len(nums) - 1
    result = BS(nums, f, l, target)
    if result != -1:
        print("Element is present at:", str(result))
    else:
        print("Element is not present")

if __name__ == "__main__":
    main()