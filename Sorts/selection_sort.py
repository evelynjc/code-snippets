def selection_sort(li):
    n = len(li)

    for i in range(n - 1):
        min_val = min(li[i:])
        min_idx = li.index(min_val)
        if li[i] != min_val:
            li[i], li[min_idx] = li[min_idx], li[i]

    return li
