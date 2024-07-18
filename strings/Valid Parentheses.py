s = "()[]{}"
s = "(]"

def isValid(s):
    for i in range(len(s)):
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""
print(isValid(s))