digits = [9]
lastIndex = len(digits) - 1

# print(lastIndex)
# if digits[lastIndex] < 9:
#     digits[lastIndex] = digits[lastIndex] + 1
# elif digits[lastIndex] == 9:
#     if len(digits) == 1:
#         digits.clear()
#         digits.append(1)
#         digits.append(0)(
#     else:
#         digits[lastIndex] = digits[lastIndex] + 1
#         digits[lastIndex - 1] = digits[lastIndex - 1] + 1
# Above solution does not work in all cases
def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1 , -1, -1):
        if digits[i] == 9:
            digits[0] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits

print(plusOne(digits=[9]))