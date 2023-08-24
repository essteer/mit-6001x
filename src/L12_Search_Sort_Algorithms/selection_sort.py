# first step: extract min element, swap with element at index 0
# subsequent steps: repeat in remaining sublists
# left portion of list is kept sorted
# at ith step, first i elements in list are sorted
# all other elements are bigger than first i elements

# 1) base case: prefix empty, suffix whole list - invariant true
# 2) induction step: move min e from suffix to end of prefix, since invariant true before move, prefix sorted after append
# 3) when exit, prefix is entire list, suffix empty, so sorted

def selection_sort(L):
    suffix_start = 0
    while suffix_start != len(L):  # outer loop executes len(L) times
        print(L)
        for i in range(suffix_start, len(L)):  # inner loop executes len(L) - i times
            if L[i] < L[suffix_start]:
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start += 1


test = [1, 5, 3, 8, 4, 9, 6, 2]

# this method avoids copying the list


# variant:
def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
