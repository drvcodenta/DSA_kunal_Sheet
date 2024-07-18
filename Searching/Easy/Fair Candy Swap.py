aliceSizes = [1,2]
bobSizes = [2,3]
sets=set(aliceSizes)
x = (sum(aliceSizes)-sum(bobSizes))//2
for y in bobSizes:
    if x+y in sets:
        print([x+y, y])
        break
