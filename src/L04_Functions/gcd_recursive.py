# Write a recursive function that finds the greatest common divisor of two positive integers

def gcd_recur(a, b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a and b
    """

    if min(a, b) == 0:
        return max(a, b)

    else:
        return gcd_recur(b, a % b)


print(gcd_recur(2, 12))
print(gcd_recur(6, 12))
print(gcd_recur(9, 12))
print(gcd_recur(17, 12))
