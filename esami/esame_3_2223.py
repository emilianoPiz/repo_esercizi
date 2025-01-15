#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame e' necessario soddisfare tutti i seguenti vincoli:
    - risolvere almeno 3 esercizi di tipo func; AND
    - risolvere almeno 1 esercizio di tipo ex; AND
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.
Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""
nome       = ""
cognome    = ""
matricola  = ""


#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci
# corrispondenti ai test che non si vogliono eseguire all'interno della lista
# `test` alla FINE di `grade.py`.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 punti
Un dizionario D e' fornito come input. Le chiavi di D sono interi mentre
i valori sono liste di stringhe con ripetizioni.

D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}

Scrivi la funzione func1(D) che costruisice e ritorna la lista W
che contiene i valori ottenuti prendendo, 
per ogni chiave K in D, 
l'elemento corrispondente dalla lista L associata a K; 
prima di selezionare un elemento, la funzione ordina L in ordine alfabetico inverso.

Dato D come definito sopra, la funzione ritorna:

    W = ["c", "b", "b"]

poiche' la prima lista in ordine inverso e' ["h", "g", "f", "e", "c"]
e l'elemento in posizione 4 e' "c".
La seconda lista e' ["z", "w", "b", "a"] e l'elemento in posizione 2 e' "b".
La terza lista e' ["b", "a", "a"] e l'elemento in posizione 0 e'  "b".
'''

#inizio 
#accedo a ogni lista la ordino in ordine alfabetico inverso 



def func1(D):
    w = []
    for k in D.keys():
        D[k]= sorted(D[k], reverse=True)
        print(D[k])
    for K in D.keys():
        w.append(D[K][K])
    return w


# %% -------------------------------- FUNC.2 -------------------------------- #
'''func2: 2 punti
Implementare la funzione func2(list_all, list_rm) per eliminare

distruttivamente da list_all tutti i numeri interi non contenuti in list_rm.

Inoltre La funzione non considera le ripetizioni in lista_all,
quindi l'elenco risultante non conterrà ripetizioni.

Esempio: se lista_all = [2, 4, 3, 4, 4, 3, 4, 5, 2, 6]
         e lista_rm = [5, 3, 2, 7]
         lista_all **deve essere modificata distruttivamente** in [2, 3, 5].

NOTA: la funzione NON ritorna nessun valore, la lista "lista_all" e' modificata
in manira distruttiva.
'''


def func2(list_all, list_rm):
    list_all[:] = list(set(list_all) & set(list_rm))


# %% -------------------------------- FUNC.3 -------------------------------- #
'''func3: 2 punti
Implementare la func3(strList) che:
- prende in input una lista di stringhe
- calcola la somma dei codici ascii dei caratteri di ciascuna stringa,
  ottenendo un valore intero per ogni stringa, e aggiunge tutti i valori
  ottenuti ad una lista.
- restituisce la lista degli interi ordinati in base alle stringhe della lista
  iniziale strList, in ordine crescente.

Ad esempio, se strList = ["monkey", "cat", "panda", "alligator"]
i valori ascii corrispondenti sono: [659, 312, 516, 959]
che, in base all'ordinamento alfabetico dell'elenco iniziale,
vengono restituiti come: [959, 312, 659, 516]
'''
#1somma di tutti i caratteri caratteri ascii di ogni parola 

def func3(strList):
    lista_somme = []
    strList[:]=sorted(strList)
    for elem in strList:
        tot = 0 
        for char in elem:
            tot+=ord(char)    
        lista_somme.append(tot)
    return lista_somme
    

# %% -------------------------------- FUNC.4 -------------------------------- #
''' func4: 5 punti
Implementare la funzione func4(M) che prende come argomento:
- M: una matrice bidimensionale di numeri interi rappresentata
  come liste di liste.

La funzione restituisce il risultato di R + C, dove:
- R è il prodotto dei valori ottenuti dalla somma di ogni riga di M.
- C è il prodotto dei valori ottenuti dalla somma di ogni colonna di M.

Esempio:
Supponiamo che M sia:

   [[1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 0, 1, 2]]

le somme calcolate sulle sue righe sono 10, 26, 12 e il loro prodotto è 3120;
le somme calcolate sulle colonne sono 15, 8, 11, 14 e il loro prodotto è 18480;
quindi la funzione restituisce 21600.
'''


def func4(M):
    R = 1
    C = 1
    lista_da_moltiplicare_rig= []
    lista_da_moltiplicare_col= []
    #faccio le somme di tutte le righe 
    for x,n in enumerate(M):
        aus_var=0 
        for y,m in enumerate(n):
            aus_var+=M[x][y]
        lista_da_moltiplicare_rig.append(aus_var)
    print("RIGHE",lista_da_moltiplicare_rig)
    #faccio le somme di tutte le righe 
    #ma prima ribalto la matrice per riusare il codice
    M_ribaltata = list(zip(*M))
    for x,n1 in enumerate(M_ribaltata):
        aus_var=0 
        for y,m in enumerate(n1):
            aus_var+=M_ribaltata[x][y]
        lista_da_moltiplicare_col.append(aus_var)
    print("COLONNE",lista_da_moltiplicare_col)
    
    #moltiplico le var RC richieste
    for intero in lista_da_moltiplicare_rig:
        print("R: ", R)
        R = R *intero
    for intero1 in lista_da_moltiplicare_col:
        print("C: ", C)
        C = C * intero1
    return R+C
        

# %% -------------------------------- FUNC.5 -------------------------------- #


'''
func5: 6 punti

Scrivere una funzione func5(points) che prende in ingresso una lista
di coordinate (x,y) di N punti nel piano cartesiano (N >= 3).  Ogni
punto è una coppia di numeri interi.  Per ogni punto, si considera la
sua distanza dal centro del piano (0, 0).

La funzione deve restituire, come una tupla, il baricentro (X, Y) dei
3 punti più vicini al centro del piano. Tutti i valori devono essere
riportati con una precisione di 3 cifre decimali (per farlo si può
usare la funzione round).

  - NOTA: La distanza tra 2 punti (x1, y1) e (x2, y2)
    è la distanza euclidea: sqrt[(x1-x2)² + (y1-y2)²]
  - NOTA: Il baricentro di N punti è il punto (X', Y'),
    dove X' è la media delle coordinate x degli N punti
    e Y' è la media delle coordinate y degli N punti.

Ad esempio, se points = [(2, 2), (-1, 1), (3, 0), (3, 2), (2, -1)],
prima di ordinarli, le distanze dal centro (0,0) sono:
 2.828, 1.414, 3.0, 3.606, 2.236
Dopo averli ordinati, il baricentro risultante dei 3 punti
più vicini a (0, 0) è: (1.0, 0.667)
'''


def func5(points):
    # scrivi qui il tuo codice
    pass


# %% ----------------------------------- EX.1 ------------------------------- #

'''
Ex1: 6 punti
Implementare la funzione ex1(root, result), ricorsiva o utilizzando
funzioni ricorsive, con 2 argomenti:
  - root: la radice di un albero binario;
  - result: una lista vuota, che che deve essere popolata in-place con
    il risultato. Si veda sotto.

L'albero è costituito da istanze della classe BinaryTree definita in tree.py
La funzione deve popolare la lista "result" in modo che ogni i-esimo elemento
della lista contiene la somma di tutti i nodi a profondità i. La
radice dell'albero è a profondità 0.

NOTA: la funzione NON ritorna nessun valore, la lista "result" e'
popolata "in-place".

Esempio:
        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

Se l'albero è quello di sinistra, result si modifica in  [5, 10, 13].
Se l'albero è quello di destra, result si modifica in [2, 12, 12, 24]
'''


#from tree import BinaryTree

def recfunc(node,level,result):
    if not node :
        return 0
    if level >= len(result):
        result.append(0)
    result[level]+=node.value
    recfunc(node.sx,level+1)
    recfunc(node.dx,level+1)
def ex1(root, result):
    recfunc(root,0,result)    

# %% ----------------------------------- EX.2 -------------------------------#
'''Ex2: 6 + 3 punti
Implementare la funzione ex2(dirin, words), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, avendo come argomento:
    - dirin: il percorso di una directory esistente come stringa
    - words: una lista di parole

La funzione esaminerà dirin e tutte le sue sottocartelle (a qualsiasi
livello), e conterà le occorrenze delle parole di 'words' in tutti i
file di testo (cioè i file con estensione .txt) presenti in qualsiasi
cartella.  Le parole presenti in un file sono separate da uno o piu dei
seguenti caratteri: spazio, tabulazione o carattere newline.

(6 punti) La funzione restituisce una lista di tuple (parola, occ), in cui:
    - il primo valore di ogni coppia è una delle parola nella lista di input.
    - il secondo valore 'occ' della coppia è il numero di occorrenze
      di quella parola nei file di testo.

(+ 3 punti) La lista è ordinata in base al numero di occorrenze delle
parole (in ordine decrescente). Se due o più parole hanno lo
stesso numero di occorrenze, sono ordinate alfabeticamente (in
ordine crescente). Se una parola dell'elenco di input non si trova mai
nei file testuali, deve comunque essere restituita dalla funzione con
conteggio 0.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk

Ad esempio, data la cartella "ex2/" e se words = ["gatto", "cane"]
la funzione restituisce: [("cane", 11), ("gatto", 6)].
'''
#cercare le occorrenze di words nei file txt


import os
def esplora_et_conta(path,occorrenze):
    lista_paths = os.listdir(path)
    full_path = ''
    for item in lista_paths:
        full_path =  path+'/'+item
    for full_path in lista_paths:
        if os.path.isdir(full_path):
            esplora_et_conta(full_path)
            pass#richiama ricorsivamente
        elif full_path.endswith(".txt"):
            with open(full_path, mode='r',encoding='utf-8')as f:
                testo = f.read().strip().split()
            for parola in testo:
                    if parola in occorrenze.keys():
                        occorrenze[parola]+=1
     

def ex2(dirin, words):
    occorrenze  = {word:0 for word in words}
    esplora_et_conta(dirin,occorrenze)
    lista_tuple = []
    for key,value in occorrenze.items():
        lista_tuple.append((key,value))
    return lista_tuple
            



##############################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)