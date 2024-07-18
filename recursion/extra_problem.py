# - Write a recursive function for given n and a to determine x:
#       n = a ^ x 
#       a = 2, 3, 4
#       (2 ^ -31) <= n <= (2 ^ 31) - 1      

def find_exponent(n, a):
    # Base case: a^0 = 1
    if n == 1:
        return 0
    # If n is not divisible by a, then n is not a power of a
    elif n % a != 0:
        return None
    else:
        # Recursively divide n by a and add 1 to the exponent count
        result = find_exponent(n / a, a)
        if result is not None:
            return result + 1
        else:
            return None

# Example usage
n = 8
a = 2
print(f"The value of x for {n} = {a}^x is:", find_exponent(n, a))