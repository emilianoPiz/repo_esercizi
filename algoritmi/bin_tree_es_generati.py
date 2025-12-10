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

 
# esercizio 3 Dato il puntatore r alla radice di un albero binario T (con nodi aventi campi val, left, right),
# un nodo u si dice "dominante" se il suo valore val è strettamente maggiore della somma dei valori di tutti i nodi
# nel sottoalbero radicato in u (escluso u stesso).
# Nota: Le foglie sono sempre dominanti (somma sottoalbero = 0).
# Progettare una funzione ricorsiva che restituisca il numero totale di nodi dominanti in T. 
# Il tempo di esecuzione deve essere Theta(n).
# a) Descrizione a parole dell'idea.
# b) Pseudocodice (senza variabili globali!).
# c) Giustificazione del costo.

def nodi_dominanti(r):
    if r == None:
        return (0,0)
    
    (somma_sx, count_sx) = nodi_dominanti(r.left)
    (somma_dx, count_dx) = nodi_dominanti(r.right)
    
    sum_tot_sub = somma_sx + somma_dx
    current_sum = sum_tot_sub + r.val
    count       = count_dx +count_sx
    
    if r.val < sum_tot_sub:
        count = count + 1
        
    return (current_sum,count)
    