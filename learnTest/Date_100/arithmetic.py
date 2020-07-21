def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        mindex = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[mindex]):
                mindex = j
        items[i], items[mindex] = items[mindex], items[i]
    return items
    pass


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items)-1):
        for j in range(10):
            pass

L = [8, 5, 4, 6, 4, 1]
L1 = select_sort(L)
print(L1)
