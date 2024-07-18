arr = [2,3,4,7,11]
k = 5
size = len(arr)
final_el = arr[size-1]
example_arr = []

for i in range(final_el):
    example_arr.append(i)

# print(example_arr)

#i want to delete the common elements in both arrays which are example_arr and arr

for i in arr:
    if i in example_arr:
        example_arr.remove(i)
print(example_arr)

print(example_arr[k])