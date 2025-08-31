def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1


def quickSelect(A,p,r,k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    i = q - p + 1
    if k == i:
        return A[q]
    elif k < i:
        return quickSelect(A, p, q-1, k)
    else:
        return quickSelect(A, q + 1, r, k - 1)

A = [38, 27, 43, 3, 9, 82, 10]
k = 3
print(f"{k}-th smalles is ", quickSelect(A, 0, len(A) - 1, k))