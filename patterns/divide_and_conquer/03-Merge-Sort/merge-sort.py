def merge(a, b, low, mid, high):
    h = low
    i = low
    j = mid + 1

    # main merge loop
    while h <= mid and j <= high:
        if a[h] <= a[j]:
            b[i] = a[h]
            h += 1
        else:
            b[i] = a[j]
            j += 1
        i += 1

    # Copy call
    if h > mid:
        for k in range(j, high + 1):
            b[i] = a[k]
            i += 1
    else:
        for k in range(h, mid + 1):
            b[i] = a[k]
            i += 1

    # Copy back into a[low...high]
    for k in range(low, high + 1):
        a[k] = b[k]


def merge_sort(a):
    if not a or len(a) < 2:
        return a
    b = [0] * len(a)

    def sort(low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid + 1, high)
        merge(a,b, low, mid, high)

    sort(0, len(a)-1)
    return a

arr = [38, 27, 43, 3, 9, 82, 10, 99]
print(merge_sort(arr))
