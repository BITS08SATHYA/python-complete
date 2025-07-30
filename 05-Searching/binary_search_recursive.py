def binary_search_recurisve(list, target, left, right):
    if left > right:
        return 'Not Found'
    else:
        middle = (left + right) // 2
        if target == list[middle]:
            return middle
        elif target < list[middle]:
            # right = middle - 1
            return binary_search_recurisve(list, target, left, middle -1)
        else:
            return binary_search_recurisve(list, target , middle + 1 , right)






list = [1,2,3,4,5,6]
target = 5
left = 0
right = len(list) - 1
print(binary_search_recurisve(list, target, left, right))