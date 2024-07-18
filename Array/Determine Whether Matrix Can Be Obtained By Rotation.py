# matrix = [[0,0,0],[0,1,0],[1,1,1]]
# target = [[1,1,1],[0,1,0],[0,0,0]]

matrix = [[1,1],[0,1]]
target = [[1,1],[1,0]]

n = len(matrix)
def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    return matrix


def flip(matrix):
    n = len(matrix)
    start = 0
    end = n-1
    for i in range(n):
        while(start <= end):
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            start += 1
            end -= 1

def check(matrix, targetMatrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != targetMatrix[i][j]:
                return False
    return True

def rotate(matrix):
    transpose(matrix)
    flip(matrix)
    return matrix

for i in range(n):
    rotate(matrix)
    if (check(matrix, target)):
        print("true")
    print("false")
