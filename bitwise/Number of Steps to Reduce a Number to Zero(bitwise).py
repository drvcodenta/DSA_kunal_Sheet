num = 14

def numberOfSteps(num:int):
    count = 0
    while(num!=0):
        if (num&1 == 1):
            num = num - 1
        else:
            num = num>>1
        count = count + 1
    return count

print(numberOfSteps(num))