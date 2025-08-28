def MaxMin(a ,i, j):
    if i == j:
        return a[i], a[i]

    # Base case with 2 elements
    elif i == j - 1:
        if a[i] < a[j]:
            return a[j], a[i]
        else:
            return a[i], a[j]

    # Recursive case: divide into halves
    else:
        mid = (i + j) // 2
        max1, min1 = MaxMin(a , i , mid)
        max2, min2 = MaxMin(a, mid + 1, j)

        # custom implementation
        if max1 > max2:
            overall_max = max1
        else:
            overall_max = max2
        if min1 > min2:
            overall_min = min2
        else:
            overall_min = min1
        #
        # overall_max = max(max1, max2)
        # overall_min = min(min1, min2)

        return overall_max, overall_min

# Example Usage
arr = [3, 5, 1, 8, 9, 2, 10, 7]
maximum, minimum = MaxMin(arr, 0, len(arr) - 1)
print("Max:", maximum)
print("Min:", minimum)

