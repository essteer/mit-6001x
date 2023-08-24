# 1) pick an index, i, that divides list in half
# 2) ask if L[i] == e
# 3) if not, ask if L[i] is larger or smaller than e
# 4) depending on answer, search left or right half of L for e

# keep reducing size of problem
# finish looking through list when 1 = n/2**i
# so i = log n
# complexity is O(log n), where n is len(L)

# Implementation version 1 - complexity O(n log n)
def bisect_search1(L, e):
    if L == []:  # O(1)
        return False
    elif len(L) == 1:  # O(1)
        return L[0] == e
    else:
        half = len(L)//2  # O(1)
        if L[half] > e:
            return bisect_search1(L[:half], e)  # not constant
        else:
            return bisect_search1(L[half:], e)  # not constant

# if and elif base cases are constant - O(1)
# half = len(L)//2 is constant O(1)

# not constant due to making copy of half of the list
# complexity is O(n log n)
