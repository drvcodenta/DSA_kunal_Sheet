n = 14
arr = [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23]

temp = arr[n-1]
# print(temp)
for i in range(n-2, -1, -1):
    if (temp < arr[i]):
        arr[i+1] = arr[i]
    elif (temp >= arr[i]):
        arr[i+1] = temp
    print(*arr)

# 1 3 5 9 13 22 27 35 46 51 55 83 87 87
# 1 3 5 9 13 22 27 35 46 51 55 83 83 87
# 1 3 5 9 13 22 27 35 46 51 55 55 83 87
# 1 3 5 9 13 22 27 35 46 51 51 55 83 87
# 1 3 5 9 13 22 27 35 46 46 51 55 83 87
# 1 3 5 9 13 22 27 35 35 46 51 55 83 87
# 1 3 5 9 13 22 27 27 35 46 51 55 83 87
# 1 3 5 9 13 22 23 27 35 46 51 55 83 87