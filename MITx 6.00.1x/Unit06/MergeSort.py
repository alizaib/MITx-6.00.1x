def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]

    middle = len(L)//2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])

    return merge(left,right)

L = [20, 13, 77, 61, 74, 5, 9, 8, 10, 5]
L = merge_sort(L)
print(L)

