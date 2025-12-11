# In un array ordinato A di n interi compaiono tutti gli interi 
# da 0 ad n−2. Esiste dunque nell’array un unico elemento duplicato.
# Si progetti un algoritmo ITERATIVO che, dato A, in tempo Θ(log n) 
# restituisca l’elemento duplicato.

# Dell’algoritmo proposto:
# a) si scriva lo pseudocodice opportunamente commentato;
# b) si giustifichi il costo computazionale.

# Soluzione:
# sapere che i dati sono ordinati apre la strada al binary search,
# inoltre sappiamo che il duplicato interomperà la corrispondenza tra l'indice e l'elemento a quell'indice


def bin_search_duplicate(A):
    ret = None

    i=0
    j=len(A)-1
    while i < j:
        mid=(i+j)//2
        if A[mid] == mid:
            i = mid + 1
        else:
            j = mid

    return A[i]


# TEST 
A = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,14 ]
print(f"A "+str(bin_search_duplicate(A)))
B = [ 0, 1, 2, 3, 4, 4, 5, 6, 7 ]
print(f"B "+str(bin_search_duplicate(B)))
C = [ 0, 0, 1, 2, 3, 4, 5, 6, 7 ]
print(f"C "+str(bin_search_duplicate(C)))
D = [ 0, 1, 1 ]
print(f"D "+str(bin_search_duplicate(D)))