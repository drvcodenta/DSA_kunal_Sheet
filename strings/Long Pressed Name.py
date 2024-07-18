# name = "alex"
# typed = "aaleex"

# for i in name:
#     if i not in typed:
#         print(False)
#     else:
#         typed.replace(i,'')
#         continue
# print(True)
# name = "saeed"
# typed = "ssaaedd"

name = "kikcxmvzi"
typed = "kiikcxxmmvvzz"
i = 0
output = True
lastString = ''
while(output and i < len(name)):
    if len(name) > len(typed):
        print('False')
        break
    if(name[i] == typed[i]):
        lastString = name[i]
        i += 1
    elif ((name[i] != typed[i]) and (typed[i] == lastString)):
        typed = typed[0: i] + typed[i+1:]
    else:
        output = False
endingTypedEntries = set(typed[len(name): ])
# print(set(name[-1]))
if len(endingTypedEntries) != 0:
    if set(name[-1]) != endingTypedEntries:
        output = False
print(output)