# O(c**n) - exponential complexity
# recursive functions with >1 recursive call for each size of problem
# many important problems inherently exponential, cost therefore high
# will lead to consideration of approximate solutions

def gen_subsets(L):
    res = []
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = gen_subsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create list of just last element
    new = []
    for small in smaller:
        # for all smaller solutions, add one with last element
        new.append(small + extra)
    return smaller + new  # combine those with last element and those without


test = [1, 2, 3, 4]

super = gen_subsets(test)

# the above is an excellent solution in terms of code, but exponentially expensive

# assuming append is constant time
# time includes time to solve smaller problem,
# plus time needed to make a copy of all elements in smaller problem

# the size of smaller is important
# we know that for a set of size k, there are 2**k cases
# so to solve need 2**n-1 + 2**n-2 + ... + 2**0 steps
# this is O(2**n) - exponential complexity
