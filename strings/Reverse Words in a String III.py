s = "Let's take LeetCode contest"
array = s.split()
# print(array)
# for i in array:
#     lambda i: i[::-1]
# print(array)

print(array[0][::-1])

print(''.join(map(lambda x: x[::-1], array)))