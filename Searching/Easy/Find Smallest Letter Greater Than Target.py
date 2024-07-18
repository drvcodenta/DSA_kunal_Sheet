letters = ["c","f","j"]
target = "d"
# first=0
# last=len(letters)-1
# while(first<=last):
#     mid=first+(last-first)//2
#     if(letters[mid]>target):
#         last=mid
#     elif(letters[mid]<target):
#         first=mid+1
#     elif(letters[mid]==target):
#         print(mid+1)
# print(last)
for i in letters:
    if i==target:
        continue
    if i > target:
        print(i)
        break
    else:
        print(letters[0])