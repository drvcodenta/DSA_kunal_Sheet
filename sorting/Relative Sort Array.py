arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
search_index = 0 #works in arr1
comparison_index = 0 #works in arr2
counter_index = 0 #works in arr1
ans = []
while(comparison_index < len(arr2)):
    search_index = comparison_index
    while(search_index < len(arr1)):
        if arr2[comparison_index] == arr1[search_index]:
            arr1[counter_index], arr1[search_index] = arr1[search_index], arr1[counter_index]
            counter_index += 1
            search_index += 1
        search_index += 1
    comparison_index += 1
sorted_portion = sorted(arr1[counter_index:])
ans = arr1[:counter_index] + sorted_portion
print(ans)