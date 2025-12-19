#rimuovere ricorsivamente i nodi contenenti interi dispari 
# dalla lista concatenata.
def es3(r):
    if r.next == None and r.key %2==0:
        # la lista è finita e key è paro -> r va in lista
        return r 

    if r.next == None and r.key %2!=0:
        # la lista è finita e key è disparo, la lista finisce prima di lui 
        return None
    
    #sono nel nodo n-esimo, se nodo è pari allora si procede ad applicare la funzione sul suo prossimo
    # se sono in un nodo dispari, lo rimuovo.  
    if r.key%2==0:
         r.next = es3(r.next)
    else:
        r = es3(r.next)

    return r 


