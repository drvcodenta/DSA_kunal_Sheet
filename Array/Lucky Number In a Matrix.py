matrix = [[3,7,8],[9,11,13],[15,16,17]]
# transposedMatrix = [list(row) for row in zip(*matrix)]
# print(transposedMatrix)
# max_col = [0]*len(transposedMatrix[0])
# for i in range(len(transposedMatrix)):
#     max_col[i] = max(transposedMatrix[i])


minRow = {min(row) for row in matrix}
# print(minRow)

maxCol = {max(col) for col in zip(*matrix)}
# print(maxCol)

print(list(minRow & maxCol))





# largest in column, smallest in row