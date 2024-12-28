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
    def create_BG(w,h,colore):
        return [[colore for _ in range(w)] for _ in range(h)]
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
            
    #inizio
    blue = (0,0,255)
    counter = 0 
    #trovo le combinazioni di colore-altezza
    #esempio [1,2,3] [(0,2,4),(1,23,4),(0,2,8)] = [(1, (0, 2, 4)), (2, (1, 23, 4)), (3, (0, 2, 8))]
    combinazione_altezza_colore = list(zip(listaAltezze,listaColori))
    
    #creo sfondo
    img_new = create_BG(w,h,blue)
    
    #creo N palazzi ripeto N volte
    for altezza,colore in combinazione_altezza_colore:
        #il primo da fare è un rettangolo alto = altezza, colore, larghezza = larghezza_palazzo e cosi via
        #il centro deve essere? larghezza_palazzo/2
        #TODO spazio_tra_essi = larghezza_palazzo * len(combinazione,altezzacolore) - w / len(combinazione,altezzacolore)+1
        #come trovo il prossimo centro?
        #come calcolo se uno è da sovrascrivere o no?
        
        #se considero altezza_attuale come intervallo e trovo un pixel non blue 
        #guardando oltre h significa che questo rettangolo sarà più basso dell'altro
        spazio_tra_essi = (larghezzaPalazzo * len(combinazione_altezza_colore)) - w / len(combinazione_altezza_colore) + 1
        x_finale = spazio_tra_essi + larghezzaPalazzo
        
        for y in range(h - altezza , h):
            for x in range(spazio_tra_essi , x_finale):   
                if img[x,y] not blue:
                    img_new[y][x] = colore
                    counter += 1 
    
    #fine
    images.save(img_new, filePngOut)
    return counter 