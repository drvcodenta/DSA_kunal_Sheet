# s = "book"
s = "textbook"
# print(len(s))
half = len(s)//2
# print(half)
vowels = ['A','E','I','O','U','a','e','i','o','u']
count1 = 0
count2 = 0
for i in range(half):
    #count the number of vowels
    if s[i] in vowels:
        count1 = count1 + 1
for i in range(half, len(s)):
    #count the number of remaining vowel
    if s[i] in vowels:
        count2 = count2 + 1
if (count1 == count2):
    print("True")
else:
    print("False")