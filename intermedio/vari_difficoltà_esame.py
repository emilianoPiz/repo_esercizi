# -*- coding: utf-8 -*-
"""
esercizi presi da 
https://github.com/sleepy-software-engineer/PythonExercises
utili ad allenarsi per l'esame di fondamenti di programmazione AA24/25

"""

"""
ESERCIZIO3:
progettare la funzione es3(ins1, ins2) che:
- riceve  in input due insiemi  di numeri naturali
- trova le terne (a,b,c) con a,b e c in insi1 con la proprieta' che a<b<c e a+b+c e' in insi2
- restituisce l'insieme di tutte le triple trovate.
Nella lista restituita le triple devono essere  rappresentate tramite tuple e le
varie tuple devono comparire nella lista per somma di componenti crescenti e in caso di parita'
in ordine lessicografico crescente.
ESEMPIO:
se ins1={ 2,4,5,6,8,9} e ins2={5,15,19,25} la funzione restituisce la lista
[(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
"""
def es3(ins1, ins2):
    insieme_risultato =[]
    #trova terne in ins1 tali che a<b<c e a+b+c in ins2
    for a in ins1:
        for b in ins1:
            for c in ins1:
                if a+b+c in ins2 and a<b<c :
                    insieme_risultato.append((a,b,c))
    #prima di tornare ordino in base al parametro che la somma degli dell'elementi della tupla
    #maggiore deve essere il primo
    return sorted(insieme_risultato, key=lambda x: x[0]+[1]+[2])

                    
''' 
ESERCIZIO 31:
Implementate la funzione es31(fname1,fname2) che prende in input l'indirizzo di due  file di testo.
Il testo del primo file va modificato come segue:
- ciascun carattere tra 'a' e 'z' (minuscoli) che compare nel file in un numero dispari di parole
(una parola e' una sequenza massimale di caratteri diversi dallo spazio, tab o a capo)
va sostituito dal corrispondente carattere maiuscolo.
Il file cosi' ottenuto va poi registrato all'indirizzo fname2.
La funzione deve restituire quanti dei 26 caratteri tra 'a' e 'z' 
da minuscoli son diventati maiuscoli nella trasformazione del file di testo. 
Ad esempio se 
- il file fname1 contiene  il testo 'Monti, Sterbini e Spognardi'
- il file fname2 conterra' il testo 'MoNtI, SterBINI e SPoGNArDI'
il valore restituito dalla funzione sara' 7 (le lettere cambiate sono NIBPGAD)
'''
def es31(fname1,fname2):
    import string
    
    lettere_cambiate=[]
    occorrenze = {x:0 for x in  string.ascii_lowercase}
    
    with open(fname1, mode='r',encoding='utf-8') as f:
        testo_raw= f.read()
    parole = testo_raw.split()
    for parola in parole:
        lettere_parole = set(parola.lower())
        for char in string.ascii_lowercase:
            if char in lettere_parole:
                occorrenze[char]+=1
    for char in occorrenze:            
            if occorrenze[char]%2:
                testo_raw =  testo_raw.replace(char, char.upper())
                lettere_cambiate.append(char)
    with open(fname2, mode="w", encoding='utf-8')as f:
        f.write(testo_raw)
    return len(lettere_cambiate)


''' func1: 2 punti
Si definisca la funzione func1(string_list, word) che prende in ingresso una
lista di stringhe 'string_list' e una parola 'word' e cancella in maniera distruttiva
da string_list tutte le stringhe che contengono 'word'.
La funzione restituisce il numero di stringhe rimosse.
'''
def func1(string_list, word):
    counter = 0
    for stringa in string_list:
        if word in stringa:
            string_list.pop(stringa)
            counter += 1
    return counter
    
''' func2: 2 punti
Si definisca una funzione func2(pathname) che prende in ingresso
una stringa che rappresenta il percorso ad un file testuale. Il file
contiene su ciascuna riga una coppia "numero,matricola" separata da
una virgola. I numeri sono sempre maggiori o uguali a zero.  La
funzione deve restituire il dizionario che si crea inserendo la
'matricola' come chiave sottoforma di stringa e come valore il
'numero' come tipo _intero_.  Una matricola puo' essere
associata a piu' numeri: nel caso in cui questo accade nel dizionario
va mantenuto il numero massimo.
Esempio:
Contenuto di func2_test_1.txt
 27,123456
 78,121212
 90,111111
 79,121212
 26,123456
 91,111111
La funzione func2('func2_test_1') ritorna {'123456': 27, '121212': 79, '111111': 91}
'''

def func2(pathname):
    dizionario ={}
    with open(pathname, encoding="utf-8", mode="r") as f:
        testo_raw= f.read()
    for stringa in testo_raw.splitlines():
        coppie = stringa.split(",")
        if coppie[1] not in dizionario:
            dizionario[str(coppie[1])]=int(coppie[0])
        for key, value in dizionario:
            if coppie[0] > dizionario[key]:
                dizionario.setdefault(key, coppie[0])
    return dizionario
""" func5: 6 punti
Si definisca una funzione func5(img, output_file_name) che prende in ingresso
un'immagine modellata come lista di liste e effetti una rotazione A DESTRA
dell'immagine di 90 gradi. La nuova immagine ruotata deve essere salvata in
output_file_name tramite il modulo images.
La funzione ritorna una tupla nel formato altezza e poi larghezza
dell'immagine ruotata.
"""

import images


def func5(img, output_file_name):
    img=images.load(img)
    ruotata=[]
    for riga in zip(*img[::-1]):
         ruotata.append(list(riga))
    images.save(ruotata, output_file_name)
    return len(ruotata), len(ruotata[0])
            
            
""" func4: 6 punti
Si scriva una funzione func4(S) che prende in ingresso una stringa 'S'
che indica del testo da cui e' necessario trasformare in spazi tutti i caratteri
non alfabetici, quindi individuare la lista di tutte le parole presenti nella
stringa, convertite in lower case.

Esempio. Da:
S = 'Pippo e topolino sono andati al mare. Hanno mangiato una bella pasta
al pesce pescato in mare il giorno prima, ma purtroppo Topolino si era
scordato di chiamare Paperino'

si passa a :
['pippo', 'e', 'topolino', 'sono', 'andati', 'al', 'mare', 'hanno',
'mangiato', 'una', 'bella', 'pasta', 'al', 'pesce', 'pescato', 'in',
'mare', 'il', 'giorno', 'prima', 'ma', 'purtroppo', 'topolino', 'si',
'era', 'scordato', 'di', 'chiamare', 'paperino']

Poi la funzione calcola l'istogramma delle parole renderizzato in una stringa.

L'istogramma sotto forma di stringa e' costruito secondo le seguenti regole:
- le parole appaiono in ordine alfabetico v
- ogni parola appare seguita da uno o più spazi, un numero di asterischi ('*')
  pari alle ripetizioni di quella parola e infine un carattere di accapo ('\n')
- il numero di spazi dopo ogni parola è tale che gli asterischi sono
  tutti allineati a sinistra.

Quindi la parte iniziale della stringa istogramma sarà:
'al        **\nandati    *\nbella     *\n .....'

che visualizzata porta a:

al        **
andati    *
bella     *
chiamare  *
di        *
e         *
era       *
giorno    *
hanno     *
il        *
in        *
ma        *
mangiato  *
mare      **
paperino  *
pasta     *
pescato   *
pesce     *
pippo     *
prima     *
purtroppo *
scordato  *
si        *
sono      *
topolino  **
una       *

NOTA: la parola piu lunga e' 'purtroppo' e dista
un solo spazio dal primo asterisco.

Si vedano test_func4_1, test_func4_2, test_func4_3
in grade.py per piu esempi
"""


def func4(S):
    #sostituisco non-alfa con spazi
    def rimuovi_nonalfa(S):
        return ''.join(char if char.isalpha() else ' ' for char in S)
    stringa_pulita=rimuovi_nonalfa(S)
    #ordino e rendo minuscole le parole della stringa
    stringa_pulita = stringa_pulita.lower()
    lista_lower = stringa_pulita.split()
    #faccio una coppia della lista cosi sorted non interferisce con il set
    lista_da_settare = set(lista_lower)    
    #conto quante volte la parola compare
    occorrenze = {x:0 for x in lista_da_settare}
    for parola in lista_lower:
        if parola in occorrenze:
            occorrenze[parola] += 1         
    #trovo la parola più lunga
    m = max(lista_lower, key=len)     
    #preparo istogramma
    isto= ""
    #creo l'istogramma
    lista_da_settare = sorted(lista_da_settare)
    for elem in lista_da_settare:
        valore = '*'*occorrenze[elem]
        isto += f"{elem:{len(m)}} {valore:{len(m)}} \n"
    print(isto)
    return isto

''' func1: 2 punti
Un dizionario D e' fornito come input. Le chiavi di D sono interi mentre
i valori sono liste di stringhe con ripetizioni.

D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}

Scrivi la funzione func1(D) che costruisice e ritorna la lista W
che contiene i valori ottenuti prendendo, per ogni chiave K in D, l'elemento
corrispondente dalla lista L associata a K; prima di selezionare un elemento,
la funzione ordine L in ordine alfabetico inverso.

Dato D come definito sopra, la funzione ritorna:

    W = ["c", "b", "b"]

poiche' la prima lista in ordine inverso e' ["h", "g", "f", "e", "c"]
e l'elemento in posizione 4 e' "c".
La seconda lista e' ["z", "w", "b", "a"] e l'elemento in posizione 2 e' "b".
La terza lista e' ["b", "a", "a"] e l'elemento in posizione 0 e'  "b".
'''


def func11(D):
    lista_da_tornare =[]
    for key, valore in D.items():
        valore = sorted(valore, reverse=True)
        lista_da_tornare.append(valore[key])
    return lista_da_tornare
'''
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


def func21(list_all, list_rm):
    lista_all_rep = list(set(list_all))
    for numero in lista_all_rep:
        if numero not in list_rm:
            lista_all_rep.remove(numero)
    list_all[:] = lista_all_rep


'''func1: 2 punti
#IMPORTANTE:
    SE ITERI UN DIZIONARIO E DEVI RIMUOVERE COSE USA .copy() method
Si definisca la funzione func1(a_dict, word) che prende in ingresso un
dizionario 'a_dict' e una parola 'word'. Ogni chiave del dizionario è
una stringa che ha una lista di stringhe come valore. La funzione deve
rimuovere dal dizionario tutte quelle chiavi associate ad una lista
che contiene una stringa 'word'.  La funzione restituisce il numero di
chiavi rimosse dal dizionario 'a_dict'.

Esempio: se a_dict = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
  l'invocazione di func1(a_dict, 'b') deve restituire 2 e
  a_dict deve risultare modificato in {'c': ['a', 'c']}.
  In quanto: e' rimossa la chiave 'a' perche' la lista ['a','b','c']
  contiene 'b' come word; e' inoltre rimossa la chiave 'b' perche' la lista
  ['a','b'] contiene 'b' come word.
'''

def func12(a_dict, word):
    #contare stringhe rimosse
    counter = 0
    for chiave, valore in a_dict.copy().items():
        if word in valore :
            a_dict.pop(chiave)
            counter += 1
    return counter
