"""
    Sia dato un array A di n interi distinti. Diciamo che un elemento A[i]$
    è un "elemento partizione" se tutti gli elementi alla 
    sua sinistra sono minori di lui e tutti gli elementi alla sua destra sono maggiori di lui.
    Si progetti un algoritmo ITERATIVO che, in tempo θ(n) e spazio ausiliario θ(1) (escluso l'input), 
    restituisca l'indice di un elemento partizione se esiste, altrimenti -1.
"""

# commento: entro nella lista e salvo l'elemento come massimo se non ho massimo corrente.
# se l'elemento corrente è minore rispetto al vecchio massimo, devo vedere anche se 
# è un massimo rispetto a destra, per fare questo dovrò fare il processo duale rispetto a sopra. 
# problemi: se il primo candidato è effettivamente elemento di partizione l'algoritmo sarà lineare
# se ogni candidato invece sarà scartato alla fine sarà n^2
A = [2, 1, 3, 4, 8, 7, 9]
def es2(A):
    n = len(A)

    if n == 0: 
        return -1
    
    i = 0
    max_sinistra = -float('inf') 

    while i < n:
        if A[i] <= max_sinistra:
            i += 1
            continue
        
        j = i + 1
        failed = False
        while j < n:
            if A[j] < A[i]: 
                failed = True
                max_sinistra = A[i] 
                i = j 
                break
            j += 1
            
        if not failed:
            return i 
        
       
    return -1   

# print(es2(A))

"""
    Sia T un albero binario i cui nodi memorizzano valori interi. Un nodo si definisce "Somma-Perfetto" se il valore in esso contenuto 
      esattamente uguale alla somma dei valori contenuti nel suo sottoalbero sinistro e nel suo sottoalbero destro. 
      (Nota: il valore di un sottoalbero vuoto è 0).
      
      Scrivere in pseudocodice un algoritmo efficiente che, ricevuto il puntatore alla radice dell'albero, restituisca il numero di nodi "Somma-Perfetti" presenti in T.
      Analizzare la complessità temporale e spaziale dell'algoritmo proposto in funzione del numero di nodi n dell'albero.

"""

# commento: la proprietà che rende un nodo somma_perfetto è che r.key == somma_sx + somma_dx
#           ogni volta che la proprietà è soddisfatta bisogna incrementare di 1 un counter 
#.          quindi ogni nodo deve tener conto della sua somma e del suo counter
#           
def somma_perfetto(r):
    if r == None:
        return (0,0)
    
    (sum_dx, count_dx) = somma_perfetto(r.right)
    (sum_sx, count_sx) = somma_perfetto(r.left)
    
    count_curr=count_dx+count_sx
    sum_curr = sum_sx + sum_dx +r.key

    if r.key == sum_dx + sum_sx:
        count_curr+=1

    return (count_curr,sum_curr)
#FINE

#[Array] Il Leader: Dato un array A di n interi, 
# un elemento è "Leader" se è maggiore della somma di tutti gli elementi alla sua destra. 
# Scrivere un algoritmo O(n) che stampi tutti i leader.
A=[4,234,6,7,876,456,5]
def print_leaders(A):
    n=len(A)
    if n==0: print("empty list given")
    sum_cur = 0
    for i in range(n-1, -1, -1):
        if sum_cur < A[i]:
            print(A[i])
        sum_cur+=A[i]
print_leaders(A)  


#[Matrici] Serpente a Sonagli: Data una matrice M di dimensioni n x n, 
# stamparne gli elementi seguendo un percorso a "serpente" 
# (prima riga da sinistra a destra, seconda da destra a sinistra, terza da sinistra a destra, ecc.)
# in O(n^2).
M=[[23,345,55],[34,23,35],[12,21,11]]
def print_serpente(M):
    n = len(M[0])
    if n==0: print("")

    for i in range(n):
        if i%2==0:
            j=0
            s=""
            while j < n:
                s+= str(M[i][j]) +"-"
                j+=1
            print(f"[{s}]\n")
        else:
            j=n-1
            s=""
            while j > -1:
                s+= str(M[i][j])+"-"
                j-=1
            print(f"[{s}]\n")

print_serpente(M)