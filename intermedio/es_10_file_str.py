  
    

'''
    Es 10: 3 punti
progettare la funzione es10(ftesto,k) che, presi in 
input l'indirizzo di un file di testo ed un intero k, 
restituisce una stringa di caratteri lunga k.

Il file di testo contiene stringhe di diversa lunghezza 
(una per riga ed ogni riga termina con '\n'), si guardi 
ad esempio il file f9.txt. 
I k caratteri della stringa restituita  dalla funzione si ottiengono
considerando le stringhe lunghe k presenti nel file di testo. 
L'i-mo carattere della stringa sara' il carattere che compare con maggior 
frequenza come i-mo carattere delle stringhe lunghe k nel file di testo (in caso 
di parita' di occorrenze viene scelto il carattere che precede 
gli altri lessicograficamente). 
Nel caso il file di testo non contenga parole lunghe k allora viene restituita 
la stringa vuota.  
Ad Esempio, per il file di testo f9.txt e k=3 la funzione restituisce  la stringa 'are' a 
seguito della presenza in f9.txt delle seguenti 4 stringhe lunghe 3:
tre
due
amo
ora 
'''
#leggere le parole
#filtrare le parole lunghe K
#costruire la stringa da tornare
    #1 contare le occorrenze di ogni i-esima lettera 
    #2 fare una lista con quelle più frequenti
    #3mettere quelli più frequenti nell'ordine richiesto, a parità di frequenza allora ordine alfa
#restituire una stringa


def es10(ftesto,k):
    #inizio
    parole_lunghe_k = []
    stringa_da_tornare = ""
    # leggo testo
    with open(ftesto, mode="r",encoding="utf-8") as f:
        testo_raw = f.read()
    # rimuovo spazi e trasformo le parole in lista di stringhe 
    lista_parole = testo_raw.strip().split()
    # trovo le parole lunghe k 
    for parola in lista_parole:
        if len(parola) ==k:
            parole_lunghe_k.append(parola)

    # creo la lista dei contatori per ogni posizione
    lista_contatori = [{} for _ in range(k)]
    
    # aggiorno i contatori per ogni parola
    for parola in parole_lunghe_k:
        for i, char in enumerate(parola):
            lista_contatori[i][char] = lista_contatori[i].get(char, 0) + 1
    
    # trovo il carattere più frequente, seguendo il criterio richiesto
    caratteri_finali = []
    for contatore in lista_contatori:
        # prima condizione   =  char è più frequente
        # seconda condizione =  se il conteggio è uguale allora ordine ascii
        best_char = None
        best_count = -1
        for char, count in contatore.items():
            if count > best_count or (count == best_count and char < best_char):
                best_char = char
                best_count = count
        caratteri_finali.append(best_char)
    
    # unisco i caratteri nella stringa
    stringa_da_tornare = ''.join(caratteri_finali)
    #fine
    return stringa_da_tornare
        
                
