'''
coding: utf-8 -*-

Created on Fri Dec 27 19:15:12 2024

@author:emi 
  
    ATTENZIONE: usate come separatore dei file il carattere "/" che funziona sia in Windows che in Linux
    ATTENZIONE: e' VIETATO usare la funzione os.walk

    Si definisca la funzione  es80(dir1, parole), che presi in input:
        dir1:   il path di una directory
        parole: un insieme di parole (stringhe di caratteri tra 'a' e 'z')
    esegue il seguente lavoro:
    Ricerca nella directory il cui path e'  dir1 e nelle sue subdirectories eventuali file con estensione .txt contenenti
    stringhe appartenenti all'insieme delle parole e restituisce un dizionario delle parole trovate.
    Nel dizionario restituito devono comparire  solo le parole effettivamente riscontrate all'interno
    dei file con estensione .txt e ciascuna chiave deve avere  come attributo una lista  di due interi.
    Il primo elemento della lista riporta il numero complessivo di volte che la parola  e' stata ritrovata in questi file,
    il secondo elemento della lista riporta la profondita' massima dei file in cui la parola e' risultata presente.
    La profondita' dei file nella directory dir1 vale 0
    Per parola intendiamo una sequenza di lunghezza massimale di caratteri tra 'a' e 'z'.
    Si puo' assumere che tutti i file con estensione .txt contengono solo parole  separate da  spazi, tab o andate a capo.
    (non sono presenti caratteri maiuscoli o segni di interpunzione)
    '''
    #cosa serve per chiuderla:
        #1. la lista di tutti i path che ci sono 
        #2. un dizionario che contiene tutte le parole nei file che compaiono in parole come chiavi e una lista di due interi
        #3. per ogni path conto quant / ha dopo la fine di dirname1 e aumento il counter adatto
        #4. inolte conto quante volte la parola compare

    #1. per ogni file di testo cerca nel suo testo le parole che che ci sono:
             #se la parola non è chiave del dizionario ed è presente tra le parole:
                 #si inizializa un attr parola:[0,x] dove x è il numero di / dopo dir1
             #se è presente nel dizionario:
                 #si aumenta int1 di 1 e si aggiorna x con il valore corrente
       
    #int1 è il numero di volte che la parola è stata trovata
    #int2 è la profondità massima di cartelle in cui la parola è stata trovata 

    #come ottenere la depth delle cartelle:
        #conto rispetto a dirname1 quante volte compare / nel path se non compare è il livello 0, per ogni / che trova si aumenta di un livello

import os
def cerca_file_txt(dir_corrente):
    # questa funzione esplora ricorsivamente tutte le cartelle e sotto cartelle della directory data in input
    risultati = []
    
    for elemento in os.listdir(dir_corrente):
        path = dir_corrente + "/" + elemento
        if os.path.isfile(path) and path.endswith(".txt"):
            #se trova file di testo lo appende ad una lista che tornerà
            risultati.append(path)
        elif os.path.isdir(path):
            #se non è file di testo richiama la funzione in modo ricorsivo e aggiunge il return al risultato
            risultati.extend(cerca_file_txt(path))

    return risultati
 
    
def costruisci_dizionario_parole(lista_path, parole,dir1):
    risultati = {}

    for path in lista_path:
        #conto quante "/" ci sono dopo dir1 
        relative_path = path[len(dir1):].strip("/")
        depth = relative_path.count("/")
        
        #leggo le parole da ogni file di testo nella lista e creo una lista con ogni parola trovata
        with open(path, mode="r",encoding="utf-8") as f :
            testo_raw = f.read()
        lista_parole = testo_raw.strip().split()

        for parola in lista_parole:
            if parola in parole and parola not in risultati.keys():
                #caso1: ho la parola nelle parole in input ma ancora non compare nel dizionario 
                #quindi inizializzo il contatore delle occorrenze e imposto la prima chiave = parola
                risultati += {parola :[1,depth]}
            elif parola in parole and parola in risultati.keys():
                #caso2: se la parola è già nel dizionario come sua chiave , allora contorllo se la depth è maggiore di quella attuale 
                #e incremento il suo contatore di 1
                risultati[parola][0] +=1
                risultati[parola][1] = max(risultati[parola][1], depth)
    return risultati
                      
def es80(dir1, parole):
    #chiamo le due funzioni e torno il risultato
    lista_path = cerca_file_txt(dir1)
    dizionario_da_tornare = costruisci_dizionario_parole(lista_path, parole,dir1)

    return dizionario_da_tornare
             
            
    