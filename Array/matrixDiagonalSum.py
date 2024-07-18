mat = [[1,2,3],[4,5,6],[7,8,9]]
n = len(mat)
sum = 0
mid = n // 2
for i in range(n):
    sum += mat[i][i]
    sum += mat[n-i-1][i]
if n % 2 == 1:
    sum -= mat[mid][mid]
print(sum)