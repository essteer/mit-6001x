# divide and conquer approach - commonly used
# 1) if len(L) == 0 or len(L) == 1, already sorted
# 2) if len(L) > 1, split into two lists, and sort each
# 3) merge sorted sublists: look at first element of each, move smaller to end of result; when one list empty, copy rest of other list

import operator


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:  # base case
        return L[:]
    else:
        middle = int(len(L)/2)
        left = merge_sort(L[:middle], compare)  # divide
        right = merge_sort(L[middle:], compare)  # divide
        return merge(left, right, compare)  # conquer with the merge step


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


# complexity
# go through two lists, but only one pass
# compare only smallest elements in each sublist
# O(len(left) + len(right)) copied elements
# O(len(longer list)) comparisons
# linear in length of the lists

# O(n log n)
# log linear complexity
