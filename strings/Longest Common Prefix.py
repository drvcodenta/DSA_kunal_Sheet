strs = ["flower","flow","flight"]
temp = ''
strs = sorted(strs)
first = strs[0]
last = strs[-1]
for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        print(temp)
        break
    else:
        temp = temp+first[i]
else:
    print(temp)