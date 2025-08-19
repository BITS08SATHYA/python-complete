from Heap01 import Heap

def heapSort(A):
    H = Heap()
    n = len(A)
    for i in range(n):
        H.insert(A[i])
    k = n - 1
    for i in range(H._csize):
        A[k] = H.deleteMax()
        k -= 1

A = [25, 14, 2, 20, 10, 40]
heapSort(A)
print(A)