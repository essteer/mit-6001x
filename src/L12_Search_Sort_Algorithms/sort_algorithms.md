# Monkey sort

- AKA bogo sort, stupid sort, slowsort, permutation sort, shotgun sort
- randomly assigns elements to list, then checks whether they're in order
- worst case potentially unbounded O(?)

# Bubble sort

- compare consecutive pairs of elements
- swap elements in pair so smaller is first
- once end of list reached, start again
- stop when no more swaps have been made
- worst case O(n^2)
- quadratic complexity

# Selection sort

- first step: extract min element, swap with element at index 0
- subsequent steps: repeat in remaining sublists
- left portion of list is kept sorted
- at ith step, first i elements in list are sorted
- all other elements are bigger than first i elements
- worst case O(n^2) where n is len(L)
- quadratic complexity
- time elapsed should be less than bubble sort

# Merge sort

- divide and conquer approach - commonly used
- 1. if len(L) == 0 or len(L) == 1, already sorted
- 2. if len(L) > 1, split into two lists, and sort each
- 3. merge sorted sublists: look at first element of each, move smaller to end of result; when one list empty, copy rest of other list
- log linear complexity
- O(n log n) - fastest possible for a sort algorithm
