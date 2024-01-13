# Write an iterative function that finds the greatest common divisor of two positive integers

def gcd_iter(a, b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a and b
    """

    divisor = min(a, b)

    while divisor > 1:
        if a % divisor == 0 and b % divisor == 0:
            return divisor

        divisor -= 1

    return divisor

print(gcd_iter(2, 12))
print(gcd_iter(6, 12))
print(gcd_iter(9, 12))
print(gcd_iter(17, 12))
