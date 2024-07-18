gain = [-5,1,5,0,-7]
# altitudeList = [0]*(len(gain)+1)
# for i in range(1, len(gain)):
#     altitudeList[i] = altitudeList[i-1] + gain[i-1]
#     print(altitudeList)

# RETURNS AN ERROR

maxValue = 0
currentValue = 0
for i in range(0, len(gain)):
    currentValue += gain[i]
    maxValue = max(maxValue, currentValue)
print(maxValue)
# GIVES GOOD TIME COMPLEXITY