#es1
        #1) T(n)= 3T(n/4)+ θ(n^3) ✅
        #2) ∃ a >= 1 , b>1  ∃ f(n) asintoticamente positiva-> n^3 lo è ✅
        #   ∃ T(n) = aT(n/b)+ f(n)
        # a=3 ; b=4.  f(n)=n^3
        # casi
        # no   #caso 1) se n^3=O(n^log4(3)-e) con e>0 O(n^0.8). allora T(n)=θ(n^log_b(a))
        # no   #caso 2) f(n) = θ( n^log_b(a) ) 
        # si   #caso 3) E e>0, tc f(n)=Ω(n^lob_b(a)+e) af(n/b)<=cf(n)    n^log_b(a)=0.8
        #                  con  0 < c <1
        # 3(n^3/64)<=cn^3   si = 3/64<1
        # T(n)=θ(n^3)

#es2
# Sia dato un array A di n interi,
# se la terza cifra è dispari, i valori in A letti da sinistra a
# organizzato rispetto alla propria matricola come segue:
# se la terza cifra è pari o nulla, i valori in A letti da sinistra a destra sono dapprima crescenti e poi decrescenti;#destra sono dapprima decrescenti e poi crescenti.
# Le due sequenze, quella crescente e quella decrescente, che costituiscono A contengono sempre almeno due elementi ciascuna. 
# Non serve memorizzare la matricola, ma basta usare la terza cifra opportunamente per definire il proprio input.
# Progettare un algoritmo iterativo che restituisca il minimo ed il massimo di A in tempo O(log n).

# bisogna usare per forza una bin search coi puntatori

  
B=[ 10, 7, 6, 3, 5, 8, 9, 12]
def max_min(A):
    
    lo, hi = 0, len(A) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if A[mid] > A[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
  
    return ( A[lo],max( A[0],A[len(A)-1] ))

print(max_min(B))


# es3 Sia dato un albero T memorizzato
# tramite record e puntatori; ogni nodo contenga un campo val,
# che memorizza una delle 10 cifre decimali, ed i due puntatori
# left e right ai figli sinistro e destro.
# Si scriva un algoritmo ricorsivo che risponda True se esiste un
# cammino radice-foglia la somma delle cui chiavi sia pari alla
# somma delle cifre dalla propria matricola, False altrimenti. 
# Il costo computazionale deve essere O(n).

somma = sum([2,2,1,0,0,6,2]) # 13
def es3(r,somma, somma_cammino=0):
    if r == None:
        return False
    
    somma_cammino+=r.val
    if r.right is None and r.left is None:
        return somma == somma_cammino
    
    sinistro = es3(r.left,somma,somma_cammino)
    destro   = es3(r.right,somma,somma_cammino)

    return destro or sinistro


