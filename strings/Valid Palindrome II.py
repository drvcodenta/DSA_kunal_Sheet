s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
l = 0
r = len(s)-1
c = 0
while(l<=r):
    if s[l] == s[r]:
        l = l + 1
        r = r - 1
    elif s[l+1] == s[r] and c == 0:
        l = l + 1
        c = 1
    elif s[l] == s[r-1] and c == 0:
        r = r - 1
        c = 1
    else:
        print("False")
        break
else:
    print("True")