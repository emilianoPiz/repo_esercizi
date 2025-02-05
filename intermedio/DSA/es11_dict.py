'''
    Es 11: 3 punti
progettare la funzione es11(ftesto) che, preso in input 
l'indirizzo di un file di testo restituisce un dizionario avente per chiavi delle stringhe 
ed attributo liste di  stringhe.
Il file di testo contiene stringhe distinte di caratteri, si guardi 
ad esempio il file f9.txt. 
Le chiavi del dizionario si ottengono dalle stringhe presenti nel file dopo aver 
eliminato da queste le vocali ed aver riordinato lessicograficamente i caratteri rimanenti 
(ad esempio dalla stringa 'angelo' si ottine la chiave 'gln').
Attributo della chiave e' la lista contenente le stringhe del file che l'hanno generata. 
Nota che  stringhe diverse possono generare una stessa chiave come nel caso 
di  'casa', 'caso' e 'cose'
Le stringhe nella lista devono comparire  ordinate per lunghezza decrescente, a parita' 
di lunghezza, lessicograficamente.

Ad Esempio, per il file di testo f10.txt  la funzione restituisce  il dizionario:
{'prt': ['parto', 'porta'], 
'r': ['era', 'ora'], 
'pr': ['arpia', 'arpa'], 
'cs': ['casa', 'cosa'], 
'fll': ['follia', 'fallo', 'folla'], 
'rt': ['otre', 'tre'], 
'lp': ['piolo', 'polo']
}
'''
#generare dict della forma {str:[str,str]}

#inizio
#dichiaro vocali e dizionario da tornare
#leggere il testo del file
#rimuovere le vocali
#riordinare le consonanti restanti in ordine lessiografico
#rendere le stringhe chiavi 
#mettere come valori delle chiavi quelle parole che hanno le stesse consonanti
#ordinare la lista valore
#return dizionario
#fine

def es11(ftesto:str)->dict :
    #inizio
    vocali = ["a","e","i","o","u"]
    dizionario_da_tornare = {}
    #prendo il testo
    with open(ftesto,mode="r",encoding="utf-8")as f :
        testo_raw = f.read()
    #rendo il testo una lista pulita di parole
    lista_parole = testo_raw.strip().split()
    #passo in rassegna ogni parola per togliere le vocali
    for parola in lista_parole:
        chiave = ""
        lista_lettere = [c for c in parola]
        for c in lista_lettere:
            if c not in vocali:
                chiave += c 
        #qui ho chiave e parola, quindi se compare già la chiave appendo la parola co quelle consonanti
        #altrimennti la creo
        chiave = ''.join(sorted(chiave))
        if chiave not in dizionario_da_tornare:
            dizionario_da_tornare[chiave] = [parola]
        else:
            dizionario_da_tornare[chiave].append(parola)
    #riordino in base alla richiesta        
    for chiave in dizionario_da_tornare:
        dizionario_da_tornare[chiave] = sorted(dizionario_da_tornare[chiave], key=lambda x: (-len(x), x))
    return dizionario_da_tornare
            



