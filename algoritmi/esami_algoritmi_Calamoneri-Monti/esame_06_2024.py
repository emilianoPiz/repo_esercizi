# si definisce punto di sella di una matrice quell'elemento tale che
# esso è il minimo della sua riga e il massimo della sua colonna
# data una matrice M, quadrata, reale, a valori distinti, ritornare l'indice
# del punto di sella, oppure None se nessun elemento è un punto di sella di M.
# massimo limite di tempo: Θ(n^2)

# soluzione: l'idea è che bisogna controllare per ogni minimo di riga
# se esso è anche un massimo di colonna, in quel caso torniamo l'indice
# se alla fine dell'iterazione ciò non avviene mai torniamo None. 

def sella(M):
    n = len(M)
    for i in range(n):
        #trovo il minimo di riga
        min_riga=0
        for x in range(n):
            if M[i][x] < M[i][min_riga]:
                min_riga=x
                
        #trovato il minimo di riga cerco nella sua colonna se esso è anche il maggiore
        sella=True 
        for y in range(n):
            if M[i][min_riga] < M[y][min_riga]:
                sella=False #basta ch un solo elemento sulla colonna sia inferiore al candidato per scartarlo
        if sella:
            return (i,min_riga)
   
    return None

A=[[1,10,8],[ 50, 600,70],[ 3,450,10]]

print(sella(A))

