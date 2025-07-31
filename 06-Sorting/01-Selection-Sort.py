def selection_sort(list):
    for i in range(len(list)):
        position = i
        print(f'{i}-iteration')
        for j in range(i+1, len(list)):
            if list[j] < list[position]:
                list[j], list[position] = list[position], list[j]  # Swapping [a,b] = [b,a]
                print(list)
    return list
list = [3,5,8,9,6,2]
print(selection_sort(list))
