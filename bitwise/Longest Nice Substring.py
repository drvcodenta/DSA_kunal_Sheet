s = "YazaAay"

def longestNiceSubstring(s: str) -> str:
    if len(s)<2: return ""
    unordered_set = set(s)
    for i in range(len(s)):
        if s[i].lower() and s[i].upper() in unordered_set:
            continue
        previousString = longestNiceSubstring(s[:i])
        nextString = longestNiceSubstring(s[i+1:])
        return previousString if len(previousString)>len(nextString) else nextString
    return s

print(longestNiceSubstring(s))