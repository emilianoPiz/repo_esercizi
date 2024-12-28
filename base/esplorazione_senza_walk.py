# -*- coding: utf-8 -*-
"""
esplorazione directory senza os.walk
questa serie di 8 esericizi serve per imparare ad esplorare le directory 
e sotto directory in maniera ricorsiva. la difficoltà è crescente
l'ultimo esercizio è preso dalla simulazione d'esame di fondamenti di programmazione
del 21/12/24 per studenti teledidatti del professor Sterbini

Esercizio 1: Leggere i file in una directory
Scrivi una funzione list_files(dirname) che riceve come argomento una directory
 e ritorna una lista dei nomi di tutti i file presenti (non le directory).
Obiettivo: Familiarizzare con os.listdir e os.path.isfile.
"""
import os
def list_files(dirname: str) -> list:
    lista_da_tornare =[]
    lista_directory = os.listdir(dirname)
    for elemento in lista_directory:
        percorso = dirname + "/"+elemento
        if os.path.isfile(percorso):
            lista_da_tornare.append(percorso)
    return lista_da_tornare


"""

Esercizio 2: Filtrare i file per estensione
Estendi la funzione precedente per includere un filtro 
che restituisce solo i file con estensione .txt.

Obiettivo: Comprendere come filtrare i risultati di una lista.
"""
def search_text(dirname):
    lista_da_tornare =[]
    lista_directory = os.listdir(dirname)
    for elemento in lista_directory:
        percorso = dirname + "/"+elemento
        if percorso.endswith(".txt"):
            lista_da_tornare.append(percorso)
    return lista_da_tornare
    

"""
Esercizio 3: Controllare il contenuto di un file
Scrivi una funzione file_contains(file_path, word) 
che riceve un file e una parola e ritorna True se la parola è contenuta nel file, altrimenti False.

Obiettivo: Imparare a lavorare con l'apertura e la lettura dei file.
"""
def file_contains(file_path, word):
    with open(file_path, mode="r", encoding="utf-8") as f:
        testo_raw = f.read()
    lista_parole = testo_raw.strip().split()
    booleano =  True if word in lista_parole else False
    return booleano
"""
Esercizio 4: Verificare più parole in un file
Estendi la funzione precedente in file_contains_all(file_path, words) per verificare se un file contiene tutte le parole di una lista words.

Obiettivo: Usare operazioni di controllo multiple (ad esempio all()).
"""
def file_contains_all(file_path, words):
    with open(file_path, mode="r", encoding="utf-8") as f:
        testo_raw = f.read()
    lista_parole = testo_raw.strip().split()
    return all(parola for parola in lista_parole if parola in words)
     
 
"""
Esercizio 5: Combinare condizioni sui file
Scrivi una funzione file_meets_criteria(file_path, necessary, forbidden) 
che verifica se un file contiene tutte le parole in necessary e nessuna parola in forbidden.

Obiettivo: Implementare condizioni combinate e lavorare con liste.
"""
def file_meets_criteria(file_path, necessary, forbidden):
    with open(file_path, mode="r", encoding="utf-8") as f:
        testo_raw = f.read()
    lista_parole = testo_raw.strip().split()
    contiene_necessary = all(parola in lista_parole for parola in necessary)
    contiene_forbidden = any(parola in lista_parole for parola in forbidden)
    return contiene_necessary and not contiene_forbidden
"""
Esercizio 6: Leggere una directory con sottodirectory
Scrivi una funzione list_all_files(dirname) che ritorna una lista di tutti i file, 
inclusi quelli presenti nelle sottodirectory. 
Usa una funzione ricorsiva per esplorare le directory.
Obiettivo: Introdurre la ricorsione per l'esplorazione.

caso base: è file
passo ricorsivo: è dir con file

"""
def list_all_files(dirname):
    lista_file = []
    for elemento in os.listdir(dirname):
        percorso_completo = dirname + '/' + elemento
        if os.path.isfile(percorso_completo):
            # Caso base: è un file
            lista_file.append(percorso_completo)
        elif os.path.isdir(percorso_completo):
           # Passo ricorsivo: esplora la sottodirectory
           lista_file.extend(list_all_files(percorso_completo))
    return lista_file

"""

Esercizio 7: Filtrare file per estensione con sottodirectory
Estendi la funzione precedente per includere solo i file .txt.

Obiettivo: Raffinare la logica di filtraggio nell’esplorazione ricorsiva.
"""
def list_all_txt_files(dirname):
    lista_file = []
    for elemento in os.listdir(dirname):
        percorso_completo = dirname + '/' + elemento
        if os.path.isfile(percorso_completo) and percorso_completo.endswith(".txt"):
            # Caso base: è un file di testo, gli altri file non mi interessano
            lista_file.append(percorso_completo)
        elif os.path.isdir(percorso_completo):
           # Passo ricorsivo: esplora la sottodirectory
           lista_file.extend(list_all_txt_files(percorso_completo))
    return lista_file

"""
Esercizio 8: Applicare criteri ai file trovati
Scrivi una funzione find_files_with_criteria(dirname, necessary, forbidden) 
che esplora una directory e ritorna i file .txt che soddisfano i criteri necessary e forbidden.

Obiettivo: Integrare tutto ciò che hai imparato fino a ora.
"""
def find_files_with_criteria(dirname, necessary, forbidden):
    lista_file =[]
    for elemento in os.listdir(dirname):
        percorso = dirname + "/"+elemento
        if percorso.endswith(".txt"):
            with open(percorso, mode="r",encoding="utf-8") as f:
                testo_raw = f.read()
            lista_parole = testo_raw.strip().split()
            contiene_necessary = all(parola in lista_parole for parola in necessary)
            contiene_forbidden = any(parola  in lista_parole for parola in forbidden)
            if contiene_necessary and not contiene_forbidden:
                lista_file.append(elemento)
        elif os.path.isdir(percorso):
            lista_file.extend(find_files_with_criteria(percorso,necessary,forbidden))
    return lista_file
            
                            
"""
TEST YOUR STRENGHT:

Si definisca la funzione ex1(dirname, necessary, forbidden), ricorsiva o che utilizza funzioni 
o metodi ricorsivi, che riceve come argomenti:
 - dirname: il nome di una directory in cui cercare dei file
 - necessary: una lista di parole che devono essere presenti nei file trovati
 - forbidden: una lista di parole che devono essere assenti  nei file trovati
e che esplora la directory e tutte le sue sottodirectory per cercare i file che soddisfano le seguenti condizioni:
- hanno come estensione ensdwith('.txt')
- contengono tutte le parole presenti in 'necessary' all(necessary)
- non contengono nessuna delle parole presenti in 'forbidden' not in forbidden

La funzione ritorna come risultato la lista di percorsi dei file trovati, return lista_da_tornare = [path,path,path]
ordinati in ordine di profondità crescente, e in caso di parità in ordine alfabetico decrescente.

AVVISO 1: Si consiglia di utilizzare le funzioni os.listdir,
os.path.isfile e os.path.isdir e NON la funzione os.join in
Windows. Utilizzare la concatenazione tra stringhe con il carattere '/'.

AVVISO 2: è vietato utilizzare la funzione os.walk

NOTA: se definite la parte ricorsiva in una funzione separata,
definitela allo stesso livello della funzione ex1 e NON come inner function

Esempio:
dirname = 'ex1/AAA'
necessary: ['ciao', 'mamma']
forbidden: ['papa', 'nonno']

Risultato: ['ex1/AAA/share/recollection/lamentable/dogsled.txt', 'ex1/AAA/heavy/tomorrow/flare/cellar.txt', 
            'ex1/AAA/heavy/spoon/cranberry.txt', 'ex1/AAA/heavy/roster/prosecutor.txt', 'ex1/AAA/gifted/systemize/due.txt', 
            'ex1/AAA/gifted/systemize/distinction.txt', 'ex1/AAA/share/help.txt', 'ex1/AAA/regime.txt', 'ex1/AAA/mayonnaise.txt']
"""