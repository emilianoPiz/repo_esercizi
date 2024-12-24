# -*- coding: utf-8 -*-

# I numeri di Tribonacci sono come i numeri di Fibonacci, ma ogni numero è funzione dei tre numeri
# di Tribonacci precedenti (anziché solo dei due precedenti come in Fibonacci).
# Ad esempio, tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3).
# tribonacci(0) = tribonacci(1) = 0
# tribonacci(2) = 1
# Scrivere una funzione ricorsiva che dato n, restituisca l'n-esimo numero di Tribonacci
def tribonacci_Rec(n: int):
    if n ==0:
        return n
    elif n == 1 or n == 2:
       return 1  
    else:
        return tribonacci_Rec(n-1) + tribonacci_Rec(n-2) + tribonacci_Rec(n-3)
    
def tribonacci_iter(n):
    if n == 0:
        return 0  # Base case for T(0)
    elif n == 1 or n == 2:
        return 1  # Base cases for T(1) and T(2)
    terzultimo, penultimo, ultimo = 0, 1, 1 
    for _ in range(3,n +1):
        next_value = terzultimo + penultimo + ultimo
        terzultimo, penultimo, ultimo = penultimo, ultimo, next_value
    return ultimo

def fibonacci_Rec(n):
    if n <= 1:
        return n 
    else:
        return fibonacci_Rec(n-1) + fibonacci_Rec(n-2) 
    

# Scrivere una funzione ricorsiva che data una lista di interi, restituisca il massimo
# Non usare cicli for/while
# Non puoi usare le funzioni max - min 
def max_recursive(l: list[int]) -> int:
    #caso base, la lista è vuota ed è rimasto solo il maggiore
    if len(l) == 1:
        return l[0]
    #eccezione: è stata passata una lista vuota
    elif not l:
        return "lista vuota impossibile trovare un massimo"
    #se non siamo nel caso base o in errore allora risolvo il problema con la ricorsione
    else:
        #paragona primo e ultimo, rimuovi il più piccolo e ripassa la lista alla funzione finchè non resta un solo elemento
        if l[0] < l[-1]:
            l.remove(l[0])
            return max_recursive(l)
        elif l[0] > l[-1]:
            l.remove(l[-1])
            return max_recursive(l)
        

# Scrivere una funzione ricorsive che calcola la somma dei numeri da 0 a n (incluso)
def sum_recursive(n: int) -> int:
    #caso base è la somma di 0+1
    if n ==0:
        return  0
    else:
        return n+ sum_recursive(n-1)
    


# Scrivere una funzione ricorsiva che calcoli la potenza di un numero,
# utilizzando la seguente formula: power_recursive(base, exp) = base * power_recursive(b, exp-1)
# Non potete usare pow(...) o l'operatore **
def power_recursive(base: int, exp: int) -> int:
    #caso base: esponente uguale 1 allora torna la base (perchè qualsiasi intero elevato a 1 è in output lo stesso intero)
    if exp ==0:
        return 1
    else:
        return base * power_recursive(base, exp-1)

# Scrivere una funzione ricorsiva che prende in input una stringe e restituisce
# la stringa invertita (ad esempio, "ciao" - > "oaic").
# Le uniche operazioni su stringhe permesse sono la concatenazione fra stringhe e lo slicing.
def reverse_recursive(s: str) -> str:
    #caso base la stringa è vuota  
    if len(s) == 0:
        return s
    else:
        result = s[-1:] + reverse_recursive(s[:-1])
        return  result

        


# Scrivere una funzione ricorsiva che controlla se un numero è un numero primo
# (controllando che non sia divisibile per tutti i numeri precedenti ad esso).
# La funzione prende in input il numero n da controllare, ed un divisore d (all'inizio d==2)
def is_prime_recursive(n: int, d=2) -> bool:
    if n == d:
        return True
    elif n % d ==0 :
        return False
    else:
        return is_prime_recursive(n, d +1)


# La Torre di Hanoi (anche conosciuta come Torre di Lucas dal nome del suo inventore)
# è un rompicapo matematico composto da tre paletti e un certo numero di dischi di
# grandezza decrescente, che possono essere infilati in uno qualsiasi dei paletti.
# Il gioco inizia con tutti i dischi incolonnati su un paletto in ordine decrescente,
# in modo da formare un cono. Lo scopo del gioco è portare tutti i dischi su un paletto diverso,
# potendo spostare solo un disco alla volta e potendo mettere un disco solo su un altro disco più grande,
# mai su uno più piccolo.
# La soluzione base del gioco della torre di Hanoi si formula in modo ricorsivo.
#
# Siano i paletti etichettati con A, B e C, e i dischi numerati da 1 (il più piccolo) a n (il più grande).
# L’algoritmo si esprime come segue:
#
# Sposta i primi n-1 dischi da A a B. (Questo lascia il disco n da solo sul paletto A)
# Sposta il disco n da A a C
# Sposta n-1 dischi da B a C
#
# Scrivere una funziona che calcola il numero minimo di mosse necessarie per spostare
# gli n dischi da uno paletto all’altro.
def hanoi_moves(n: int) -> int:
    #il numero di mosse è pari a 2^n-1
    if n == 1:
        return 1
    else:
        return 2 * hanoi_moves(n - 1) +1
    
    
    
# Nota: esercizio difficile
# Scrivere una funzione che risolve il problema dello zaino.
# Dato una lista di tuple l=[(w0, v0), (w1, v1), ...], dove wi è
# il peso in kg dell'oggetto i-esimo, e vi è il suo valore in euro,
# scrivere una funzione che prenda in input la lista l, e un peso massimo W.
# La funzione deve restituire la somma dei valori degli oggetti in una lista
# r=[(wk, vk), (wj, vj), ...] contenente un sottoinsieme delle tuple di input,
# tale che la somma dei pesi sia minore o uguale a W e il valore totale (in euro)           if sum(pesi)<=W
# sia il massimo possibile

"""
massimo_valore(l, W):
    se la lista è vuota o W = 0:
        return 0
    prendi_la_prima_tupla = (se w0 <= W allora v0 + massimo_valore(lista_senza_primo, W - w0) altrimenti 0)
    non_prendere_la_prima_tupla = massimo_valore(lista_senza_primo, W)
    return max(prendi_la_prima_tupla, non_prendere_la_prima_tupla)
"""
def knapsack(l: list[tuple[int, int]], W: int) -> int:
    # Caso base: se la lista è vuota o la capacità è 0, valore = 0
    if not l or W == 0:
        return 0

    # Estrai peso e valore del primo oggetto
    peso, valore = l[0]

    # Se possiamo prendere il primo oggetto, calcoliamo il valore prendendolo
    if peso <= W:
        valore_con = valore + knapsack(l[1:], W - peso)  # lo prendo
    else:
        valore_con = 0  # non posso prenderlo

    # Calcoliamo il valore non prendendo il primo oggetto
    valore_senza = knapsack(l[1:], W)

    # Torna il massimo tra prenderlo o non prenderlo
    return max(valore_con, valore_senza)
            
    

