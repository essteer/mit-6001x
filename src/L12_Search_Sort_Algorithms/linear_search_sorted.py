# example of linear search on a SORTED list
# though bisection search would be better

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
        return False

# must only look until a number greater than e is reached
# O(len(L)) for the loop * O(1) to test if e == L[i]
# overall complexity is O(n) - where n is len(L)

# better than brute force (for a sorted list), but cost remains linear
