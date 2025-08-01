def merge(list, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = [0] * (right + 1)
    while i <= mid and j <= right:
        if list[i] < list[j]:
            B[k] = list[i]
            i = i + 1
        else:
            B[k] = list[j]
            j = j + 1
        k = k + 1
    while i <= mid:
        B[k] = list[i]
        i = i + 1
        k = k + 1
    while j <= right:
        B[k] = list[j]
        j = j + 1
        k = k + 1
    for x in range(left, right+1):
        list[x] = B[x]


def merge_sort(list, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(list, left, mid)
        merge_sort(list, mid + 1, right)
        merge(list, left, mid, right)
    return list


list = [3,5,8,9,6,2]
print(merge_sort(list, 0, len(list) - 1))


