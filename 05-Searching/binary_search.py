from math import floor


def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2  # // - integer division
        if target == list[middle]:
            return middle
        elif target < list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

list = [1,2,3,4,5,6,7,8]
target = 1
print(binary_search(list, target))
