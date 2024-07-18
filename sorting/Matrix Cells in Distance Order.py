rows = 1
cols = 2
rCenter = 0
cCenter = 0

# list1 = []

# for i in range(rows):
#     for j in range(cols):
#         list1.append([i,j])
# print(list1)

list1 = [[x,y] for x in range(rows) for y in range(cols)]
list1.sort(key=lambda x: abs(rCenter-x[0]) + abs(cCenter-x[1]))
print(list1)