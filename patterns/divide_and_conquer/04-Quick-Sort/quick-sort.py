from array import array

def partition(A, p: int, r: int) -> int:
    x = A[r]          # pivot = last element in A[p..r]
    i = p - 1         # end of the "≤ pivot" zone (starts before p)
    j = p
    while j <= r - 1: # scan A[p..r-1]
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]   # place A[j] into the "≤ pivot" zone
        j += 1
    A[i+1], A[r] = A[r], A[i+1]       # put pivot right after the "≤ pivot" zone
    return i + 1                      # pivot’s final index

def quicksort(A, p: int, r: int) -> None:
    if p < r:
        q = partition(A, p, r)        # place one pivot correctly
        quicksort(A, p, q - 1)        # sort left side
        quicksort(A, q + 1, r)        # sort right side

# ---- example ----
A = [38, 27, 43, 3, 9, 82, 10]
print(A)
quicksort(A, 0, len(A) - 1)
print(list(A))  # just to display
