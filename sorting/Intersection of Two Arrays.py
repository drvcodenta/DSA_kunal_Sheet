nums1 = [4,4,9,5,9,9]
nums2 = [9,4,9]

nums1.sort()
nums2.sort()
ans=[]

for i in range(len(nums1)):
    #binary search
    first = 0
    last = len(nums2)-1
    while(first<=last):
        mid = first + (last - first)//2
        if(nums2[mid] == nums1[i]):
            ans.append(nums2[mid])
            break
        elif (nums2[mid] > nums1[i]):
            first = mid + 1
        elif (nums2[mid] < nums1[i]):
            last = mid - 1

# for i in range(len(ans)-1):
#     if(i+1 < len(ans)):
#         if (ans[i] == ans[i+1]):
#             final_ans.append(ans[i+1])

ans = list(set(ans))

print(ans)