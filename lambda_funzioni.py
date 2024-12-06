# -*- coding: utf-8 -*-
"""
LAMBDA FUNZIONE 
"""
"""
DICHIARAZIONE FUNZIONI
"""
#dati fittizi per non ricevere errori
DATA = []

#aritmetiche e funzioni elementari
Q     = lambda x : x**2
C     = lambda x : x**3
SQR   = lambda x : x**(1/2) 
H     = lambda x : x/2


#NUOVA_LISTA_ORDINATA_CON_LAMBDA     = sorted(arry_t, key=SRT)
SRT   = lambda x : x[1]

#FILTRA TUTTI I pari                 = filter(DATA, EVN)
EVN   = lambda x : x % 2 == 0

#FILTRA TUTTI I dispari              = filter(DATA, ODD)
ODD   = lambda x : x % 2 == 1

#AGGIUNGI 5 A OGNI ELEMENTO          = map(ADD_5,DATA)
ADD_5 = lambda x : x+5

#in base alla lunghezza
#ORDINATA_CON_LEN_S                  = sorted(DATA, key=LEN_S)
LEN_S = lambda x : len(x) 

#ORDINA IN BASE A UN PARAMETRO CONOSCIUTO
#LISTA_SRT_P                         = sorted(DATA,key=SRT_P)
SRT_P = lambda x : x["price"]

#COMBINAZIONE DI METODO MAP E FILTER
#FAI IL QUADRATO    DEI SOLI  PARI    DI OGNUNOG DI ESSI
#          map(Q,   filter(   EVN,    DATA))
map(Q,filter(EVN,DATA))

#LAMBDA CON ARGOMENTO DI DEFAULT
TWO_S = lambda x , y=10 : x +y


LST_S = lambda x: int(''.join(filter(str.isdigit, x)))

