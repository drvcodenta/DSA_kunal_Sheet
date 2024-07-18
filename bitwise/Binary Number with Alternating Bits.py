n = 7
def hasAlternatingBits(n: int) -> bool:
    binary = bin(n)[2:]
    for i in range(len(binary)):
        if i+1 >= len(binary):
            break
        if binary[i] != binary[i+1]:
            return False
    return True
print(hasAlternatingBits(n))