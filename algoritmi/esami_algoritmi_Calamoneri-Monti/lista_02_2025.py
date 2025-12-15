def somma_mul_lista(M,r):
    if r == None:
        return 0
    somma = somma_mul_lista(M,r.next)
    if r.key %M ==0:
        somma += r.key
    return somma

