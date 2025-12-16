"""
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