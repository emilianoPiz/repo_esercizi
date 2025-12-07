def blur_5_conv(img):
    #copio l'immagine poichè questo algoritmo sfrutta i pixel già modificati in precedenza per i suoi calcoli
    output_img = img
    # per ogni pixel esso viene sostituito da una convoluzione di lui e dei suoi vicini,
    # questo risulterà in un pixel macchiato dai colori dei pixel vicini
    # creando un effetto di blurring su ogni pixel 
    for i in range(1, len(img)-1):
        for j in range(1, len(img[0])-1):
            if i+1 < len(img) and j+1 <len(img[0]):
              output_img[i][j]= round((img[i][j]+img[i+1][j]+img[i][j+1]+img[i][j-1]+img[i-1][j])/5)

    return output_img

img = [[12,15,4],[0,125,250],[145,12,11,],[124,255,255],
       [12,15,4],[0,125,250],[145,12,11,],[124,255,255]] #immagine in python a caso 
print(blur_5_conv(img))