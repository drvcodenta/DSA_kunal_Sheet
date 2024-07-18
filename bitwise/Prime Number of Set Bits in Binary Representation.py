left = 6
right = 10

def countPrimeSetBits(left: int, right: int) -> int:
    count = 0
    for i in range(left, right+1):
        k = bin(i)[2:].count('1')
        # print(k)
        if k == 1 or k == 0:
            pass
        else:
            for j in range(2, k):
                # print('nirahua nirahua')
                # print(k)
                # print(j)
                if 0 == k%j:
                    # print(' prime number')
                    break
            count += 1
                # print(count)
    return count

print(countPrimeSetBits(left, right))