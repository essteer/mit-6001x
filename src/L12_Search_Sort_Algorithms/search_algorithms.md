# Linear search

- brute force search
- list does not have to be sorted

# Bisection search

- list must be sorted to give correct answer
- two different implementations of the algorithm contained here

# Searching a sorted list - n is len(L)

- with linear search, search for an element is O(n)
- with binary search, can search in O(log n) - assuming the list is sorted

- we should sort first when we will do repeat searches
- this amortises the cost of the sort over many searches
- SORT + K*O(log n) < K*O(n)
- for large K, SORT time becomes irrelevant
