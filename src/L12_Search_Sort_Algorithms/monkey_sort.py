# AKA bogosort, stupid sort, slowsort, permutation sort, shotgun sort
# randomly assign elements into list, then check whether they're in order
# if not, randomly assign and check again

import random


def monkey_sort(L):
    while not is_sorted(L):
        random.shuffle(L)

# best case: O(n) where n is len(L) to check if sorted
# worst case: O(?), potentially unbounded
