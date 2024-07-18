mat = [[1,2],[3,4]]
r = 1
c = 4


list = []
flat = [num for row in mat for num in row]

for index_row in range(r):
    list.append(flat[index_row * c: index_row * c + c])
print(list)