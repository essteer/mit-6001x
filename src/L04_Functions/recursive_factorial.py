# An example of a recursive function, for calculating factorials

def fact_recur(n):
    """
    Takes an integer, n
    Calculates the factorial of that integer using recursion
    """
    if n == 1:
        return 1

    else:
        return n * fact_recur(n - 1)


# Compare iterative version:
def fact_iter(n):
    """
    Takes an integer, n
    Calculates the factorial of that integer using iteration
    """
    prod = 1

    for i in range(1, n + 1):
        prod *= i

    return prod
