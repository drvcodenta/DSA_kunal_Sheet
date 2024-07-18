# nums = [1,1,2,3,3,4,4,8,8]
# nums = [3,3,7,7,10,11,11]
# if len(nums)==1:
#     print(nums[0])
# first=0
# last=len(nums)-1
# while(first<last):
#     mid=first+(last-first)//2
#     if (nums[mid]==nums[mid+1] or nums[mid]==nums[mid-1]):
#         #it's an element that has a double
#         #you can now check what is the index of first occuring element
#         #now take out time to find out the double numbers index...
#         if (nums[mid]==nums[mid+1]):
#             #1st case
#             if (mid%2==0):
#                 #double numbers exist in regular order,which means single element would occur later in the array
#                 #first would be updated
#                 first = mid+1
#             else:
#                 #not regular order case
#                 #last would be updated
#                 last = mid-1
#         elif (nums[mid]==nums[mid-1]):
#             #2nd case
#             if (mid-1)%2==0:
#                 #update first
#                 first = mid+1
#             else:
#                 #update last
#                 last = mid - 1
#     elif (nums[mid]!=nums[mid+1] or nums[mid]!=nums[mid+1]):
#         print(nums[mid])
#         break
# above method is correct in intuition, but has bugs!

#2nd solution:

# nums = [1,1,2,3,3,4,4,8,8]
# nums = [1,1,2]
nums = [3,3,7,7,10,11,11]
first=0
last=len(nums)-1
while(first<=last):
    mid=first+(last-first)//2
    if(((mid-1<0)or(nums[mid]!=nums[mid-1]))and((mid+1>len(nums)-1)or(nums[mid]!=nums[mid+1]))):
        print(f"{nums[mid]} for array {nums}")
        break
    #if left hand section of the mid value is in odd, then it contains the element otherwise right hand section will!
    leftSide = mid-1 if (nums[mid]==nums[mid-1]) else mid
    if leftSide%2:
        last=mid-1
    else:
        first=mid+1
