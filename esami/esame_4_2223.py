# -*- coding: utf-8 -*-
'''simulazione esame fatta a 4 mani con gabriele'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame e' necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "pippo"
cognome    = "pippone"
matricola  = "42069"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

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

def func1(a_dict, word):
    #contare stringhe rimosse
    counter = 0
    for chiave, valore in a_dict.copy().items():
        if word in valore :
            a_dict.pop(chiave)
            counter += 1
    return counter

#a = {'a':['a','b','c'], 'b':['a','b'], 'c':['a','c']}
#print(func1(a, 'b'))
#print(a)

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(a_string) che prende in ingresso una
stringa 'a_string' e restituisce un'altra stringa. La nuova stringa ha
tutte le lettere della stringa in input ripetute una volta sola e in
ordine alfabetico inverso.

Esempio: se a_string='welocme' l'invocazione di func2(a_string) dovrà
         restituire la stringa 'womlec'
'''

def func2(a_string):
    insieme_di_char = set(list(a_string))
    stringa_senza_doppie = "".join(list(insieme_di_char))
    lista_ordinata = sorted(stringa_senza_doppie, reverse=True)
    stringa_da_tornare = "".join(lista_ordinata)
    return stringa_da_tornare

print(func2('welcome'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe con lo stesso numero di elementi e
restituisce una nuova lista composta dalle stringhe ottenute
concatenando:
 - la prima stringa della prima lista con l'ultima stringa della
   seconda lista,
 - la seconda stringa della prima lista con la penultima della seconda
   lista,
 - e così via.
La lista risultante deve essere ordinata per numero di caratteri
crescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['so', 'sin', 'vas', 'rin', 'vul']  e
            string_list2=['cane', 'casai', 'to', 'cero', 'sia']
         l'invocazione di func3(string_list1, string_list2) dovrà restituire
         la lista ['sosia','vasto','sincero','vulcane','rincasai']
'''


def func3(string_list1, string_list2):
    #ribalto la stringa per ovviare al problema degli indici
    #invece di selezionare in base a lst[0] e lst[-1] il primo elemento lst[1]e lst[-2]
    #selezionerò sempre lst[0]
    stringa_ribaltata = string_list2[::-1]
    
    #instanzio le variabili che mi serviranno nel programma
    lista_da_tornare = []
    indice = 0
    
    #passo in rassegna la prima stringa
        #creo una stringa contenente l'i-esimo elemento delle liste e li appendo dentro la lista da tornare
    for stringa in string_list1:
        stringa_da_appendere = ""
        stringa_da_appendere += string_list1[indice] + stringa_ribaltata[indice]
        lista_da_tornare.append(stringa_da_appendere)
        indice +=1
        
    #ordina lista_da_tornare in base alla lunghezza delle stringhe
    lista_da_tornare = sorted(lista_da_tornare, key=lambda x:len(x))
    
    return lista_da_tornare



#string_list1=['so', 'sin', 'vas', 'rin', 'vul']
#string_list2=['cane', 'casai', 'to', 'cero', 'sia']
#print(func3(string_list1, string_list2))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 punti

Si scriva una funzione func4(input_file, output_file) che prende in
ingresso due stringhe, 'input_file' e 'output_file' che rappresentano
i percorsi a due file.  All'interno del file indicato da 'input_file'
sono presenti su una sola riga una serie di parole (composte da
caratteri alfabetici) separate da virgole, spazi, punti e virgole e da
punti. . ; ,
La funzione deve individuare tutte le parole contenute nel file
indicate da 'input_file' e scriverle all'interno di un nuovo file
indicato da 'output_file'.  Le parole devono essere scritte
all'interno del file su una sola riga terminata dal carattere di
a capo, separate da uno spazio e con il seguente ordine:
    - numero di caratteri crescente, len(x)
    - in caso di parità, in ordine alfabetico, indipendentemente da
      maiuscole e minuscole lower(x)
    - in caso di parole identiche, in ordine lessicografico lower(x).
La funzione deve restituire il numero di parole scritte nel file in
output.
"/n"
Esempio: se il contenuto del file 'input_file' è il seguente
Dog,cat,dog;Cat.bird car

l'invocazione di func4('input_file', 'output_file') dovrà scrivere nel
file 'output_file' la seguente riga
car Cat cat Dog dog bird

e ritornare il valore 6.

#1 individuare tutte le parole singole e metterle in una lista
#2 pulire caratteri non alfa con un for loop
#3 ordinare in base ai tre parametri di sopra la lista e usare join per renderla una stringa  carattere finale = "/n"

#4 scrivere la stringa nell'output file
"""


def func4(input_file, output_file):   
   #funzione per togliere non alfa
    def rm_non_alfa(x):
        for parola in x:
            for char in list(parola):
                if char in ":,." or char == " ":
                    parola.pop(char)
        return x 
    
    #funzione per ordinare
    def ordina_lista(lista):
            return sorted(lista, key=lambda x: (len(x), x.lower(), x))

    #leggere parole nel file
    with open(input_file, mode="r",encoding="utf-8") as f:
        testo_raw = f.read()
            
    #creo una lista con tutte le parole e rimuovo gli spazi      
    lista_parole_non_pulita = testo_raw.strip().split()
    
    #fare un remove non alfa su lista_parole_non_pulita
    lista_non_alfa = rm_non_alfa(lista_parole_non_pulita)
    
    #ordinare in base ai parametri 
        #- numero di caratteri crescente, lambda x: len(x)
        #- in caso di parità, in ordine alfabetico, indipendentemente da maiuscole e minuscole lower(x)
        #- in caso di parole identiche, in ordine lessicografico lower(x).
    lista_ordinata = ordina_lista(lista_non_alfa)
    lista_ordinata += ["/n"]
    #trasforma la lista in una stringa con /n alla fine
    stringa_da_scrivere = "".join(lista_ordinata)
    with open(output_file, mode="w",encoding="utf-8"):
        print(stringa_da_scrivere,output_file)
        
    
    
        

# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))
# print(func4('func4/func4_test2.txt','func4/func4_out2.txt'))
# print(func4('func4/func4_test3.txt','func4/func4_out3.txt'))


# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene una serie di punti
diversi bianchi su uno sfondo nero. La funzione deve individuare tutti
i rettangoli definiti da quattro pixel bianchi che possono essere
considerati gli spigoli di tali rettangoli (si veda l'esempio più avanti).

Si può assumere che:
    - ogni riga ha al più due punti bianchi e
    - ogni colonna ha al più due punti bianchi.

La funzione deve ritornare una lista contenente l'area di tutti i rettangoli
individuati nell'immagine, ordinati per dimensione crescente.

Esempio: nell'immagine del file func5/image01.png ci sono gli spigoli del
         rettangolo (5,5), (45,5), (5,25), (45,25) con area 861
         e del rettangolo (10,10), (20,10), (10,20), (20,20) con area 121
         e c'è un pixel in (31, 15), per cui l'invocazione di
         func5('func5/image01.png') deve restituire la lista [121, 861].
         Gli spigoli riportati sopra sono nel formato:
         top-left, top-right, bottom-left, bottom-right.
         Le coordinate sono (x,y).



"""
import images

def func5(input_pngfile):
    #inizio
    img=images.load(input_pngfile)
    #pixel bianchi
    pixel_bianchi = []
    #lista da ordinare e tornare tornare 
    lista_da_tornare = []
    #prendere tutti i pixel bianchi 
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            if pixel == (255,255,255):
                pixel_bianchi.append((x,y))
    #vedere i pixel bianchi che possono formare un rettangolo
    for (x1,y1) in pixel_bianchi:
        for (x2,y2) in pixel_bianchi:
            if x1 < x2 and y1 < y2:
               if (x1, y2) in white_pixels and (x2, y1) in white_pixels:
                    area = (x2 - x1) * (y2 - y1)
                    lista_da_tornare.append(area)
    #ordino la lista
    lista_da_tornare.sort()
    return lista_da_tornare

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.
La funzione deve explorare ricorsivamente l'albero delle directory con
radice in 'directory' e restituire un dizionario.
Le chiavi del dizionario sono i percorsi delle sotto-directory di
'directory', sottoforma di stringa.
Il valore della chiave di una directory è un set di stringhe con i nomi
di quei file '.txt' presenti in 'directory' per i quali il primo carattere
del contenuto del file è uguale all'ultimo.
Se una directory non contiene nessun file .txt con tale caratteristica,
allora quella directory non appare nel dizionario.
Esempio: se la funzione è chiamata su 'ex1/A', ritorna:

{'ex1/A/B': {'b.txt'}, 'ex1/A/C': {'c.txt'}}

poiché ex1/A/B/b.txt e ex1/A/C/c.txt sono gli unici file in cui
il primo carattere del contenuto è uguale all'ultimo ('k' per il primo,
'a' per il secondo).

NOTA: è proibito usare la funzione os.walk. Si possono usare:
  
    os.listdir, 
    os.path.isfile, 
    os.path.exists, 
    etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.
  
#individuare ogni file ricorsivamente
#caso base: 
#controllare se testo[0] == testo[-1]
#
return dizionario = {percorsi_sotto_dir:{"nome_file.txt","nome_file.txt"}}
"""
#1 esplora la directory e crea le stringhe dei vari percorsi

#come stabilire se la parola del file di testo va come chiave
#controllare se la prima lettera è uguale all'ultima, chiamata per ogni file di testo def is_eligible()
#se eligibile torna true, aggiungi sub_dir al set della sua chiave


def check_param(file_di_testo):
    with open(file_di_testo, mode="r", encoding="utf-8") as f:
        testo_raw = f.read()
    return len(testo_raw) > 0 and testo_raw[0] == testo_raw[-1]

def esplora_subdir(path):
    dizionario_da_tornare = {}
    stringhe_dir = os.listdir(path)

    for elem in stringhe_dir:
        elemento_path = path + "/" + elem

        if os.path.isdir(elemento_path):
            sotto_dizionario = esplora_subdir(elemento_path)
            dizionario_da_tornare.update(sotto_dizionario)

        elif os.path.isfile(elemento_path) and elem.endswith(".txt") and check_param(elemento_path):
            if path not in dizionario_da_tornare:
                dizionario_da_tornare[path] = set()
            dizionario_da_tornare[path].add(elem)

    return dizionario_da_tornare

def ex1(root):
    return esplora_subdir(root)



# print(ex1('ex1/A'))
# print(ex1('ex1/B'))
# print(ex1('ex1'))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 punti

Si definisca la funzione ex2(root) ricorsiva (o che al suo interno
usa una funzione ricorsiva) che riceve in ingresso la radice di
un albero binario, come definito nella classe `BinaryTree` del modulo
tree.py.  L'albero in ingresso ha delle stringhe come valori. La
funzione deve restituire la stringa risultante dalla concatenazione di
tutti i valori associati ai nodi dell'albero con la seguente regola:
  - la concatenazione avviene con l'ordine LNR se il nodo si trova
    in un livello pari
  - con l'ordine RNL se il nodo è in un livello dispari
dove L è il sottoalbero sinistro, N il nodo e R il sottoalbero destro.
La radice si assume a livello 0.

Esempio:

        ______A______                        ______A______
       |             |                      |             |
       B__        ___C___                __ B__        ___C___
          |      |       |              |      |      |       |
          D      E       F             _D_     E_    _F_     _G_
                                      |   |      |  |   |   |   |
                                      H   I      J  K   L   M   N

  Se l'albero è quello di sinistra, la funzione deve restituire
  la stringa 'DBAFCE'.

  Se l'albero è quello di destra, la funzione deve restituire la
  stringa 'EJBHDIAMGNCKFL'
  """


def ex2(root):
    esplora_albero(root,0)
    def esplora_albero(root,livello):
        if not root:
            return ''
        r = esplora_albero(root.dx,livello+1)
        l = esplora_albero(root.sx, livello+1)
        n = root.value
        if livello%2:
            return l+n+r
        else:
            return r+n+l

    pass


# from tree import BinaryTree
# root = BinaryTree.fromList(['A', ['B',None,['D',None,None]], ['C', ['E',None,None], ['F',None,None]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',None,None],['I',None,None]],['E',None,['J',None,None]]], ['C', ['F',['K',None,None],['L',None,None]], ['G',['M',None,None],['N',None,None]]]])
# print(ex2(root))
# root = BinaryTree.fromList(['A', ['B',['D',['H',['L',None,None],None],None],['E',None,['I',None,None]]],['C', ['F',['J',None,None],None],['G',None,['K',None,['M',None,None]]]]])
# print(ex2(root))
###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)