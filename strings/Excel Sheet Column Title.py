columnNumber = 701
#let's solve the damn problem, ohh yeah...
#so divmod function returns two values which are quotient and remainder (quotient, remainder)
#quotient are also the column number values which signifies the value of column in the final ans
# (q, r) = divmod(columnNumber, 26)
# print(q, r)
result = []
while(columnNumber):
    # result.append()
    (columnNumber, r) = divmod(columnNumber-1, 26)
    result.append(chr(65+r))
print("".join(reversed(result)))
print(result)