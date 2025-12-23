# Dato un array A di n interi, si scriva un algoritmo iterativo
# MaxSequenzaElementiUguali che calcoli il numero di elementi
# della più lunga porzione di A costituita interamente da elementi
# consecutivi uguali tra loro.
# Ad esempio, se A = [5, 7, 3, 3, 8, 9, 9, 9, 5, 3, 2, 2], allora la risposta è 3
# in quanto la porzione [9, 9, 9] è la più lunga formata da elementi
# consecutivi tutti uguali.


#soluzione: per risolvere il problema è necessario verificare per quante iterazioni 
# la proprietà di uguaglianza è verificata.
# quindi servirà un contatore che verrà resettato ogni volta che la sequenza si interrompe, e un secondo che
# terrà conto del record massimo di iterazioni successive in cui la condizione è verificata, quest'ultimo verrà tornato.
def es2(A):
    if not A:
        return "empty list given"
    if len(A)==1:
        return 1
    
    max_d=1
    d=1

    for i in range (1,len(A)): # costo computazionale temporale: Θ(n)
        if A[i]==A[i-1]:
            d +=1
        else:
            d = 1    
        if d >= max_d:
            max_d=d
    return max_d     

#TEST
A = [5, 7, 3, 3, 8, 9, 9, 9, 5, 3, 2, 2]
print(es2(A))

# Dato un albero binario non vuoto a valori interi T ed un suo
# nodo v, il costo del cammino radice-v è definito come la somma
# dei valori dei nodi nel percorso che va dalla radice al nodo v
# (estremi inclusi).
# Vogliamo calcolare il costo del massimo cammino radice-
# foglia di T.

# soluzione: l'idea è che ci servirà per prima cosa contare la somma di tutti i nodi
# risalendo nella ricorsione invece dovremmo scegliere quale tra le due somme è maggiore
# il caso base è raggiunto quando siamo su un foglia, torneremo key da li
# il nodo superiore dovrà sommare e scegliere tra la somma del suo figlio desto e sinistro 
# poi passarla sopra

def es3(r):
    if r is None:
        return 0 
    if r.left==None and r.right==None:
        return r.key
    
    val_dx = es3(r.right)
    val_sx = es3(r.left)

    if val_sx < val_dx:
        sum_t=val_dx+r.key
    else:
        sum_t=val_sx+r.key

    return sum_t
