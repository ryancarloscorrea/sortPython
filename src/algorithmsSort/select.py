def parttition(A, p,r):
    x = A[r]
    i = p -1
    j = p
    
    for j in range (r -1):
        if A[j]<= x:
            i = i +1
            A[i], A[j] = A[j], A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

def select (A, p, r ,i) :
    if p == r:
	    return A[p]
    q = parttition(A, p,r)
    k = q - p + 1

    if k == i:
        return A[q]
    
    if k > i  :  
        select(A, p, q -1, i)
    else:
        select(A, q + 1, r, i-k)


arr = [33, 11,22,33,44,55,88,66,77,99]
parttition(arr,1,7)

print(arr)
