def reverse(str, i, j):
    if i>j:
        return
    temp = str[i]
    str[i] = str[j]
    str[j] = temp
    return reverse(str, i=i+1, j=j-1)

# print(reverse(s, 0, len(s)-1))
def main():
    s = ["h","e","l","l","o"]
    reverse(s, 0, len(s)-1)
    print(s)

if __name__ == "__main__":
    main()