s = "is2 sentence4 This1 a3"
a = s.split()
print("s:",s)
print("a:",a)
# for i in range(len(a)):
#     print(sorted(a, key=a[i][-1]))

sorted_words = sorted(a, key=lambda x: x[-1])
# print(sorted_words)
sorted_array = [i[:-1] for i in sorted_words]
print(sorted_array)
print(" ".join(sorted_array))