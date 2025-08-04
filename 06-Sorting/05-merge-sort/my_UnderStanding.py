def mergeSort(list, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(list, left, mid)
        print(list)
        # mergeSort(list, mid+1, right)
    return list


# def merge(list, left, mid, right):

list1 = [3,5,8,9,6,2]
print(mergeSort(list1, 0, len(list1) - 1))

# merge(list, left, mid, right)