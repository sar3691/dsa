def merge_sort(a):
    if len(a) <= 1:
        return a

    m = len(a) // 2
    L = merge_sort(a[:m])
    R = merge_sort(a[m:])

    return merge(L, R)


def merge(L, R):
    i = j = 0
    res = []

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1

    return res + L[i:] + R[j:]


# Input
a = list(map(int, input("Enter numbers: ").split()))
print("Sorted:", merge_sort(a))
