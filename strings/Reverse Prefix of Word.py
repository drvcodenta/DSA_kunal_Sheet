word = "abcdefd"
ch = "d"
first = word.find(ch)
if first == -1:
    print(word)
else:
    print(word[:first + 1][::-1] + word[first + 1:])