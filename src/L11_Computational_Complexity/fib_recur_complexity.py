def fib_recur(n):
    """assumes n an int >= 0"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

# initial 0 and 1 base cases are constant complexity, O(1)
# else clause 0 and 1 are also O(1)

# two recursive calls for each call of the function - characteristic of exponential complexity

# worst case = O(2**n)
