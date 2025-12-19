# Si scriva lo pseudocodice, opportunamente commentato, 
# di una funzione iterativa che, preso in input un array A 
# di interi, trovi la lunghezza massima delle 
# sequenze crescenti presenti nell’array.
def es2(A):
    if not A:
        return "empty list given"
    if len(A)==1:
        return 1
    cont=0
    c=0
    for i in range(1,len(A)):
        if A[i]>A[i-1]:
            c+=1
        if c >= cont:
            cont = c

    return 1 if c==0 else cont 


a =[3, 1, 5, 2, 6, 8, 7, 1]
b=[]
c=[1]
print(es2(a))
print(es2(b))
print(es2(c))


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


