def isUpper(word, index):
    if index == len(word)-1:
        return "No Upper letter found!"
    if word[index].isUpper():
        return word[index]
    return isUpper(word, index+1)

