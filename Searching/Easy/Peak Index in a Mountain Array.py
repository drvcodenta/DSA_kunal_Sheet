# arr = [0,10,5,2]
# arr = [3,4,5,1]
# arr = [18,29,38,59,98,100,99,98,90]
arr = [3,9,8,6,4]
first = 0
last = len(arr)-1
while(first<=last):
    mid = first + (last-first)//2
    if(arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]):
        print(mid)
        break
    elif (arr[mid]<arr[mid-1]):
        last = mid 
    elif (arr[mid]<arr[mid+1]):
        first = mid + 1