import images


def es75(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut):
    """
    Definite la funzione es75 che riceve come argomenti
        h:                  altezza della immagine
        w:                  larghezza della immagine
        listaColori:        una lista di N colori nel formato (R, G, B) che devono essere applicati, nell'ordine da sinistra a destra, ai rettangoli
        listaAltezze:       una lista di N altezze < h
        larghezzaPalazzo:   la larghezza di ciascuno dei rettangoli da disegnare
        filePngOut:         path del file PNG in cui salvare l'immagine
        :return             numero di pixel cambiati piu' di 1 volta
    e che crea una immagine di dimensioni w,h con sfondo blu (0,0,255).
    Sulla immagine devono essere disegnati N rettangoli equispaziati tutti di larghezza larghezzaPalazzo, appoggiati in basso.
    L'altezza ed il colore del rettangolo i-esimo (da sinistra a destra) e' data dallo i-esimo elemento delle liste listaAltezze e listaColori.
    I rettangoli devono essere disegnati in modo che i rettangoli piu' bassi restino in primo piano rispetto ai rettangoli piu' alti.
    La funzione deve inoltre ritornare il numero di pixel che appartengono a piu' di un rettangolo
    (ovvero quelli di rettangoli che sono stati coperti da almeno un altro rettangolo)

    Nota:   assumete che la larghezza w della immagine sia sempre un multiplo di (1+N),
            in modo che il centro della posizione x di ciascun palazzo sia un valore intero
    Nota:   assumete che larghezzaPalazzo sia un valore pari
    Nota:   assumete che tutte le altezze siano minori o uguali dell'altezza h della immagine
    """
    
    #1 disegnare n rettangoli
    #la distanza deve essere uguale a larghezzaPalazzo, e devono essere a -h da top
    #palazzo0 = listaAltezze0,listaColori0
    #rettangolo1.h > rettangolo2.h => rettangolo2 deve stare davanti
    #blue = (0,0,255)
    
    #come gestire il fatto che i pixel più bassi devono stare davanti? potrei prima 
    
    #COSA SERVE PER CHIUDERLA:
        #1. Img_out scritta su filePngOut
            # fare uno sfondo blue di dimensioni h,w  V
            #TODO creare N rettangoli (questo significa eseguire un operazione N volte dove N è la lunghezza di listaColori o listaAltezze)
            # -larghi = larghezza_palazzo
            # -alti = lista_altezze[i]
            # -di colore = lista_colori[i] 
            
        #2. contatore numero pixel appartenenti a più rettangoli
            #TODO : creare un condizionale che si attivi mentre un pixel viene colorato mentre non è (0,0,255)
    def create_BG(w,h,colore):
        return [[colore for _ in range(w)] for _ in range(h)]
    def drawRettangolo(img, l, r, t, b, c, counts):
        # si evita di sbordare dalla immagine
        w = len(img[0])
        h = len(img)
        l = max(l, 0)
        r = min(r, w)
        t = max(t, 0)
        b = min(b, h)
        for x in range(l, r):
            for y in range(t, b):
                img[y][x] = c
                counts[y][x] += 1
                
    #inizio
    blue = (0,0,255)
    N = len(listaAltezze)
    #trovo le combinazioni di colore-altezza, qui l'insieme dei rettangoli
    #esempio [1,2,3] [(0,2,4),(1,23,4),(0,2,8)] = [(1, (0, 2, 4)), (2, (1, 23, 4)), (3, (0, 2, 8))]
    rettangoli = list(zip(listaAltezze,listaColori))
    #ogni volta che su un pixel verrà scritto un colore verrà aggiornato l'interno alle stesse coordinate di counts
    counts = [[0 for _ in range(w)]for _ in range(h)] 
    #creo sfondo
    img_new = [[blue for _ in range(w)] for _ in range(h)]
      
    #step = larghezza immagine divisa para per il numero di palazzi più uno 
    step = w//(N+1)
   
    #il punto in basso a sinistra del primo rettangolo
    #sarà distante dal bordo dell'immagine pari alla distanza degli spazi che separeranno poi tutti i rettangoli
    start = step - larghezzaPalazzo//2
    end = start + larghezzaPalazzo
   
    #aggiungo i dati necessari al rettangolo per essere disegnato     
    for indice, altezza, colore in enumerate(rettangoli):
        rettangoli.append((start, end, h-altezza, h, colore))
        print(rettangoli[indice])
        start += step
        end += step
    #ordino i rettangoli in base alla loro altezza 
    rettangoli.sort(key=lambda r: r[2])
   
    #creo N palazzi 
    for r in rettangoli:
        drawRettangolo(img_new, *r, counts)
    images.save(img_new, filePngOut)
   
    #conto quanti cambiati ci sono guardando in counts, dove un pixel è stato scritto più di una volta
    cambiati = 0
    for line in counts:
        for n in line:
            if n > 1:
                cambiati += 1
    return cambiati
"C:/Users/User/Desktop/università/esercitazio/FONDAMENTI DI PROGRAMMAZIONE/esercizi/università(FONDAMENTI DI PROGRAMMAZIONE)/repo_esercizi/intermedio/test.png"

es75(250, 100, [(269,200,129)], [50], 10, "C:/Users/User/Desktop/università/esercitazio/FONDAMENTI DI PROGRAMMAZIONE/esercizi/università(FONDAMENTI DI PROGRAMMAZIONE)/repo_esercizi/intermedio/test.png")