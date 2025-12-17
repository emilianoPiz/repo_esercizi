#somma massima di un sottoarray con K elementi
# Dato un array arr[] e un intero k, 
# dobbiamo calcolare la somma massima di un sottoarray di dimensione esattamente k .

A=[5,9, 2, -1, 0, 3]

def max_subarray_sum(A,k):
    i=j=0
    somma_r=0
    while j <= len(A):
        j=i+k
        somma = sum(A[i:j]) #TODO: è lento in python. 
        if somma > somma_r:
            somma_r=somma
        i+=1
    return somma_r

print(max_subarray_sum(A,3))