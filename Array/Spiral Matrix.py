matrix = [[1,2,3],[4,5,6],[7,8,9]]
m = len(matrix)
n = len(matrix[0])

# 1 2 3
# 4 5 6
# 7 8 9


right = n-1
bottom = m-1
left = 0
top = 0

ans = []
while(len(ans) < m*n):
    for i in range(left, right+1):
        ans.append(matrix[top][i])
    top = top + 1
    for i in range(top, bottom+1):
        ans.append(matrix[i][right])
    right = right -1
    if top <= bottom:
        for i in range(right , left -1, -1):
            ans.append(matrix[bottom][i])
        bottom = bottom -1
    if left <= right:
        for i in range(bottom , top -1, -1):
            ans.append(matrix[i][left])
        left = left + 1

print(ans)