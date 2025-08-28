def IBinSearch(a, n , key):
    low = 0
    high = n

    while low < high:
        mid = (low + high) // 2
        if key < a[mid]:
            high = mid - 1
        elif key > a[mid]:
            low = mid + 1
        else:
            return mid, a[mid]

    return -1

a = [15, 28,37,45,54,63,78,86,92]
print(IBinSearch(a,  len(a), 37))