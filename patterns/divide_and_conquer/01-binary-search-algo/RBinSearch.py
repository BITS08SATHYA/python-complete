def RBinSearch(a, l, r, key):
    if l == r:
        if key == a[l]:
            return l
        else:
            return 0
    else:
        mid = (l + r) // 2
        if key == a[mid]:
            return mid, a[mid]
        elif key < a[mid]:
            return RBinSearch(a, l , mid - 1, key)
        else:
            return RBinSearch(a, mid+1, r, key)


a = [15, 28,37,45,54,63,78,86,92]
print(RBinSearch(a, 0, len(a), 37))