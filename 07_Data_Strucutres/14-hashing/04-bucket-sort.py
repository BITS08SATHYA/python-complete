import math

from LinkedList import LinkedList
def bucketSort(A):
    n = len(A)
    max_element = max(A)
    l = []
    buckets = [l] * 10

    for i in range(n):
        j = math.floor(n * (A[i] / (max_element + 1)))  # index computation
        if buckets[j] == 0:
            buckets[j] = A[i]
        else:
            buckets[j].append(A[i])
    for i in range(10):
        insertionSort(buckets[i])
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            A[k] = buckets[i].pop(0)
            k += 1

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position - 1] > cvalue:
            A[position] = A[position - 1]
            position -= 1
        A[position] = cvalue

A = [54, 78, 64, 92, 81, 60, 86, 28]
print("Original array:", A)
bucketSort(A)
print("Sorted array:", A)