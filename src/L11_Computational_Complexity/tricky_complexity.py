def h(n):
    """assume n an int >= 0"""
    answer = 0
    s = str(n)
    for c in s:  # linear O(len(s)) - but what in terms of input n?
        answer += int(c)
    return answer

# convert integer to string
# iterate over length of string, not magnitude of input n
# think of it like dividing n by 10 with each iteration
# although it is linear in the length of the string (s),
# it is O(log n) - the base does not matter
