def es30(fname1,fname2,fname3):
    ''' 
    Si implementi la funzione es30(fname1,fname2,fname3) prende in input l'indirizzo di tre file di testo.
    Il primo file di testo contiene un messaggio codificato dove ogni carattere e' stato 
    sostituito da un intero di tre cifre.
    Tutti i caratteri non numerici devono essere trasferiti come sono.
    Nel secondo file  e' possibile ritrovare le corrispondenze numeri-caratteri tra i numeri 
    del testo e il rispettivo carattere. 
    Piu' precisamente questo secondo file e' organizzato in righe,  in ciascuna riga sono 
    presenti un carattere  e un intero  di tre cifre  che gli corrisponde nel file di testo separati da almeno uno spazio.
    Numeri diversi possono far riferimento ad uno stesso carattere e non tutti i numeri che appaiono in fname1
    sono necessariamente presenti nel file di decodifica.
    La funzione es30 deve decodificare il messaggio presente nel primo file grazie 
    alle informazioni contenute nel secondo.
    I numeri non presenti nel secondo file vanno decodificati con il simbolo '?'.
    Il messaggio decodificato va poi salvato nel terzo file.
    La funzione infine restituisce il numero di caratteri decodificati con il valore '?' presenti nel file decodificato.
    Ad esempio se 
    - il file fname1 contiene il testo '991118991991345      103    091027003091103?'
    - il file fname2 contiene il testo 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
    il testo decodificato da registrare in file3 sara': 'tutt? a n?nna?' e la funzione restituisce il numero 2.
    Potete assumere che i caratteri numerici appaiano sempre raggruppati in triplette.
    '''
    cifrario = {}
    counter =  0

    with open(fname1, mode="r", encoding="utf-8") as f:
        messaggio_in_codice = f.read()

    with open(fname2, mode="r", encoding="utf-8") as f1:
        testo_raw_cifrario = f1.read().splitlines()

    for riga in testo_raw_cifrario:
        parti = riga.split()
        if len(parti) == 2:
            valore, chiave = parti[1], parti[0]
            cifrario[valore] = chiave

    def decrypt(cifrario, messaggio_in_codice):
        nonlocal counter
        blocchi = [] 
        i = 0

        while i < len(messaggio_in_codice):
            if messaggio_in_codice[i].isdigit() and i + 2 < len(messaggio_in_codice): 
                blocco = messaggio_in_codice[i:i+3] 
                if blocco in cifrario:
                    blocchi.append(cifrario[blocco])
                else:
                    blocchi.append("?")
                    counter += 1
                i += 3 
            else:
                blocchi.append(messaggio_in_codice[i]) 
                i += 1
        return blocchi

    blocchi = decrypt(cifrario, messaggio_in_codice)
    messaggio_decriptato = "".join(blocchi)

    with open(fname3, mode="w", encoding="utf-8") as fOut:
        fOut.write(messaggio_decriptato)

    return counter














