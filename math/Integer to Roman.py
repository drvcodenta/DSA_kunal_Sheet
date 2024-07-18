num = 3749
# Output: "MMMDCCXLIX"

def IntToRoman(num):
    string = []
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    for i in range(len(nums)):
        while(num >= nums[i]):
            num = num - nums[i]
            string.append(roman[i])
    return "".join(string)

print(IntToRoman(num))