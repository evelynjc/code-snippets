def bubble_sort(li):
    n = len(li)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

    return li
