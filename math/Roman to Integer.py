s = "MCMXCIV"

roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

count = 0
for i in range(len(s)-1):
    if roman[s[i]] < roman[s[i+1]]:
        count -= (roman[s[i]])
        i = i+1
    else:
        count += roman[s[i]]
print(count+roman[s[-1]])