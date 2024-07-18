# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]
m=len(matrix)
n=len(matrix[0])
ans=[[0]*m for _ in range(n)]
for i in range(m):
    for j in range(n):
        ans[j][i] = matrix[i][j]
print(ans)