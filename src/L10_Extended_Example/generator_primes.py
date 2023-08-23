# An example of using generators, for prime numbers

# Write a generator, gen_primes, that returns the sequence of prime numbers
# on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# Have the generator keep a list of the primes it's generated
# A candidate number x is prime if (x % p) != 0 for all earlier primes p

def gen_primes():
    """
    Generator function for prime numbers.
    Based on the formula (x % p) != 0
    for all earlier primes
    """

    primes_list = [2]
    x = 3
    yield 2

    while True:

        for p in primes_list:
            if x % p == 0:
                break

            else:
                primes_list.append(x)
                yield x

        x += 2
