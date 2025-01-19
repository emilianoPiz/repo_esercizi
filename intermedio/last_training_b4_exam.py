# %% ----------------------------- ES.1 ----------------------------------- #
"""
Ex 1: 6 punti

Implementa la funzione    ex1(radice : tree.BinaryTree, lista_pesi:list[int]) -> tree.BinaryTree
che riceve come argomento:
- radice: un albero binario formato da nodi tree.BinaryTree
- lista_pesi: una lista di interi
e che da esso costruisce ricorsivamente o usando funzioni o metodi ricorsivi
un secondo albero binario che ha la stessa struttura del primo con i valori dei nodi moltiplicati 
ciascuno per l'n-esimo valore di lista_pesi, dove n è la profondità del nodo nell'albero
(considerando la radice a profondità 0).

ATTENZIONE: l'albero originale deve rimanere inalterato.

Esempio:
Se l'albero in input è:
   ___1___
   |     |
 __2__   3___         
 |   |      |
 4   5      6
e lista_pesi = [2,7,3,1]
l'albero in output sarà:
   ___2___
   |     |
 __14_   21__
 |   |      |
12   15    18
"""
import tree
#

def make_albero(node,level,lista_pesi):
    if not node:
        return None
    nuovo_valore = node.value * lista_pesi[level]
    nuovo_nodo = tree.BinaryTree(nuovo_valore)
    nuovo_nodo.left = make_albero(node.left,level+1,lista_pesi)
    nuovo_nodo.right= make_albero(node.right,level+1,lista_pesi)
    return nuovo_nodo
def ex1(radice: tree.BinaryTree, lista_pesi: list[int]) -> tree.BinaryTree:
    return make_albero(radice, 0, lista_pesi)


# %% ----------------------------- ES.2 ----------------------------------- #
"""
Ex 2: 6 punti

Implementa la funzione    ex2(path : str, lista_estensioni : list[str]) -> dict[str, list[str]]
che riceve come argomento:
- path: il path di una directory
- lista_estensioni: una lista di estensioni di file (stringhe)
e che esplora ricorsivamente o usando funzioni o metodi ricorsivi la directory path
e tutte le sue sottodirectory e ritorna un dizionario che ha come chiavi le estensioni
e come valori l'insieme delle directory che contengono quel tipo di file.

ATTENZIONE: è proibito usare la funzione os.walk
NOTA: potete usare le funzioni os.listdir, os.path.isdir, os.path.isfile ...
NOTA: usate il carattere '/' per separare i path, che funziona sia su Windows che Linux

Esempio:
    directory  = 'ex2/A'
    extensions = ["txt", "pdf", "png", "gif"]
    expected   = {'txt': {'ex2/A/C', 'ex2/A', 'ex2/A/B'}, 'pdf': {'ex2/A/C', 'ex2/A'}, 'png': {'ex2/A/C'}, 'gif': {'ex2/A/C'}}
"""
import os
def esplora_e_cerca (path,dizio_dator):
    lista_path= os.listdir(path)
    for elem in lista_path:
        full_path = path + "/" + elem
        if os.path.isdir(full_path):
            esplora_e_cerca(full_path, dizio_dator)
        elif os.path.isfile(full_path):
            for ext in dizio_dator.keys():
                if full_path.endswith(ext):
                    dizio_dator[ext].add(path)
    pass
def ex2(path : str, lista_estensioni : list[str]) -> dict[str, list[str]]:
    dizio_dator = {x:set() for x in lista_estensioni}
    esplora_e_cerca(path,dizio_dator)
    return dizio_dator
# %% ----------------------------- ES.3 ----------------------------------- #
"""
Func 3: 2 punti

Implementa la funzione    func3(D1 : dict[str,list[int]], D2 : dict[int,list[str]]) -> dict[str, list[str]] 
che riceve come argomenti:
    - D1: un dizionario che ha come chiavi delle parole e come valori liste di interi DIVERSI tra loro
    - D2: un dizionario che ha come chiavi degli interi e come valori liste di parole
e che ritorna un dizionario che ha come chiavi delle parole e come valori liste di parole. ret_dict[parola]=["parola","parola"]

Le chiavi sono le sole chiavi di D1 che hanno almeno uno degli interi ad esse associati che è una chiave di D2.

Tutte le parole associate in D2 a tali interi devono apparire nella lista associata a quella chiave nel risultato.
L'ordinamento delle parole nei valori del risultato è per dimensioni decrescenti 
e in caso di parità in ordine alfabetico crescente.

Esempio:
D1 = { 'a':[1,2,3], 'b':[3,4,5] }
D2 = { 1:['a','bb','ccc'], 3:['qq','z'], 5:['b','fff'] }
expected = {'a': ['a', 'z', 'bb', 'qq', 'ccc'], 'b': ['b', 'z', 'qq', 'fff']}
"""
  
def func3(D1 : dict[str,list[int]], D2 : dict[int,list[str]]) -> dict[str, list[str]]:
    dizio_dator = {}
    for k,v in D1.items():
        words =[]
        for n in v:
            if n in D2.keys():
                words += D2[n]
        if words:
            dizio_dator[k] = sorted(words, key=lambda x: (len(x),x) )
    
    
    return dizio_dator    # completa la funzione
# %% ----------------------------- ES.4 ----------------------------------- #
"""
Func 1: 2 punti

Implementa la funzione func1(testo : str, K : int) -> set[str] 
che riceve come argomenti:
- testo: una stringa contenente parole separate da caratteri non alfabetici
- K: un intero
e che ritorna l'insieme delle parole che appaiono esattamente K volte nel testo.

Esempio:
K = 2
testo = '''sopra la panca la capra campa, sotto la panca la capra crepa!'''
expected = {'capra', 'panca'}

"""
testo = '''essere o non essere, questo è il dilemma: 
           se sia più nobile nella mente soffrire colpi di fionda e dardi d’atroce fortuna 
           o prender armi contro un mare d’affanni e, opponendosi, por loro fine? 
           morire, dormire; nient’altro; e con un sonno dire che poniamo fine al dolore 
           del cuore e ai mille tumulti naturali di cui è erede la carne: 
           è una conclusione da desiderarsi devotamente'''
def rm_nonalfa(stringa:str) -> str:
    ret_string = ""
    for car in stringa:
        if car.isalpha() or car == " " :
            ret_string += car
        else:
            ret_string += " "
    print(ret_string)
    return ret_string
            
def func1(testo : str, K : int) -> set[str]:
    new_testo= rm_nonalfa(testo)
    dict_parole = {x:0 for x in set(new_testo.split())}
    for parola in new_testo.split():
        if parola in dict_parole.keys():
            dict_parole[parola]+=1
    return_Set = set()
    for parola in dict_parole :
        if dict_parole[parola] == K:
            return_Set.add(parola)
    return return_Set
    # completa la funzione
# %% ----------------------------- ES.5 ----------------------------------- #
"""
Func 2: 2 punti

Implementa la funzione   func2(parole : list[str]) -> dict[str, list[str]]
che riceve come argomenti:
    - parole: una lista di parole
e che ritorna un dizionario che ha come chiavi le lettere iniziali delle parole,
e come valori la lista della parole che hanno quella iniziale, 
ordinate per lunghezza crescente e in caso parità in ordine alfabetico decrescente.

Esempio:
parole = ['sei','sicuro','che','sopra','la','panca','le','capre','campino?',
          'certamente,','mentre','sotto','la','panca','le','capre','crepano!']
expected = {'s': ['sei', 'sotto', 'sopra', 'sicuro'], 
            'c': ['che', 'capre', 'capre', 'crepano!', 'campino?', 'certamente,'], 
            'l': ['le', 'le', 'la', 'la'], 
            'p': ['panca', 'panca'], 
            'm': ['mentre']}
"""
def func2(parole : list[str]) -> dict[str, list[str]]:
    dizio = {}
    for parola in parole:
        if parola [0] not in dizio.keys():
            dizio[parola[0]] = [parola]
        elif parola[0] in dizio.keys():
            dizio[parola[0]].append(parola)
    for key,value in dizio.items():
        dizio[key]= sorted(value, key=lambda x:(-len(x),x),reverse=True)        
    return dizio
    # completa la funzione

# %% ----------------------------- ES.6 ----------------------------------- #

''' func1: 4 punti
Si definisca la funzione func1(D1 : dict[str, int], D2 : dict[str, int]) -> dict[int, str]
che riceve come argomenti due dizionari D1 e D2 con chiavi stringhe e valori interi
e che torna come risultato un dizioneario con chiavi intere e valori stringhe.
Il dizionario da ritornare deve contenere come chiavi tutti gli interi che appartengono
a chiavi che non sono comuni tra D1 e D2, e come valori la concatenazione delle chiavi
di D1 o D2 che hanno quel valore.
Le chiavi da concatenare (se sono più di una) devono essere ordinate 
in ordine di lunghezza decrescente ed, in caso di parità, in ordine alfabetico crescente. 

Esempio:
D1 = {'aa': 1, 'bb': 2, 'cc': 1, 'ddd': 4}
D2 = {'bb': 4, 'ee': 4, 'ff': 1, 'ggg': 1}
#
d = str:int
Risultato: {1: 'gggaaccff', 4: 'dddee'}
'''
def func1(D1,  D2):
    dizionario_da_tornare = {}

    for chiave, valore in D1.items():
        if chiave not in D2:
            if valore not in dizionario_da_tornare:
                dizionario_da_tornare[valore] = []
            dizionario_da_tornare[valore].append(chiave)
 
    for chiave, valore in D2.items():
        if chiave not in D1:
            if valore not in dizionario_da_tornare:
                dizionario_da_tornare[valore] = []
            dizionario_da_tornare[valore].append(chiave)
 
    for k in dizionario_da_tornare:
        dizionario_da_tornare[k].sort(key=lambda x: (-len(x), x))
        dizionario_da_tornare[k] = ''.join(dizionario_da_tornare[k])
 
    return dizionario_da_tornare
    
# %% ----------------------------- ES.7 ----------------------------------- #

''' func2: 2 punti
Si definisca la funzione func2(testo: str, n: int) -> list[str]
che riceve come argomenti 
- una stringa 'testo' comnposta da parole separate da spazi, tab e accapo
- un intero 'n' 
e che torna come risultato la lista di parole del testo che hanno almeno n caratteri, 
ordinate in ordine opposto a quello di apparizione nel testo.

Esempio:
testo = 'la rana in Spagna gracida in campagna'
n = 3
Risultato = ['campagna', 'gracida', 'Spagna', 'rana']
'''
def func2(testo, n):
    lista_da_tornare  =[]
    tasto_da_iterare = testo.strip().split()
    for parola in tasto_da_iterare:
        if len(parola) >= n:
            #print(parola)
            lista_da_tornare.append(parola)
    #visto che le appendo in ordine di come compaiono nel testo originale posso invertire la lista e ottenere il risultato voluto
    return lista_da_tornare[::-1]


# %% ----------------------------- ES.8 ----------------------------------- #
'''  func3: 2 punti
Si definisca la funzione func3(S1 : set[str], S2 : set[str]) -> dict[str,list[str]]
che riceve come argomenti due insiemi di stringhe S1 e S2 e che torna come risultato
un dizionario che 
come chiavi ha le stringhe di S1 che sono prefissi di almeno una stringa di S2
e come valori la lista di stringhe di S2 che hanno quel prefisso.
Le liste associate a ciascuna chiave devono 
essere ordinate in ordine decrescente
di lunghezza e, in caso di parità, in ordine alfabetico crescente.

Esempio:
S1 = {'a', 'b', 'c'}
S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
Risultato = {'a': ['abc', 'aa', 'ab'], 'c': ['cc', 'cd'], 'b': ['bb', 'bc']}
'''

def func3(S1, S2):
    dizionario_da_tornare = {}
    for elem in S1:
        for elem2 in S2:
            if elem ==elem2[:len(elem)]:
                if elem in dizionario_da_tornare.keys():
                    dizionario_da_tornare[elem].append(elem2)
                else:
                    dizionario_da_tornare[elem] = [elem2]
    for chiave in dizionario_da_tornare:
        dizionario_da_tornare[chiave].sort(key=lambda x: (- len(x), x))
        
    return dizionario_da_tornare
     
# %% --------------------- VARIOUS CREATE TREE ---------------------------- #
"""A SEGUIRE UNA SERIE DI ESERCIZI PER PRENDERE LA MANO CON LA CREAZIONE DI ALBERI BINARI"""
import tree
# %% ---------------------------- TREE1 ------------------------------------#
def ex2(radice: tree.BinaryTree, lista_somme: list[int]) -> tree.BinaryTree:
    """
    Riceve:
    - radice: la radice di un albero binario (nodi di tipo tree.BinaryTree)
    - lista_somme: una lista di interi
    
    Restituisce:
    - un nuovo albero binario, della stessa struttura dell’albero originale,
      i cui nodi hanno valore pari a:
         valore_originale + lista_somme[profondità]
      ove 'profondità' è 0 per la radice, 1 per i suoi figli, ecc.
    
    Se la profondità di un nodo supera la lunghezza di lista_somme,
    si somma 0 (oppure puoi assumere che lista_somme sia sufficiente a
    coprire tutte le profondità presenti).
    
    L'albero originale non deve essere modificato.
    """
    # IMPLEMENTAZIONE
    pass
# %% ---------------------------- TREE2 ------------------------------------#
def ex3(radice: tree.BinaryTree) -> tree.BinaryTree:
    """
    Riceve:
    - radice: la radice di un albero binario (nodi di tipo tree.BinaryTree)
    
    Restituisce:
    - un nuovo albero binario, che abbia la stessa struttura di 'radice',
      ma in cui il valore di ciascun nodo è la somma dei valori
      presenti nel cammino dalla radice a quel nodo nell’albero originale.
    
    L'albero di partenza NON deve essere modificato.
    """
    # IMPLEMENTAZIONE
    pass
# %% ---------------------------- TREE3 ------------------------------------#
def ex4(radice: tree.BinaryTree, soglie: list[int]) -> tree.BinaryTree:
    """
    Riceve:
    - radice: la radice di un albero binario (nodi di tipo tree.BinaryTree)
    - soglie: una lista di interi (sufficientemente lunga per
              la profondità massima dell'albero)
    
    Restituisce:
    - un nuovo albero binario, con la stessa struttura, in cui
      ciascun nodo ha valore:
         originale_val se originale_val >= soglie[profondità]
         altrimenti 0
      dove 'profondità' è 0 per la radice, 1 per i suoi figli, ecc.
      
    L'albero di partenza NON deve essere modificato.
    """
    # IMPLEMENTAZIONE
    pass

