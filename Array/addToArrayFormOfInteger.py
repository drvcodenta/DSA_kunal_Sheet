# num = [1,2,0,0]
# k = 34
num = [2,7,4]
k = 181
string = ''.join(map(str, num))
print(type(''.join(map(str, num))))
print(string)
string_ans = str(int(string) + k)
ans = []
for i in range(len(string_ans)):
    ans.append(int(string_ans[i]))
print(ans)
print(type(ans[0]))