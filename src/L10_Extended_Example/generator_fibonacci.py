# An example of using generators, for the Fibonacci sequence

def gen_fib():
    fibn_1 = 1  # fib(n-1)
    fibn_2 = 0  # fib(n-2)

    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next


fib = gen_fib()

# Print the generator object
print(fib)

# Cycle through the sequence each time next is called
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
