items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
dictionary = {
    'type': 0,
    'color': 1,
    'name': 2
}
count = 0
# print(dictionary["color"])

# print(dictionary[ruleKey])

for i in range(0, len(items)):
    j = dictionary[ruleKey]
    if items[i][j] == ruleValue:
        count += 1

print(count)