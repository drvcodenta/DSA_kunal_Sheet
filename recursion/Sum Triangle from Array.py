A = [4, 7, 3, 6, 7]

def sum_triangle(A):
    if len(A) < 1:
        return
    temp = [0]*(len(A)-1)
    for i in range(0, len(A)-1):
        temp[i] = A[i] + A[i+1]
    sum_triangle(temp)
    print(A)
    return A

print(sum_triangle(A))