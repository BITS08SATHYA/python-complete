def linear_search(list, target):
    for index,value in enumerate(list):
        if value == target:
            return index
    return -1

list = [1,2,3,4,5]
target = 4
# linear_search(list, target)
print(linear_search(list, target))