# n = 19
# UniqueList = []
# def isHappy(n):
#     global UniqueList 
#     count = 0
#     string = str(n)
#     for i in range(len(string)):
#         count += int(string[i])*int(string[i])
#     if (count == 1):
#         return True
#     else:
#         #check for the cyclic nature
#         if count not in UniqueList:
#             UniqueList.append(count)
#             return isHappy(count)
#         else:
#             return False
# restult = isHappy(n)
# print(restult)


# Above code solves the problem using recursion, now here's the iteration method

