a = "1010"
b = "1011"

# binary = int(a)
# print(binary)
# carry = 0
# string = []
# for i in range(len(a)-1, -1, -1):
#     if int(a[i]) == int(b[i]) == 1:
#         # print("yes it's 1", i)
#         string.append("0")
#         carry = 1
#     elif int(a[i]) != int(b[i]):
#         if 1 == carry:
#             string.append("0")
#         elif 0 == carry:
#             string.append("1")
#     elif int(a[i]) == int(b[i]) == 0:
#         if 1 == carry:
#             string.append("1")
#             carry = 0
# if carry == 1:
#     string.append("1")
# print("".join(reversed(string)))

# print(int(a))
# print("0b" + a)
# print(int(a, 2))

print(bin(int(a,2)+int(b,2))[2:])