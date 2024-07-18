# nums = [12,345,2,6,7896]
nums = [555,901,482,1771]
even_count=0
for i in range(len(nums)):
    count = 1
    num = nums[i]
    while(num>=10):
        num = num/10
        count += 1
    if (count%2 == 0):
        even_count += 1
print(even_count)