# 1) pick an index, i, that divides list in half
# 2) ask if L[i] == e
# 3) if not, ask if L[i] is larger or smaller than e
# 4) depending on answer, search left or right half of L for e

# keep reducing size of problem
# finish looking through list when 1 = n/2**i
# so i = log n
# complexity is O(log n), where n is len(L)

# Implementation version 2 - more efficient version, complexity O(log n)
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):  # helper function
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:  # base case
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

# rather than making repeated copies as in implementation 1
# here we use pointers to cut down the search
# list never copied
# recursive calls are not constant, but the work within them is constant
# complexity is O(log n)
