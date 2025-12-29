"""
    Sia dato un array A di interi. Si scriva
    un algoritmo che restituisca True se A rappresenta uno heap
    minimo e False altrimenti.
"""

#soluzione: una lista rappresenta un heap minimo quando il valore di ogni padre è inferiore
# al valore dei suoi figli.
# per questo bisognerà iterare almeno la prima metà dell'array (in quanto la seconda metà dell'array 
# conterrà solo foglie) e chiederci ad ogni iterazione se è vero che il padre è maggiore dei suoi
# figli, la prima volta che questo avverà torneremo False, se ciò non avverrà allora torneremo True, 
# l'algoritmo ha quindi costo lineare rispetto alla lunghezza di A O(n).
# dichiarerò anche le funzioni helper sx e dx per accedere all'elemento (operazione costante)

def sx(i):
    return i*2
def dx(i):
    return sx(i)+1
def parent(i):
    return i//2

def es2(A):
    n = len(A)
    for i in range(n//2):
        if A[i] > A[sx(i)] or A[i]> A[dx(i)]:
            return False
    return True 
A=[1,3,5,7,9,11,13]
print(es2(A))

"""
    ES3
    Siano dati in input un valore intero
    M ed il puntatore r alla testa di una lista concatenata i cui
    record sono costituiti da un campo key con valori interi e da
    un campo next contenente un puntatore al record successivo.
    Si progetti un algoritmo ricorsivo che dia in output la som-
    ma di tutte le chiavi della lista concatenata che siano multipli
    di M, senza modificare la lista.
    Ad esempio, se M = 3 e la lista puntata da L è la seguente:
    L → 3 → 1 → 9 → 2 → 8 → 6/
    l’output dovrà essere 18, in quanto le chiavi che risultano
    essere multiple di 3 sono -nell’ordine- 3, 9 e 6.
"""

def ES3(M,r):
    if r == None:
        return 0
    somma = ES3(M,r.next)
    if r.key %M ==0:
        somma += r.key
    return somma

