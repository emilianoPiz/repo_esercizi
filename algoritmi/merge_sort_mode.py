def merge_sort(A,mode):
    #orders an array in Θ(n log(n))
    # mode: 0 for descending order
    # mode: 1 for ascending order  
    if mode == 1:
        A=merge_sort_asc(A)
    else:
        A=merge_sort_desc(A) 
    return A

def merge_sort_desc(A):
    if len(A)>1:
        r = merge_sort_desc(A[: len(A) // 2])
        l = merge_sort_desc(A[len(A) // 2 :])
        i,k,j = 0,0,0
        while i < len(r) and j < len(l):
            if r[i]<l[j]:
                A[k]=r[i]
                i+=1
            else:
                A[k]=l[j]
                j+=1       
            k+=1
        while i < len(r):
            A[k]=r[i]
            i+=1
            k+=1
        while j < len(l):
            A[k]=l[j]
            j+=1
            k+=1
    return A

def merge_sort_asc(A):
    if len(A)>1:
        r = merge_sort_asc(A[: len(A)//2])
        l = merge_sort_asc(A[len(A)//2 :])
        i,k,j = 0,0,0
        while i < len(r) and j < len(l):
            if r[i]>l[j]:
                A[k] = r[i]
                i+=1
            else:
                A[k] = l[j]
                j+=1       
            k+=1
        while i < len(r):
            A[k] = r[i]
            i+=1
            k+=1
        while j < len(l):
            A[k] = l[j]
            j+=1
            k+=1
    return A

A =[34,234,1,23,7,41,2,2456,3225,347,43,345,4,677]

print(A)
merge_sort(A,0)
print(A)


A =[34,234,1,23,7,41,2,2456,3225,347,43,345,4,677]

print(A)
merge_sort(A,1)
print(A)