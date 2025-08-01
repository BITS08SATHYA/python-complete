def bubble_sort(list):
    n = len(list)
    for passes in range(n-1, 0 , -1):
        for i in range(passes):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list


list = [3,5,8,9,6,2]
print(bubble_sort(list))