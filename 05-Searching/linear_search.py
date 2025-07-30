def linear_search(list, target):
    # for index,value in enumerate(list):
    #     if value == target:
    #         return index
    # return -1

    idx = 0
    while idx < len(list):
        if list[idx] == target:
            return idx
        idx = idx + 1
    return -1


list = [1,2,3,4,5]
target = 4
# linear_search(list, target)
print(linear_search(list, target))