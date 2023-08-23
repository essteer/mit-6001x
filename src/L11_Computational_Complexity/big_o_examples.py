# Examples of determining Big O complexity for functions

# O(1) -> constant running time
# O(log n) -> logarithmic running time
# O(n) -> linear running time
# O(n log n) -> log-linear running time
# O(n**c) -> polynomial running time (c is a constant)
# O(c**n) -> exponential running time (c is a constant raised to a power based on size of input)

# O(1) - few examples, where complexity is independent of input
# More often there are parts of algorithms that fit this complexity

# O(log n)
# Complexity grows as a log of size of one of its inputs
# E.g. bisection search, binary search of a list
def int_to_str(i):
    digits = "123456789"
    if i == "0":
        return "0"
    result = ""
    # steps are constant within the loop, so question is how many times the loop is entered
    while i > 0:
        result = digits[i % 10] + result
        i = i//10
    return result


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
