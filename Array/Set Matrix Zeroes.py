matrix = [[1,1,1],[1,0,1],[1,1,1]]

# 1 1 1
# 1 0 1
# 1 1 1

m = len(matrix) #rows
n = len(matrix[0]) #columns
row = []
col = []

for i in range(m):
    for j in range(len(matrix[i])):
        print(f"Element at ({i},{j}): {matrix[i][j]}")
        if( matrix[i][j] == 0):
            print("Yes its zero, now change all the rows and colums in line with this zero")
            row.append(i)
            col.append(j)

for i in row:
    for j in range(n):
        matrix[i][j] = 0

for i in col:
    for j in range(m):
        matrix[j][i] = 0

print(f"After changint the elements at given indexes: {matrix}")