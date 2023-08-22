# Provide an expression using applyToEach, so that after evaluation testList has the indicated value.
# >>> print(testList)
# [1, 4, 8, 9]

testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

    return L


print(applyToEach(testList, abs))
