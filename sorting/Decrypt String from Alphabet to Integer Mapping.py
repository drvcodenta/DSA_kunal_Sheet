s = "10#11#12"

ans = []
i = 0
while(i<len(s)):

    if(i+2 < len(s) and s[i+2] == '#'):
        #decode 2 character as one and append it to the answer list
        j = int(s[i:i+2])
        ans.append(chr(j+96))
        i = i+3
    else:
        #decode only 1 character and append to the answer list
        j = int(s[i])
        ans.append(chr(j+96))
        i = i + 1

print(ans)

# 1-a, 2-b
# i = 1
# i = 10
# print(chr(i+96))