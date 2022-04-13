def insertion_sort(li):
    n = len(li)

    for i in range(1, n):
        key = li[i]
        j = i - 1
        while j >= 0 and key < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = key

    return li
