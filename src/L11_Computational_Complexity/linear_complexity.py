# O(n) - linear complexity
# e.g. searching a list in a sequence to check whether an element is present
# adding characters of a string
def add_digits(s):
    val = 0  # constant
    for c in s:  # number of times through loop is linear with len(s)
        val += int(c)  # constant
    return val  # constant


# complexity can depend on number of recursive calls
# iterative example below is slightly faster in time
def fact_iter(n):
    prod = i
    for i in range(1, n+1):
        prod *= i
    return prod


# number of function calls is linear in n, so still O(n)
def fact_recur(n):
    """asssume n >= 0"""
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)
