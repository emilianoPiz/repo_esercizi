""" Esercizio 2 (10 punti):
     Sia data una collezione C di n interi compresi tra 0 a 50
    tra cui sono certamente presenti dei duplicati. Gli elementi
    della collezione sono memorizzati in un array A. Si vuole de-
    terminare la distanza massima tra le posizioni di due elementi
    duplicati in A, cioè il massimo al variare di x ∈ C di max(j− i),
    t.c. A[i] = x e A[j] = x.
    1
    Ad esempio per A = [3, 3, 4, 6, 6, 3, 5, 5, 5, 6, 6, 9, 9, 1] gli ele-
    menti che in A si ripetono sono 3, 5, 6 e 9.
    La distanza massima tra i duplicati del 3 è 5 (j = 5 e i = 0),
    la distanza massima tra i duplicati del 5 è 2 (j = 8, i = 6),
    la distanza massima tra i duplicati del 6 è 7 (j = 3 e i = 10),
    la distanza massima tra i duplicati del 9 è 1 (j = 12 e i = 11).
    quindi la risposta per l’array A è 7.
    Progettare un algoritmo che, dato A, in tempo Θ(n) restituisca
    la distanza massima tra le posizioni con elementi duplicati.
    Dell’algoritmo proposto:
    a) si scriva lo pseudocodice opportunamente commentato;
    b) si giustifichi il costo computazionale.
"""

# soluzione: per trovare la massima distanza bisogna prima di tutto capire il primo e 
# l'ultimo indice di ciascun duplicato, la loro differenza assoluta è la distanza massima tra due duplicati.
# quindi useremo due liste, inizializzate preventivamente con 50 elementi None (operazione costante), 
# al posto di None scriveremo, in una lista, i valori della prima comparsa di un numero in A
# nell'altra, scriveremo ogni volta il risultato, cosi che alla fine del loop 
# gli indici salvati in last saranno le ultime comparse degli interi.)
# il costo di questo algoritmo è lineare alla dimensione di A, 
# rispettando la richiesta (esegue solo un for di n iterazioni, gli altri costi sono costanti)

def longest_duplicate(A):
    first=[None]*50
    last =[None]*50

    for i in range(0,len(A)):
        if first[A[i]] is None: 
            first[A[i]]=i
        last[A[i]]=i

    dist = 0
    for i in range(0,49):
        if first[i] is not None and last[i] is not None:
            if last[i]-first[i] > dist:
                dist = last[i]-first[i]

    return dist

#Test
A = [3, 3, 4, 6, 6, 3, 5, 5, 5, 6, 6, 9, 9, 1]
print(longest_duplicate(A))
