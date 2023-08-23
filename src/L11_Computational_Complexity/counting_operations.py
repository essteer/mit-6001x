# An example of counting operations in a program to test efficiency
# This is not an optimal method

# Assume that the following steps take constant time:
# mathematical operations
# comparisons
# assignments
# accessing objects in memory
# Then count the number of operations executed as a fuction of size of output

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32  # 3 operations


def my_sum(x):
    total = 0  # 1 operation
    for i in range(x + 1):  # 1 operation x times
        total += i  # 2 operations x times
    return i  # operations = 1 + 3x operations


# Pros
# Depends on algorithm
# Independent of computers

# Cons
# There is no formal definition of which operations to count
# Count depends on implementations
