'''
Definite la funzione es63(fileParole,fileTerne) che prende in input:
- il path FileParole ad un file di testo contenente parole, una parola per ogni riga,
- il path fileTerne di un file di testo da creare.
La funzione legge le parole presenti nel file di FileParole e crea
un nuovo file di testo che salva all'indirizzo fileTerne e restituisce infine il
numero totale di caratteri presenti nelle parole del file FileParole (ignorando spazi e accapi).
Il file creato ha lo stesso numero di righe del file letto (una per ogni parola)
ma le parole in ciascuna riga sono sostituite da terne di interi. Piu' precisamente in
corrispondenza della generica parola s viene prodotta la stringa con la tupla
(a,b,c) seguita da accapo,
dove a e' la lunghezza della parola s, b e' il numero di vocali presenti nella
parola s e c e' il numero di lettere maiuscole presenti nella parola s.

Ad esempio se il file delle parole contiene le due parole 'PytHon' e 'fonDAMenti'
la funzione deve creare e salvare in fileTerne un  file di due righe con le due
terne (6,1,2) e (10,4,3) e restituire poi l'intero 16.
'''

from string import ascii_uppercase
def es63(fileParole, fileTerne):
    #1 parola =  1 terna (a=lunghezza,b=vocali,c=maiusc)
    #restituire numero totale di caratteri presenti nelle parole del file FileParole (ignorando spazi e accapi).

    #inizio
    #leggo le parole dal file di testo
    #per ogni parola stabilisco la sua tripla
    #creo una stringa con le tuple nell'ordine in cui le ho appese
    #salvo la stringa su fout
    #fine 
    
    #leggo le parole
    counter=0
    stringa = ""
    with open(fileParole,mode='r',encoding="utf-8") as f:
        testo_raw = f.read()
    lista_parole = testo_raw.strip().splitlines()
    for parola in lista_parole:
        a,b,c = 0,0,0
        #lunghezza parola
        a = len(parola)
        #conta vocali e controlla se è maiusc
        for char in parola:
            counter +=1
            if char in "aeiouAEIOU":
                b+=1
            if char in ascii_uppercase:
                c+=1
        stringa += str((a,b,c))+"\n"
    with open(fileTerne, mode="w",encoding="utf-8") as fOut :
        fOut.write(stringa)
    return counter
    