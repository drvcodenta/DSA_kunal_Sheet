grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# count = 0

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] < 0:
#             count += 1

# print(count)

#above method is n square time complexity

# count = 0
# for i in range(len(grid)):
#     first = 0
#     last = len(grid[0])-1
#     while(first<last):
#         mid = first + (last-first)//2
#         if(grid[i][mid]<0 and grid[i][mid-1]>0):
#             count += (last-mid)
#         elif(grid[i][mid]<0 and grid[i][mid-1]<0):
#             count += (last-mid)
#             last = mid-1
#         elif(grid[i][mid]>0):
#             first = mid+1

# code error in above method

c = lambda grid: sum(el<0 for row in grid for el in row)
print(c(grid))