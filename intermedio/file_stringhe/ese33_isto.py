
    ''' 
    Implementate la funzione es33(fname1,fname2) prende in input l'indirizzo di un  file di testo fname e
    costruisce un istogramma con le frequenze di alcuni dei caratteri presenti nel  file di testo. 
    Salva l'istogramma creato nel file di testo fname2 e restituisce il numero di linee di cui e' composto.
    L'istogramma contiene tante linee quanti sono i caratteri tra 'a' e 'z' presenti nel testo.
    Se un certo carattere x compare nel testo  y volte allora nell'istogramma ci sara' 
    una riga con una stringa composta dal carattere x ripetuto y volte. Le righe dell'istogramma 
    vanno ordinate per lunghezza decrescente dei caratteri che vi compaiono e 
    lessicograficamente a parita' di lunghezza.
    Ad esempio se il file fname1 contiene il testo 'Monti, Sterbini e Spognardi' allora
    il valore restituito dalla funzione sara' 11 e  l'istogramma sara'
    iiii
	nnn
	ee
	oo
	rr
	tt
	a
	b
	d
	g
	p
    '''
def es33(fname1, fname2):

    with open(fname1, mode="r", encoding="utf-8") as f:
        testo_raw = f.read().lower()

    occorrenze = {}
    for char in testo_raw:
        if 'a' <= char <= 'z':  
            occorrenze[char] = occorrenze.get(char, 0) + 1

    occorrenze_ordinate = sorted(occorrenze.items(), key=lambda x: (-x[1], x[0]))

    righe = [char * count for char, count in occorrenze_ordinate]

    with open(fname2, mode="w", encoding="utf-8") as f:
        f.write("\n".join(righe))

    return len(righe)

            
            
            
            
            
            
        
        
        
    
    
    
    
                
                














 