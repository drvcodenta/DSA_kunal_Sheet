n = 153
def armstrongNumber (n):
    # code here 
    value = sum(int(i)**3 for i in str(n))
    if value == n:
        return True
    else:
        return False
print(armstrongNumber(n))
