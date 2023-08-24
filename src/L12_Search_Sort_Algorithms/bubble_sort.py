# compare consecutive pairs of elements
# swap elements in pair so smaller is first
# once end of list reached, start again
# stop when no more swaps have been made

def bubble_sort(L):
    swap = False
    # outer loop for multiple passes until no more swaps, O(len(L))
    while not swap:
        swap = True
        print(L)
        for j in range(1, len(L)):  # inner loop is for comparisons, O(len(L))
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


test = [1, 5, 3, 8, 4, 2, 9, 6]

# O(n**2), since we have two O(len(L)) loops
# quadratic complexity
