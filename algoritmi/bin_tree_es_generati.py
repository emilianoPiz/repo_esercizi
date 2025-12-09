# Esercizio: Verifica di un Cammino Strettamente Crescente
# Testo del problema: Dato il puntatore r al nodo radice di un albero binario 
# contenente valori interi, progettare un algoritmo ricorsivo che determini  
# in tempo θ(n) se esiste almeno un cammino radice-foglia in cui i valori dei nodi 
# sono strettamente crescenti.

def path_incr(r):
    
    if r == None:
        return False
    
    path_sx = False
    path_dx = False

    if r.value < r.left.key and r.left is not None:
        path_sx = path_incr(r.sx)

    if r.value < r.right.key and r.right is not None:
        path_dx = path_incr(r.dx)

    return path_dx or path_sx

# Esercizio: Somma del Cammino (Path Sum)
# Dato il puntatore r al nodo radice di un albero binario contenente valori interi
# e un numero intero target, progettare un algoritmo ricorsivo che determini 
# in tempo  Θ(n) se esiste un cammino radice-foglia tale che la somma di 
# tutti i valori dei nodi lungo il cammino sia esattamente uguale a target.


def path_sum(r,target,s=0):
    if r == None:
        return False
    s += r.value
    if r.left is None and r.right is None:
        return s == target
    return path_sum(r.left,target,s) or path_sum(r.right,target,s)