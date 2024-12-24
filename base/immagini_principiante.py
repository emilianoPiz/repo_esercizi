'''
ex1
Scrivi una funzione count_black_pixels(image) che prende in input un'immagine e restituisce il numero totale di pixel neri (0, 0, 0).
'''
import images
def count_black_pixels(path):
    img = images.load(path)
    counter=0
    for x, riga in enumerate(img):
        for y, pixel in enumerate(riga):
            if pixel == (0,0,0):
                counter+=1
    return counter

'''
Scrivi una funzione brightest_pixel(image) 
che restituisce le coordinate del pixel più luminoso (somma massima dei valori RGB). 
Se ci sono più pixel con la stessa luminosità, restituisci il primo trovato.
'''
def brightest_pixel(path):
    img = images.load(path)
    #sostituisco di volta in volta il pixel se quello trovato è più luminoso
    pixel_più_luminoso_corrente = (0,0,0)
    coordinate=[]
    for x, riga in enumerate(img):
        for y, pixel in enumerate(riga):
            if sum(pixel) > sum(pixel_più_luminoso_corrente):
                coordinate = (x,y)
                pixel_più_luminoso_corrente = [pixel]
    return coordinate

'''
Scrivi una funzione replace_color(image, old_color, new_color) 
che sostituisce tutti i pixel con il colore old_color con il colore new_color e 
restituisce l'immagine modifica
'''
def replace_color(image,old_color,new_color):
    img = images.load(image)
    for x,riga in enumerate(img):
        for y ,pixel in enumerate(riga):
            if pixel == old_color:
                img[x][y] = new_color
    return img

'''
Scrivi una funzione invert_colors(image) che inverte i colori di ogni pixel dell'immagine, trasformando il colore 
(𝑟,𝑔,𝑏)(r,g,b) in  (255−𝑟,255−𝑔,25−𝑏)
(255−r,255−g,255−b).
'''

def negative_img(image):
    img_invertita =[]
    riga_invertita = []
    img = images.load(image)
    for x, riga in enumerate(img):
            
        for y,(r,g,b) in enumerate(riga):
            riga_invertita.append((255-r,255-g,255-b))
            if len(riga_invertita) == len(img[0]):
               img_invertita.append(riga_invertita)
               riga_invertita = []
          
    return img_invertita

'''
Scrivi una funzione adjust_brightness(image, factor)
 che aumenta o diminuisce la luminosità dell'immagine 
 moltiplicando ogni componente RGB di ogni pixel per factor. 
 Assicurati di mantenere i valori RGB nell'intervallo 
[0,255].
'''

def adjust_brightness(image,factor):
    #caso semplice, vuole immagine nera
    img = images.load(image)
    if factor ==0 :
        black_img =[]
        for x,riga in enumerate(img):
            for y,(r,g,b) in enumerate(riga):
                black_img.append((0,0,0)) 
        return black_img
    #caso di luminosità alzata, numeri positivi
    if factor > 0:
        img_piu_lum =[]
        for x,riga in enumerate(img):
            for y,(r,g,b) in enumerate(riga):
                new_tuple=(r*factor,g*factor,b*factor)
                if r > 255:
                    r=255
                if g > 255:
                    g = 255
                if r > 255:
                   r = 255
                img_piu_lum.append(new_tuple)
        return img_piu_lum

'''
Scrivi una funzione add_white_border(image, thickness) che aggiunge 
un bordo bianco (255, 255, 255) 
di spessore thickness intorno all'immagine e restituisce l'immagine modificata.
'''
                
def white_border(image,thickness):
    img = images.load(image)
    width = len(img[0])
    height = len(img)
    for y, riga in enumerate(img):
        while y > thickness:
            for x,pixel in enumerate(img[y]):
                pixel = (255,255,255)
