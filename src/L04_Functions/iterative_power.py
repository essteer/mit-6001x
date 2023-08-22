def iterPower(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    """
    counter = 0
    ans = base

    if exp == 0:
        return 1

    while counter < (exp - 1):
        ans *= base
        counter += 1

    return ans


print(iterPower(2, 3))
