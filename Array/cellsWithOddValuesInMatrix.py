# m = 2
# n = 3
# indices = [[0,1],[1,1]]
# matrix = [[0]*n for _ in range(m)]
# for row in indices:
#     num_row = row[0]
#     num_column = row[1]
#     for i in matrix[num_row]:
#         matrix[num_row][i] += 1
#     for i in matrix:
#         i[num_column] += 1
# print(matrix)


#The above code didn't worked as expected

# m = 2
# n = 3
# indices = [[0,1],[1,1]]
# matrix = [[0]*n for _ in range(m)]
# for row in indices:
#     num_row = row[0]
#     num_column = row[1]
#     for i in range(n):
#         matrix[num_row][i] += 1
#     for i in matrix:
#         i[num_column] += 1
# print(matrix)


m = 2
n = 3
indices = [[0,1],[1,1]]
matrix = [[0]*n for _ in range(m)]
for ri,ci in indices:
    for i in range(n):
        matrix[ri][i] += 1
    for j in range(m):
        matrix[j][ci] += 1
# print(matrix)
count = 0
        
for row in matrix:
    for column in row:
        if column%2!= 0:
            count += 1

print(count)