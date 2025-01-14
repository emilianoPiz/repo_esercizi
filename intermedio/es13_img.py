# -*- coding: utf-8 -*-
"""
ESERICIZI IMMAGINI LIVELLO ESAME

'''    
    Es 12: 4 punti
    Progettare la  funzione es13(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e  fimm1 di due file .PNG. 
    - legge l'immagine da fimm ne modifica i colori dei pixel e  la salva poi 
      all'indirizzo fimm1.
    - restituisce infine il numero di colori DIFFERENTI presenti nell'immagine modificata.
      I colori dei pixel dalla nuova immagine si ottengono a partire da quelli 
      dell'immagine originaria con la seguente  procedura:.
      le tuple dei DIFFERENTI colori presenti nella prima immagine vengono ordinate in 
      ordine crescente.
      La sequenza ordinata di tuple  che si ottiene viene suddivisa a gruppi di 50 (se il 
      numero totale di tuple non e' un multiplo di 50 allora l'ultimo gruppo avra' 
      meno di 50 elementi). 
      I colori corrispondenti alle tuple che compaiono come  primo elemento di 
      ciascun gruppo saranno i colori assegnati ai pixel dell'immagine.
      tutti i pixel che avevano colori corrispondenti a tuple finite in uno stesso 
      gruppo avranno come colore quello corrispondente alla prima tupla del gruppo.
      Ad esempio i pixel che avevano colori corrispondenti alle tuple finite nelle prime 50 posizioni 
      della sequenza ordinata  avranno ora tutti lo stesso colore (dato dal colore corrispondente 
      alla tupla che occupa la prima posizione  della sequenza), i pixel 
      che avevano colori le cui tuple  nella sequenza occupano le posizioni 
      da 50 a 99 avranno tutti lo stesso  colore (corrispondente alla tupla in posizione  
      50) ecc. ecc. 
      Sull'immagine Fig1.png la funzione deve produrre il file RisFig1.png e restituire il numero ?
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
        
    #come capire i colori da cambiare:
        1. nella prima immagine si ordinano in ordine crescente tutte le tuple di colori differenti 
        2. la sequenza ottenuta viene divisa in gruppi da 50 (con probabilmente l'ultimo membro con meno di 50 elementi)
        3. per ogni gruppo si prende la prima tupla che compare e si scrive quel colore su tutti i pixel che hanno un colore
               compreso nel gruppo della tupla presa
    contare ogni volta che avviene un cambio colore                                                  
"""
import images
def es13(fimm,fimm1):
    img = images.load(fimm) #immagine da cui prendere i colori
    lista_tuple  = []        #lista delle tuple spacchettate
    lista_da_50  = []        #da inserirci al massimo 50 elementi 
    lista_gruppi = []        #da inserirci i gruppi da 50 elementi
    
    #spacchetta pixel 
    for riga in enumerate(img):
        for pixel in enumerate(riga):
            lista_tuple.append(pixel)
    #ordina pixel  
    lista_tuple = sorted(lista_tuple)
    
    #dal primo elemento al 50esimo riempi una lista, quando arrivi al 50 inviala e svuotale
    for elem in lista_tuple:
        if len(lista_da_50) < 51:
            lista_da_50.append(elem)
        elif len(lista_da_50) ==50:
            lista_gruppi.append(set(lista_da_50))
            lista_da_50 = []
        if lista_da_50:
            lista_gruppi.append(set(lista_da_50))    
            
    #per ogni gruppo si prende la prima tupla che compare e si scrive quel colore su tutti i pixel che hanno un colore
    #compreso nel gruppo della tupla presa        
    img_out = [riga[:] for riga in img]
    for gruppo in lista_gruppi:
        primo_colore = next(iter(gruppo))
        for x,riga in enumerate(img_out):
            for y,pixel in enumerate(riga):
                if pixel in gruppo:
                    img_out[x][y] = primo_colore
    #salva img_out              
    images.save(img_out,fimm1)
    
    colori_modificati = set(pixel for riga in img_out for pixel in riga)
    return len(colori_modificati)
            
                
    
es13("C:\\Users\\User\\Downloads\\Foto1.png","C:\\Users\\User\\Downloads\\RisFoto1.png")  
   
            
            
        
        
     

