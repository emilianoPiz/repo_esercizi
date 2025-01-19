#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Assegnare le variabili sottostanti con il proprio
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la prova e' NECESSARIO:
    - assegnare le variabili con nome cognome e matricola
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale e' la somma dei punteggi dei problemi risolti.
Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.
"""
nome       = "asd"
cognome    = "asd"
matricola  = "42069"

#########################################

################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci
# corrispondenti ai test che non si vogliono eseguire all'interno della lista
# `test` alla FINE di `grade.py`.
#
# Per eseguire il debug di funzioni ricorsive potete disattivare il test di
# ricorsione, assegnando `DEBUG=True` all'interno file `grade.py`.
#
# L'impostazione DEBUG=True attiva anche lo la stampa a terminale dello STACK
# TRACE degli errori, che permette di conoscere il numero della linea di
# program.py che ha generato un errore.
################################################################################


# %% -------------------------------- FUNC.1 -------------------------------- #
''' func1: 2 punti
Si definisca la funzione func1(string_list1, string_list2) che riceve in
ingresso due liste di stringhe e restituisce una nuova lista di stringhe
contenente le stringhe presenti soltanto in una delle due liste in ingresso
(ossia, che non compaiono in entrambe le liste). La lista in output
dev'essere ordinata in ordine di lunghezza crescente 
e in caso di parità in ordine alfabetico inverso.
'''
def func1(string_list1, string_list2):
    new_string_list = set(string_list1) ^ set(string_list2)
    new_string_list = sorted(new_string_list, key=lambda x :(-len(x),x), reverse=True)
    return new_string_list
    
    # completate la funzione


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca una funzione func2(a_string) che prende in ingresso una
stringa 'a_string' e restituisce un'altra stringa. La nuova stringa ha
tutte le lettere della stringa in input che vi appaiono almeno 2 volte
in ordine alfabetico inverso.

Esempio: se a_string='welcome home' l'invocazione di func2(a_string) dovrà
         restituire la stringa 'ome'
'''

def func2(a_string):
    new_string_list = []
    for car in a_string:
        if a_string.count(car)>=2 and car not in new_string_list:
            new_string_list.append(car)
    new_string_sorted= sorted(new_string_list, reverse= True)
    
    return "".join(new_string_sorted)
# print(func2('welcome home'))


# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che prende
in ingresso due liste di stringhe con lo stesso numero di stringhe. len strlist 1=2 
Due stringhe prese a coppie da string_list1 e string_list2 hanno sempre
la stessa lunghezza.

Esempio: se  string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
             string_list2=['ce', 'cas', 'too', 'ceo', 'sia']

'sIn' ha la stessa lunghezza di 'cas', 'VUL' ha la stessa lunghezza di 'sia'.

Si restituisca una nuova lista che trasforma la lista string_list2 con le   return lista
seguenti regole:
 - il case dei caratteri della stringa della lista string_list1 serve
   come guida per impostare il case dei caratteri della stringa della lista
   string_list2
- in particolare se un carattere della stringa della lista string_list1
  è lowercase allora il nuovo carattere da creare dovrà essere preso dal
  carattere corrispondente della stringa della lista string_list2 ma reso
  UPPERCASE.
- viceversa, se un carattere della stringa della lista string_list1
  è UPPERCASE allora il nuovo carattere da creare dovrà essere preso dal
  carattere corrispondente della stringa della lista string_list2 ma reso
  lowercase.
- Nel caso un carattere non sia né lowercase né UPPERCASE si sostituisce con spazio
- Le liste possono contenere stringhe vuote.

La lista finale va ordinata in ordine decrescente in base alla lunghezza
delle stringhe, in caso di parità, in ordine alfabetico crescente.

Esempio: 
string_list1=['sO', 'sIn', 'VAS', 'rin', 'VUL']
string_list2=['ce', 'cas', 'too', 'ceo', 'sia']
expected    =['CEO', 'CaS', 'sia', 'too', 'Ce']

Ad esempio 'ce' --> 'Ce' perche 'sO' ha la 's' minuscola e 'O' maiuscola.

NOTA: si usino le funzioni delle stringhe isupper(), lower() etc.
'''
#inizio
#dichiarazione
# per x volte dove x è la lunghezza di una delle due liste
    #dichiaro una stringa vuota
    #guardo l'i-esimo carattere del i-esimo elemento di list_2. se l'i-esimo carattere del i-esimo elem di list_1 è lower, 
    #allora questo to upper, sennò to lower e lo appendo a stringa vuota
    #se non islower and is upper
    #allora strings

def func3(string_list1, string_list2):
    lista_new=[]
    for j,elem in enumerate(string_list2):
        stringa_aus = ""
        try: 
            for i,car in enumerate(elem):
                if string_list1[j][i].islower():
                    car = car.upper()
                    stringa_aus += car
                elif string_list1[j][i].isupper():
                    car = car.lower()
                    stringa_aus += car
                elif  not (string_list1[j][i].isupper() and string_list1[j][i].islower()):
                    car[:] = " "
                    stringa_aus += car
        except: IndexError("STRINGA FUORI DAL RANGE")          
        if len(stringa_aus) == len(string_list1[j]) :
            lista_new.append(stringa_aus)
            stringa_aus = ""
    lista_new = sorted(lista_new,key=lambda x :(-len(x),x))
    return lista_new
'''
string_list1=['sO', 'sIn', 'VAS', '', '']
string_list2=['ce', 'cas', 'too', '', '']
print(func3(string_list1, string_list2)) # ['CEO', 'CaS', 'sia', 'too', 'Ce']
'''

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 2+4 punti
2 punti:
Definire una funzione func4(input_filename, output_filename, length)
che prende in input due stringhe che rappresentano due nomi di file e un intero.
Il file input_filename contiene stringhe separate da spazi,
tabulazioni o ritorni a capo.

La funzione deve restituire il numero di stringhe della lunghezza richiesta
trovate nel file di input.
PROBLEMA 1 

+4 punti:
La funzione deve creare un nuovo file di testo chiamato output_filename
contenente tutte le stringhe di lunghezza 'length' presenti nel file
input_filename organizzate per righe.
Le righe sono in ordine alfabetico decrescente.
Le parole in ogni riga:
    - hanno la stessa lettera iniziale, senza distinzione tra
      maiuscole e minuscole
    - sono separate da uno spazio
    - sono ordinate in ordine alfabetico, senza distinzione tra
      maiuscole e minuscole. In caso di parole uguali, sono
      in ordine alfabetico.

Esempio
Se le seguenti tre righe sono presenti nel file 'func4_test1.txt'

f= 'cat bat    rat
Condor baT
Cat cAr CAR''

la funzione func4('func4_test1.txt', 'func4_out1.txt', 3) deve scrivere
nel file 'func4_out1.txt' le seguenti 3 righe:
rat
CAR cAr Cat cat
baT bat

e restituire il valore 7.
"""

    
def func4(input_filename, output_filename, length):
    with open(input_filename, mode="r", encoding="utf-8") as f:
        lista_parole = [x for x in f.read().split() if len(x) == length]
    
    numero_stringhe = len(lista_parole)  

    iniziale_per_righe = {}
    for parola in lista_parole:
        iniziale = parola[0].lower()
        if iniziale not in iniziale_per_righe:
            iniziale_per_righe[iniziale] = []
        iniziale_per_righe[iniziale].append(parola)
        
    righe = []
    for iniziale in sorted(iniziale_per_righe.keys(), reverse=True): 
        gruppo = sorted(iniziale_per_righe[iniziale], key=lambda x: (x.lower(), x))  
        righe.append(" ".join(gruppo))
    
    with open(output_filename, mode="w", encoding="utf-8") as fout:
        fout.write("\n".join(righe) + "\n")

    return numero_stringhe

print(func4('func4/func4_test1.txt', 'func4/func4_out1.txt', 3))
#%% ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 8 punti
Si definisca la funzione func5(txt_input, width, height, png_output) che riceve come argomenti

- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file.

Il file txt_file contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura

Possono essre presenti 2 tipi di figura:
- segmento orizzontale 
    HORIZONTAL R G B x y L
    Il segmento inizia nel punto (x,y) ed è lunga L pixel, verso destra
- segmento verticale
    VERTICAL R G B x y L
    Il segmento inizia nel punto (x,y) ed è lunga L pixel, verso il basso

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di segmenti disegnati dei due tipi
come tupla dei due valori (HORIZ,VERT)

NOTA: va gestito correttamente lo sbordare delle figure dalla
immagine, infatti sono ammesse anche coordinate negative, e dimensioni
o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func5/in_1.txt contiene le 3 righe
HORIZONTAL 0 255 0 -30 40 110
VERTICAL 255 0 0 20 10 200
VERTICAL 0 0 255 10 20 50

l'esecuzione della funzione func5('func5/in_1.txt', 50, 100, 'func5/your_image_1.png')
produrrà una figura uguale al file 'func5/expected_1.png'
e tornerà la coppia (1, 2)
'''
#1 inizio
#2 dichiarazione (altezza,larghezza,file_out)
#2.1 creo una struttura dati che contiene come chiavi horiz e vert, e come value una lista dei vari segmenti da fare
#3 disegnare ogni segnemento con chiave horiz e aumentare un counter specifico
#3 disegnare ogni segnemento con chiave horiz e aumentare un counter specifico
#4 disegni figura
#5 return tupla dei counter 
import images

def draw_line(height, width, pixel, x, y, L, tipo, new_img):
    if tipo == "HORIZONTAL":
        for i in range(L):
            if 0 <= x + i < width and 0 <= y < height:
                new_img[y][x + i] = pixel
    elif tipo == "VERTICAL":
        for i in range(L):
            if 0 <= x < width and 0 <= y + i < height:
                new_img[y + i][x] = pixel
    return new_img

def func5(txt_input, width, height, png_output):
    with open(txt_input, mode="r", encoding="utf-8") as f:
        testo = f.read()

    data_struc = {"HORIZONTAL": [], "VERTICAL": []}
    new_img = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]
    counter_horizontal = 0
    counter_vertical = 0

    for riga in testo.splitlines():
        parts = riga.split()
        tipo = parts[0]
        R, G, B = map(int, parts[1:4])
        x, y, L = map(int, parts[4:])

        if tipo == "VERTICAL":
            data_struc["VERTICAL"].append((R, G, B, x, y, L))
            counter_vertical += 1
        elif tipo == "HORIZONTAL":
            data_struc["HORIZONTAL"].append((R, G, B, x, y, L))
            counter_horizontal += 1

    for key, value in data_struc.items():
        for item in value:
            R, G, B, x, y, L = item
            new_img = draw_line(height, width, (R, G, B), x, y, L, key, new_img)

    images.save(new_img, png_output)
    return counter_horizontal, counter_vertical





# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si scriva una funzione ricorsiva ex1(a_set, n), o che al suo interno
usa una funzione ricorsiva, che prende in ingresso un set di stringhe
'a_set' e un intero n e restituisce un nuovo set.
Il set in output deve contenere tutte le possibili stringhe ottenute
con la concatenazione di n elementi appartenenti ad a_set.

NOTA: definite la funzione ricorsiva come funzione esterna (col def in prima colonna)

Esempio:
    la funzione ex1({''a',b','c'}, 2) deve restituire l'insieme
    {'cb', 'bb', 'cc', 'aa', 'ca', 'ba', 'bc', 'ab', 'ac'}
"""


    
    # completate la funzione



# print(ex1({'a','b','c'}, 2))

# ----------------------------------- EX.2 ----------------------------------- #


"""
Es 2: 9 punti

Si progetti la funzione ex2(node, k), ricorsiva o che fa uso di
funzioni o metodi ricorsivi, che riceve come argomenti un albero
binario e trova il nodo divisibile per k che si trova a profondità
minima (partendo da radice=0). La funzione restituisce la profondità
del nodo individuato. Se nessun nodo è divisibile per k la funzione
ritorna il valore -1.

Ciascun nodo è un oggetto della classe tree.BinaryTree

Esempio: se K=5 e l'albero è il seguente
             ______1______                      # profondità 0
             |           |                      #
       _____25___        7  ------------------- # 1
       |        |                               #
    ___3___     65 ---------------------------- # 2
    |     |                                     #
    4     55  --------------------------------- # 3

la funzione ex2 deve ritornare 1, perchè 25 è il nodo con valore
multiplo di 5 che si trova a profondità minima, ovvero 1. Gli
altri nodi potenziali sono 55 e 65, ma sono a una profondità
maggiore (rispettivamente 3 e 2).

NOTA: definite la funzione ricorsiva come funzione esterna (col def in prima colonna)

"""

def expl_cont(node,level,k):
    if not node:
        return -1
    if node.value % k ==0:
        return level
    left_level = expl_cont(node.left,  level + 1, k)
    right_level= expl_cont(node.right, level + 1, k)
    if left_level<= -1 and right_level<= -1:
        return -1
    elif left_level<= -1:
        return right_level
    elif right_level<= -1:
        return left_level
    else:
        return min(left_level, right_level)
             
def ex2(node, k):
    level = expl_cont(node,0,k)
    return level

###################################################################################
if __name__ == '__main__':
    # Place your tests here
    print('*' * 50)
    print('ITA\nEseguire grade.py per effettuare il debug con grader incorporato.')
    print('Altrimenti, inserire codice qui per verificare le funzioni con test propri')
    print('*' * 50)
    print('ENG\nRun grade.py to debug the code with the automatic grader.')
    print('Alternatively, insert here the code to check the functions with custom test inputs')
    print('*' * 50)
