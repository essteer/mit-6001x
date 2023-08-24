def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True  # could be sped up slightly by returning True here, but doesn't affect worst case
    return found

# must look through all elements to decide it isn't there
# O(len(L)) for the loop * O(1) to test if e == L[i]
# overall complexity is O(n) - where n is len(L)
