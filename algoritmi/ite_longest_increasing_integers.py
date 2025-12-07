# Si scriva lo pseudocodice, opportunamente commentato, di una funzione iterativa che, preso in
# input un array A di interi, trovi la lunghezza massima delle
# sequenze crescenti presenti nell’array e la restistuica come intero. 
# tempo massimo consentito: O(n)
# spazio massimo consentito = θ(1) -> non si possono usare strutture dati 

#soluzione con puntatori (meh):

def ite_longest_increasing_integers(A):
    i = 0 
    j = 1
    d = 1
    next_val=A[j]
    d_max=1
    while j<(len(A)-1):   # il while dipende da j, che viene incrementato di 1 in ogni caso
                          # il while viene eseguito n volte dove n è la lunghezza dell'array in input
        if A[i] < next_val:
            d+=1           
            j+=1
            i+=1
            next_val=A[j]
            if d > d_max:
                d_max = d
        else:
            j+=1
            i+=1
            d=1      
            next_val=A[j]
    # a parte il while tutte le altre operazioni sono costanti        
    return d_max
A = [3, 1, 5, 2, 6, 8, 7, 1]
#T(n)= O(n)+c (la somma delle operazioni costanti eseguite)
#T(n)= è in θ(n) come da richiesta e non si utilizzano array d'appoggio
print(ite_longest_increasing_integers(A))


#soluzione 2 (più leggibile, e molto più veloce in python)
# soluzione 1 puntatori: 1.2403 secondi per n= 1,000,000
# soluzione 2: 0.6974 secondi per n= 1,000,000
def sol2(A):
    if len(A) == 0 :
        return 0

    counter_max = 1
    counter = 1 

    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            counter +=1
        else:
            counter = 1
        if counter > counter_max:
            counter_max = counter

    return counter_max
