def bubble_sort(L):
    iterations = 0
    total_swaps = 0
    swap = True
    k = 0
    while swap:
        swap = False
        for i in range(1, len(L)-k):            
            iterations += 1
            if L[i-1] > L[i]:
                swap = True
                (L[i-1], L[i]) = (L[i], L[i-1])
                total_swaps += 1
        k += 1

    return (iterations, total_swaps)

L = [20, 13, 77, 61, 74, 5, 9, 8, 10, 5]
(iterations, swaps) = bubble_sort(L)
print(L)
print("List of length {0} sorted in {1} iterations and {2} swaps".format(len(L), iterations, swaps))


