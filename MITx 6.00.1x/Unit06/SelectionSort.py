def selection_sort(L):
    iterations = 0
    total_swaps = 0
    for i in range(0, len(L)):
        for j in range(i, len(L)):
            iterations += 1
            if L[i] > L[j]:
                total_swaps += 1
                L[i], L[j] = L[j], L[i]
    return (iterations, total_swaps)

L = [20, 13, 77, 61, 74, 5, 9, 8, 10, 5]
(iterations, swaps) = selection_sort(L)
print(L)
print("List of length {0} sorted in {1} iterations and {2} swaps".format(len(L), iterations, swaps))