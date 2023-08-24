def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

# initial 0 and 1 base cases are constant complexity, O(1)
# else clause 0 and 1 are also O(1)

# the inside of the for loop is what we're interested in
# we go through the loop O(n) times

# final return statement is O(1)

# best case = O(1)
# worst case = O(1) + O(n) + O(1) == O(n)
