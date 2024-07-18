left = 1
right = 22

def isSelfDividing(num):
    for i in str(num):
        if i == '0' or num % int(i) != 0:
            return False
    return True

# print(isSelfDividing(6))

# for i in str(right):
#     print(i)

string = []
for i in range(left, right+1):
    count = isSelfDividing(i)
    if count:
        string.append(i)
print(string)