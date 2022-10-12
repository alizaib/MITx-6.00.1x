def generate_all_subsets(L):
    if len(L) == 0:
        return [[]]

    smaller = generate_all_subsets(L[:-1])
    last_item = L[-1:]
    new = []
    for small in smaller:
        new.append(small + last_item)
    return smaller + new

L = [1, 2, 3]
L_all = generate_all_subsets(L)

print(L_all)

