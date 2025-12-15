#nodo deve avere 2 figli e chiave pari
#restituire la somma dei nodi che hanno questa condizione

def es3(r):
    if r == None:
        return 0
    somma_dx = es3(r.left)
    somma_sx = es3(r.right)
    if r%2==0 and r.left !=None and r.right !=None:
        return 1 + somma_dx+somma_sx
    else:
        return somma_sx+somma_dx
    

