# Dato un array A di n interi non negativi distinti, 
# si vuole determinare se esistono almeno tre numeri consecutivi di valore inferiore a 100.
# Ad esempio,
# # se A = [101, 5, 9, 31, 33, 10, 100, 4, 8, 32, 500, 11, 99], 
# gli elementi 8, 9 e 10 così come gli elementi 31, 32 e 33 rispettano la proprietà mentre 99,
# 100 e 101 no.
# Progettare un algoritmo che, dato A, in tempo Θ(n) restituisce il valore 
# dell’elemento centrale della terna se questa è presente, −1 altrimenti. 
# Se esistono pi`u terne allora bisogna restituire l’elemento centrale di valore massimo 
# (nell’esempio sopra, l’algoritmo dovrebbe restituire 32; se nell’array ci fossero 4 numeri consecutivi andrebbe restituito il terzo, ad esempio se l’array contenesse soltanto 5, 6,
# 7 e 8, andrebbe restituito il 7).
# Dell’algoritmo proposto:
# a) si scriva lo pseudocodice opportunamente commentato;
# b) si giustifichi il costo computazionale.

def triple_inferiori_100(A):
    consecutivi = [0]*100

    for i in range(0,len(A)):
        if A[i]<100:
            consecutivi[A[i]] = A[i]
    
    centrale = 0 
    for i in range (1,99):
        if consecutivi[i]>0 and consecutivi[i-1]>0 and consecutivi[i+1]>0 :
            centrale = consecutivi[i]

    return centrale if centrale >0 else -1

A = [46, 101, 5, 9,45, 31, 33, 10, 100, 4, 8, 32, 47,32, 500, 11, 99]

print(triple_inferiori_100(A))

