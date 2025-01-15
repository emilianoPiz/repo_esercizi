"""
Si definisca la funzione ricorsiva (o che usa una vostra funzione ricorsiva) es68(dir, estensioni),
che deve contare quanti file di certi tipi si trovano in una directory o in una delle sue sottodirectories,
e che riceve come argomenti
    dir: il path della directory in cui cercare
    estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
La funzione deve tornare un dizionario che ha come chiavi le estensioni passate come argomento
e come valori il numero di file il cui nome termina in quel modo, solo se > 0
(ovvero, se nessun file con una data estensione appare nella directory o nelle sottodirectories
la chiave non deve apparire nel dizionario tornato dalla funzione).

Tests: date alcune directory contenenti file di tipo (ext) diverso, si chiama la funzione per contare alcuni dei tipi di file nelle diverse directory
Test: che la funzione sia ricorsiva
"""




import os
import os.path
def conta_et_esplora (path,diz,estensioni):
    lista_path= os.listdir(path)
    for elem in lista_path:
        full_path = path + "/" +elem
        if os.path.isdir(full_path):
            es68(path, diz)
        elif os.path.isfile(full_path):
            for exten in estensioni:
                if full_path.endswith(exten):
                    diz[exten] +=1
    
def es68(directory, estensioni):   
    occorrenze = {ext:0 for ext in estensioni} 
    conta_et_esplora(directory, occorrenze,estensioni)
    diz_dator ={chiave:valore for chiave,valore in occorrenze.items() if valore>0}
    return diz_dator