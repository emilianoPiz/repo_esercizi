# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:36:30 2024

@author: emi
gli esercizi sono presi da repository publiche,rimediati qui e li
"""

  
       
"""
# Scrivere una funzione che data una tupla (x, y, z)
# restituisca la tupla (z+1, x-1, y+2)
"""
def tuple_ex(t: tuple) -> tuple:
    if len(t)<3:
        raise "TUPLE SHOULD HAVE EXACLTY 3 ARGUMENTS"
    z,x,y = t
    return (z+1,x-1,y+2)


"""
# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
"""        
def intersect(a: list, b: list) -> list:
    risultato = []
    for elem in b:
        if elem in a:
            risultato.append(elem)
    for elem in a:
        if elem in b:
            risultato.append(elem)
            #prima di tornare mi assicuro che non ci siano termini ripetuti
    return list(set(risultato))
    #modo alternativo suggerito da gpt    
    # Usa l'intersezione dei set per calcolare i valori comuni
    #return list(set(a) & set(b))



"""
# Scrivere una funzione che data una lista contenente valori >= 0 positivi, 
# crei una nuova lista contentente soltanto gli elementi della lista 
# originale tali che soddisfano la seguente proprietà:
#    lista[i] > 2*media(lista[0:i])
# elemento è maggiore del doppio della media degli elementi contenuti nella slice [0:elemento]

# (Il primo elemento non viene quindi mai inserito)
# Ad esempio, si consideri la lista [5, 3, 10, 0]
#  Il primo elemento è 5. Non viene inserito
#  Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5.
 Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista
#  Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4. 
Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista
#  Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6.
 Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista
"""
lista = [5, 3, 10, 0]
def remove_avg(a: list) -> list:
    lista_da_tornare = []
    #se abbiamo meno di 2 elementi è inutile fare il loop
    if len(a)<2:
        return lista_da_tornare
    
    somma_cumulativa = a[0]
    
    for elem in range(1, len(a)):
        media_elementi = somma_cumulativa / elem
        if a[elem]> 2*media_elementi:
            lista_da_tornare.append(a[elem])
        somma_cumulativa += a[elem]
    return lista_da_tornare




"""
# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
   
"""
def frequency(a: list) -> list:
    occorrenze = {}
    for elem in a:
        if elem in occorrenze:
            print("PRIMA",occorrenze)
            occorrenze[elem] += 1
            print("DOPO",occorrenze)
        else:
            occorrenze[elem]=1
    result = sorted(occorrenze.items())
    
    return result



# Scrivere una funzione che restituisce True
# se la lista è palindroma, o False altrimenti
def is_palindrome(a: list) -> bool:
    if a == a[::-1]:
        return True
 
def is_pali_oneLine (a:str )-> bool:
    return a == a[::-1]        

#soluzione più efficiente per quanto riguarda la memoria
#in quanto non crea una nuova variabile in memoria
def is_pali_oneVar(a) :
    for i in range(len(a)//2):
        if a[i] != a[-i -1]:
            return False
    return True
        
"""
# Scrivere una funzione che prende in input una lista, e 
# restituisce True se la lista è ordinata in ordine
# crescente o decrescente, e False altrimenti.
# Suggerimento: fare attenzione ai valori duplicati
# Utilizzare un solo ciclo e non utilizzare sorted/sort.
"""

def is_sorted(a: list) -> bool:
    #per ogni elemento se esso è inferiore dell'elemento successivo
    crescente= True
    decrescente= True
    
    for elem in range(1, len(a)):
        if a[elem] > a[elem -1]:
            crescente = False
        if a[elem] < a[elem -1]:
            decrescente = False
    if not crescente and not decrescente:
        return False
    return True

"""
# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
"""
def is_sorted_half(a: list) -> bool:
    crescente = True
    decresente = True
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            pass

#crea una funzione che restituisce l'n-esimo numero di fibonacci
def fibonacci(n:int) -> int:
    ultimo = 1
    penultimo = 0 
    for i in range(n):
        ultimo , penultimo = ultimo + penultimo , ultimo 
    return ultimo + penultimo 

#controlla se un numero è primo in modo iterativo

def is_prime_iter(n:int)->bool:
    #per ogni numero prima di lui
    #dividi n per quel numero
    # se almeno una volta la divisione è para allora non è primo
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            return False
    return True
#controlla se è n è primo in modo ricorsivo
def is_prime_recursive(n: int, d=2) -> bool:
    if n == 1 or n == 0:
        return False
    if n < 0:
        return "insert a positive number"
    if n == d:
        return True
    elif n % d == 0:
        return False
    return is_prime_recursive(n, d+1)
#controlla stringa palindroma oneline
def is_pali(lista):
    return True if lista == lista[::-1] 
#somma tutti i numeri in una lista
def somma_numeri (lista: list) -> int:
    return sum(lista)
#converti un numero decimale in binario
def dec_to_bin(n:int)->str:
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary or "0"        
#troa il numero più grande della lista senza max
def massimo(lista:list) -> int:
    massimo = 0
    for elem in lista:
        if elem > massimo:
            massimo = elem
    return massimo        
#conta quante vocali sono presenti in una lista
def conta_vocali(stringa:str)->int:
    vocali=["a","e","i","o","u"]
    contatore = 0 
    for char in stringa:
        if char in vocali:
            contatore +=1
    return contatore
#printa n colonne di una piramide di stelle
def pyramid(n:int):
    for i in range(1,n+1):
        spazi = " "* (n-i)
        stelle = "*"* (2*i-1)
        print(spazi + stelle)
#calcola il fattoriale di un numero in modo riscorsivo    
def fattoriale_ricorsivo(n):
    if n == 1 or n ==0:
        return 1
    else:
        risultato = n*fattoriale_ricorsivo(n-1)
        return risultato
#calcola il fattoriale di un numero in modo iterativo    
def fattoriale(n:int)->int:
    risultato = 1 
    if n == 0:
        return 1 
    for i in range(1,n+1):
        risultato *= i
    return risultato
#somma tutti 
def somma_di_pari(n):
    risultato = 0 
    for i in range(n +1):
        if i % 2 == 0:
            risultato += i
    return risultato
#torna true se il numero è perfetto
def is_perfect(n):
    lista_di_divisori = []
    #se la somma di divisori è uguale ad N torna true
    for i in range(1,n+1):
        if n % i == 0 and not i == n:
            lista_di_divisori.append(i)
            print(lista_di_divisori)
    return  sum(lista_di_divisori) == n
#torna la media di una lista si interi
def average(lista:list)->float:
    if len(lista) == 0:
        return 0
    return sum(lista)/len(lista)
#quante quante volte una parola è pesente in una lista
def occorrenze(frase:str, parola:str) -> int:
    lista_parole = frase.split()
    counter = 0
    for word in lista_parole:
        if parola in lista_parole:
            counter +=1
    return counter
#torna tutti i primi in un intervallo di numeri 
def primi_in_intervallo(a,b):
    def is_prime(n:int)->bool:
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i == 0 :
                return False
        return True
    lista_da_tornare = []
    for i in range(a,b+1):
        if is_prime(i):
            lista_da_tornare.append(i)
    return lista_da_tornare
#crea una funzione che simuli il comportamento della funzione sorted 
#crescente e decrescente
def mia_sorted_crescente(lista :list)-> list:
    lista_ordinata = []
    while lista:
        minimo = min(lista)
        lista.remove(minimo)
        lista_ordinata.append(minimo)        
    return lista_ordinata
    
def mia_sorted_decrescente(lista :list)-> list:
    lista_ordinata = []
    while lista:
        massimo= max(lista)
        lista.remove(massimo)
        lista_ordinata.append(massimo)        
    return lista_ordinata
#controlla se due parole sono anagrammi               
def anagramma(A:str,B:str)->bool:
    lista_A= {x: 0 for x in A}
    lista_B= {x: 0 for x in B}

    #conta le lettere
    for x in A:
        if x in lista_A:
            lista_A[x] += 1
    for x in B:
        if x in lista_B:
            lista_B[x] += 1
    return lista_A == lista_B
#torna n-stringa quando n è 0 o superiore, e float quando è negativo    
def int_to_str_flt(n):
    if n >= 0 :
        return str(n)
    elif n <0:
        return float(-n)
    else:
        return "non hai inserito un numero"
#conta quante cifra ha un numero    
def num_digits(intero):
    return len(str(intero))


#progetta una funzione che calcoli il massimo comun divisore di due numeri 
#interi positivie lo restituisca, la funzione deve funzionare in modo ricorsivo 
def MCD_recursive(x,y):
    if x == y :
        return x
    else:
        if x > y:
            z = x-y
            return MCD_recursive(z,y)
        else:
            z = y-x
            return MCD_recursive(z,x)
#setssa di sopra ma iterativa 
def MCD_iter(x,y):
    while x!=y:
        if x > y:
            x-=y
        else:
             y-=x
    return x