image = [[1,1,0],[1,0,1],[0,0,0]]
for k in range(0, len(image)):
    i=0
    j=len(image)-1
    while(i<=j):
        image[k][i], image[k][j] = image[k][j], image[k][i]
        image[k][i] = image[k][i]^1
        image[k][j] = image[k][j]^1
        if i==j:
            image[k][i] = image[k][i]^1
        i += 1
        j -= 1
print(image)