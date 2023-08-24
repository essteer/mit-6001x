# O(n**c) - polynomial
# most common polynomial algorithms are quadratic - complexity grows with square of input size
# commonly results from nested loops or recursive function calls

def is_subset(L1, L2):
    for e1 in L1:  # element in first list
        matched = False
        for e2 in L2:  # given e1, loop over all elements in second list
            if e1 == e2:
                matched = True  # if match found, set flag to True and break
                break
        # if go through all elements with no match return False
        if not matched:
            return False
    # worst case is when L1 is a subset of L2
    return True

# outer loop is executed len(L1) times
# each iteration will execute inner loop <= len(L2) times
# O(len(L1)*len(L2))

# worst case is when L1 and L2 are the same length
# O(len(L1)**2)


def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:  # nested loop, indicative of quadratic performance
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res

# first nested loop takes len(L1)*len(L2) steps
# second loop takes at most len(L1) steps - if all L1 elements appeared in L2 (linear)
# linear term therefore overwhelmed by quadratic term
# O(len(L1)*len(L2))


# O() for nested loops
def g(n):
    """assume n >= 0"""
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# computes n**2 very inefficiently
# when dealing with nested loops, look at the ranges
# nested loops, each iterating n times
