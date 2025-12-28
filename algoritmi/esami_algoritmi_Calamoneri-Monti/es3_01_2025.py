"""
    ES2
    Sia dato un array E di n coppie di interi
    del tipo (i, e), in cui il primo elemento di ciascuna coppia i è
    un indice tra 0 ed n-1 assegnato ad una persona, ed il secondo
    elemento e rappresenta l’età della persona di indice i; 
    sia poi data una matrice quadrata e simmetrica A di dimensione n x n
    a valori 0 ed 1 in cui A[j, k] = A[k, j] é uguale ad 1 se e solo se
    la persona di indice j conosce la persona di indice k.
    Si scriva un algoritmo il più efficiente possibile che ve-
    rifichi se esiste almeno una coppia di conoscenti coetanei.
    L’algoritmo dovrebbe dare in output una coppia con gli indici1
    dei due conoscenti coetanei se ce ne sono, oppure la coppia (0,0).
"""

# soluzione: sicuramente bisognerà scorrere la matrice contenente le informazioni sulle relazioni
# di conoscenza tra gli indici, e poi bisogna avere accesso costante all'età di una persona una volta
# ottenuto il suo indice, per fare questo, bisogna scomporre le compie in un array lungo n 
# dapprima sarà popolato con elementi None e poi metterà all'i-esimo indice l'età di quella persona
# il costo sarà O(n^2)+Θ(n), che in notazione asintotica risulta essere il massimo tra 
# O(n^2) e θ(n), quindi O(n^2).

def coetanei(E,A):
    #dichiaro l'array con i valori None al posto dell'età
    #θ(1)
    età=[None]*len(E)
    n = len(E)
    #estraggo le età dalle coppie mettendole come elemento all'i-esimo indice (i rappresenta la persona)
    #Θ(n)
    for i,e in E:
        età[i]=e
    
    # itero tutta la matrice delle relazioni di conoscenza, esco dall'algoritmo appena è soddisfatta la
    # condizione di essere conoscenti ( A[i][j]==1 ) e di essere coetanei ( if età[i] == età[j] )
    # Θ(n^2)
    for i in range(n):
        for j in range(n):
            if A[i][j]==1:
                if età[i] == età[j]:
                    return (i,j)
    #se non esco mai, significa che non esistono conoscenti coetanei e ritorno (0,0)
    return (0,0)

E = [(2,35),(1,31),(3,35),(0,35)]
A = [[0,1,0,1],[1,0,1,0],(0,1,0,0),[1,0,0,0]]
print(coetanei(E, A))

"""
    ES3
    Sia T un albero binario radicato memorizzato tramite record e puntatori. 
    L’albero è non vuoto e ogni nodo contiene un valore intero come chiave. 
    definiamo il costo di un cammino radice-foglia come la somma delle chiavi
    dei nodi che compongono il cammino.
    Si progetti un algoritmo ricorsivo per trovare il valore mi-
    nimo del costo di un cammino radice-foglia in un albero T
    dato in input tramite il puntatore alla sua radice.
"""

#soluzione: applicando un ragionamento divide et impera al problema è possibile
#suddividerlo in 3 fasi principali, 
# 1) se siamo sul nodo foglia, dobbiamo solo tornare il nostro valore
# 2) se siamo un nodo dobbiamo prima capire qual'è il minore cammino dai nostri figli
# 3) una volta capito il minore possiamo eseguire la somma del nostro valore
#      con il cammino minore e ritornare il risultato

def check_min_path(r):
    # caso base
    if r.left is None and r.right is None:
        return r.key
    #passo ricosivo
    s_sx = check_min_path(r.left)
    s_dx = check_min_path(r.right)
    # controllo quale dei due path sottostanti è minore
    if s_sx < s_dx:
        #ritorno il minore più il valore corrente
        return r.key + s_sx
    #ritorno il minore più il valore corrente
    return r.key + s_dx