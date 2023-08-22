# An example of a recursive function, for multiplying two integers

def mult(a, b):
    """
    Takes two integers, a and b
    Returns the product of those integers via recursion
    """
    if b == 1:
        return a

    else:
        return a + mult(a, b - 1)


# Compare iterative version:
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
