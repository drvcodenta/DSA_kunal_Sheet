n = 5
def binaryGap(n):
    binary = bin(n)[2:]
    # print(binary)
    i = 0
    gap = []
    while(i < len(binary)):
        j = i + 1
        flag = 0
        while j < len(binary):
            if binary[i] == '1' and binary[j] == '1':
                print('Adjacent Found')
                flag = 1
                gap.append(j - i)
                i = j
                print(gap)
                break
            else:
                j = j+1  
        if 0 == flag:
            i = i+1
    if gap == []:
        return 0
    else:
        return max(gap)
print(binaryGap(n))