# columnNumber = 701
columnNumber = 2147483647


# if columnNumber>26:
#     firstVar = int(columnNumber//26)
# secondVar = int(columnNumber%26)
# # print(firstVar)
# print(chr(64+firstVar))
# print(chr(64+secondVar))

# string = []
# string.append(chr(64+firstVar))
# string.append(chr(64+secondVar))
# print(string)
# print("".join(string))

#above method leetcode walon ko nahi chahiye, so here is the copied solution
string = []
while(columnNumber):
    (columnNumber,r) = divmod(columnNumber-1, 26)
    string.append(chr(65+r))
print("".join(string))
# print(chr(65 + columnNumber), chr(64 + r))
print("".join(reversed(string)))