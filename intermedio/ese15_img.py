''' 
ese15   
    Es 3: 6 punti
    Si definisca la  funzione es3(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
      La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
      Per quanto riguarda i colori dei pixel della nuova immagine:
      il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
      le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore 
      del pixel dell'unica immagine originaria in cui e' presente.
      (guardate le immagini di test per chiarimenti)
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    
    -out su fimmm3 larga come max(larghezze) e alta come max(altezze)
    pixel = (0,0,0) se è in entrambe fimm1 e fimm2 o in nessuna (in nessuna equivale a dire che ha recuperato i pixel che gli mancavano in altezza o larghezza)
    in caso contrario il colore sarà dato dall'unica immagine che lo occupa'
'''
import images
def es15(fimm1,fimm2,fimm3):
    #inizio
    #estrapolo le variabili che mi servono alla risoluzione
    img     = images.load(fimm1)
    img2    = images.load(fimm2)
    h1      = len(img)
    w1      = len(img[0])
    h2      = len(img2)
    w2      = len(img2[0])
    nero    = (0,0,0)
    counter = 0 
    
    #creo un immagine nera con le dimensioni massime in h e w 
    new_img = [[nero for _ in range(max(w1,w2))] for _ in range(max(h1,h2))]
  
    #riempio gli spazi appartenti ad una sola immagine
    for y in range(max(h1,h2)):
        for x in range(max(w1,w2)):
            if y < h1 and x < w1:
                new_img[y][x] = img[y][x]
            elif y < h2 and x < w2:
                new_img[y][x] = img2[y][x]
            else:
                new_img[y][x] = nero
                counter += 1
    
    images.save(new_img, fimm3)
    return counter