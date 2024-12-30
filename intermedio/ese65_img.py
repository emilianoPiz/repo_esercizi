import images

def es65(k,lista1,fout):
    '''
    Un quadrato sul piano e' individuato dalla sestupla  di interi (x,y,l,r,g,b) dove
    (x,y) e' la coordinata del  vertice in alto a sinistra del quadrato,  l e' la lunghezza del lato
    e gli ultimi tre valori danno il suo colore (r,g,b).
    La funzione es65(k,lista1,fout) salva in formato PNG all'indirizzo fout un'immagine quadrata
    di lato $k$ ottenuta come segue:
    Su di uno sfondo di colore nero (0,0,0) di dimensione k per k  vengono disegnati in
    sequenza i quadrati in lista1 che ricadono in tutto o in parte nella finestra k per k.
    Il colore dei quadrati non deve necessariamente essere quello originale ma viene determinato
    in base a questa regola: 
        
        il colore del quadrato e' quello originale se nessuno dei pixel su cui incide il quadrato ha un colore maggiore, 
        in caso contrario il colore del quadrato sara' dato dal colore massimo tra quello dei pixel su cui incide.
        
    Un colore(x,y,z) e' maggiore di un altro (x',y',z') se x>x' o a parita' y>y' o a parita' z>z'.
    Infine la funzione deve restituire il numero di pixel di  colore nero che compaiono nell’immagine
    dopo aver inserito i quadrati.
    Ad esempio se
    lista1=[(20,50,20,0,255,0),(30,60,20,255,0,0),(60,50,20,255,0,0),(70,60,20,0,255,0)]
    con es65(100,lista1,'prova1.png') si otterra' la figura nel file prova1.png
    e verra' restituito il valore 8600.
    '''
    def black_counts(img,counts):
        #per ogni pixel che trova nero, aggiunge un 1 in una matrice della stessa dimensione all'immagine
        for x, row in enumerate(img):
            for y, pixel in enumerate(row):
                if pixel == (0,0,0):
                    counts[x][y] = 1 
                    
    def draw_sqr(x,y,l,r,g,b,img):
        #riceve un oggetto del tipo ( x 20 , y 50 , l 20 , r 0 , g 255 , b 0 )
        #applica la legge di paragone e disegna il quadrato
        #il quadrato inizia da img[x][y] fino a img[x+l][y+l]
        lato = len(img)
        for i in range (x,x+l):
            for j in range(y,y+l):
                if x < lato and y < lato:
                    r1,g1,b1 = img[i][j]
                    if img[i][j] == (0,0,0):
                        img[i][j]= (r,g,b)
                    if r > r1 or (r == r1 and g > g1) or (r == r1 and g == g1 and b >= b1):
                        img[i][j]= (r,g,b)
    
    #inizio
    black  = (0,0,0)   
    img    = [[ black for _ in range(k)] for _ in range(k)]
    counts = [[ 0     for _ in range(k)] for _ in range(k)] 

    #creo N quadrati
    for sqr in lista1:
        draw_sqr(*sqr,img)
    
    #dopo aver creato i quadrati vedo quanto nero resta    
    black_counts(img,counts)
    
    #fine
    images.save(img, fout)    
    #contare gli uni in counts 
    tot = 0
    for lista in counts:
       tot += sum(lista)
    return tot
   