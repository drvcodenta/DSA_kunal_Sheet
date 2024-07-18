# x = 3
# y = 1
x = 1
y = 4

def HammingDist(x:int, y:int):
    count = 0
    binary_x = bin(x)[2:]
    binary_y = bin(y)[2:]
    max_length = max(len(binary_x), len(binary_y))
    padded_bx = binary_x.zfill(max_length)
    padded_by = binary_y.zfill(max_length)
    # print(padded_bx)
    # print(padded_by)
    for i in range(max_length):
        if padded_bx[i] != padded_by[i]:
            count = count + 1
    return count

print(HammingDist(x,y))