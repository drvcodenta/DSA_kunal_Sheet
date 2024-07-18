n = 3
# square_value = n*n
# print(square_value)
row = n
col = n
# ans = [[0]*col]*row
ans = [[0 for i in range(col)] for j in range(row)]
# print(ans)

right = n-1
left = 0
top = 0
bottom = n-1
value = 1
while ( right >= left and bottom >= top ):
    for i in range(left, right+1):
        ans[top][i] = value
        value = value + 1
    top = top + 1
    for i in range(top, bottom+1):
        ans[i][right] = value 
        value = value + 1
    right= right -1 
    if right >= left and bottom >= top:
        for i in range(right, left-1, -1):
            ans[bottom][i] = value
            value = value + 1
        bottom = bottom - 1
        for i in range(bottom, top-1, -1):
            ans[i][left] = value
            value = value + 1
        left = left + 1
    

print(ans)