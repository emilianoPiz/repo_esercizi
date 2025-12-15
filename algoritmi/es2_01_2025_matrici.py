""" Esercizio 2 (10 punti): Sia dato un array E di n coppie di interi
del tipo (i, e), in cui il primo elemento di ciascuna coppia i è
un indice tra [0 , n−1] assegnato ad una persona, ed il secondo
elemento e rappresenta l’età della persona di indice i; sia poi
data una matrice quadrata e simmetrica A di dimensione n×n
a valori 0 ed 1 in cui A[j, k] = A[k, j] é uguale ad 1 se e solo se
la persona di indice j conosce la persona di indice k.
Si scriva un algoritmo il più efficiente possibile che ve-
rifichi se esiste almeno una coppia di conoscenti coetanei.

Si scriva lo pseudocodice opportunamente commentato del-
l’algoritmo progettato e se ne calcoli formalmente il costo
asintotico."""

# soluzione
# per rispondere alla domanda bisogna necessariamente controllare ogni casella di A
# la lunghezza di A è n. quindi per controllare tutte le caselle ci vogliono almeno n^2 passi
# indicizzare le età in un array dove ogni indice corrisponde alla propria età 
#  prima di iniziare a chiederci quali amici hanno la stessa età permette di accedere a questa informazione in tempo costante 

""" 
    il costro dell'algoritmo proposto è pari a T(n)= O(n^2)+Θ(n)+costanti_varie
    sapendo che il costo asintotico totale tra due funzioni sommate tra di esse è max(f(x),g(x))
    max(O(n^2),Θ(n))= O(n^2)     
"""  

def check_coetanei(A,E):
    v=[]
    n=len(A)
    
    #inizio for:
    for i, e in E:
        v[i]=e
    #costo complessivo Θ(n)
    
    ##inizio for annidato
    for j in range(0,n):
        for k in range(0,n):
            if A[j,k]==1:
                if v[j] == v[k]:
                    return (j,k)
    ##costo complessivo O(n^2)
    
    return (0,0)   

