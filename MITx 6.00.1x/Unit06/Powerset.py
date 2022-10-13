def get_power_set(L):
    if len(L) == 0:
        return [[]]

    smaller = get_power_set(L[:-1])
    last_item = L[-1:]
    new = []
    for small in smaller:
        new.append(small + last_item)
    return smaller + new

L = [1, 2, 3]
L_all = get_power_set(L)

print(L_all)

