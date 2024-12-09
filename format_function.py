# -*- coding: utf-8 -*-
"""
operatori format:
:<		allinea a sinistra (dentro lo spazio disponibile)
:>		allinea a destra(dentro lo spazio disponibile)
:^		allinea al centro (dentro lo spazio disponibile)
:=		Places the sign to the left most position
:+		usa un piu per indicare se ilrisultato è positivo o negativo
:-		usa il segno meno solo i numeri negativi
: 		usa uno spazio per inserire uno spazioe extra prima dei numeri positivi (e un segno meno per i numeri negativi)
:,		usa lo spazio come separatore dei decimali 
:_		usa l'underscore come separatore per le migliaia
:b		formato binario
:c		converte il carattere nel suo corrispettivo unicode
:d		formato decimale
:e		formato scientifico con la e minuscola
:E		formato scientifico con la Emasiuscola
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		formato generale (dei numeri)
:G		formato generale (usi la G maiuscola per la notazione scientifica)
:o		formato ottale
:x		formato esadecimale minuscolo
:X		formato esadecimale maiuscolo
:n		formattazione numero
:%		formattazione percentuale

"{:F},{:%}".format(var1,var2)
f"{var1:F},{var2:%}"
"""
#DATI TEST
voti_no = 233
voti_si = 232
tot_voti = voti_no +voti_si 
anno = "2021"
evento = "refendum"

#questo modo di farlo con f"" è molto meno laboriosa
stringa_finale = f"su un totale votanti di {tot_voti} con {voti_si:0} si. Si è arrivati al {voti_si /tot_voti:2.2%}"

#quando si usa format bisogna rispettare l'indicizazzione delle parentesi rispetto alle variabili (tipo in C, nelle prime parentesi andrà la prima var e cosi via)
stringa_format = "su un totale votanti di {:} con {:0} si. Si è arrivati al {:2.2%}".format(tot_voti,voti_si,voti_si /tot_voti)



"""
ESERCIZI:
    
    
Scrivi un programma che stampi i seguenti numeri in una tabella con larghezza di 10 caratteri:
Allineati a destra
Allineati a sinistra
Centrati
Numeri: 123, 45, 6789
"""
def PP_dx10(n):
    return f"{n:<10}"
PP_dx10(5)
def PP_sx10(n):
    return f"{n:>10}"
PP_sx10(10)
def PP_cc10(n):
    return f"{n:^10}"
PP_cc10(4356)
"""

Esercizio 2: Riempimento personalizzato
Usa il simbolo * come carattere di riempimento per formattare i seguenti numeri:
7 (larghezza 5, centrato)
34 (larghezza 6, allineato a destra)
"""
def PP_star(n):
    if(n==7):
        return f"{n:*^5}"
    elif(n==34):
        return f"{n:*<6}"
    else:
        return f"{n:*>10}"
PP_star(7)
PP_star(34)
PP_star(3)




"""
Esercizio 3: Formattazione di numeri decimali
Stampa il numero 123.456789 in questi formati:

Con 2 cifre decimali.
Con 4 cifre decimali.
Senza cifre decimali.


"""
def dec_format2(n):
    return f"{n:2.2%}"
def dec_format4(n):
    return f"{n:2d}"
def rmdec(n):
    return f"{n:f}"





"""
Esercizio 4: Uso dinamico della larghezza
Scrivi una funzione che accetta due parametri: un numero e una larghezza. Usa .format() per stampare il numero allineato a destra nella larghezza specificata.

formattazione(42, 6)  # Output: '    42'
"""
def agile_format(number,parameter):
    return "{:>{:}}".format(number, parameter)

"""
Esercizio 5: Numeri con zeri iniziali
Formatta i seguenti numeri in modo che abbiano sempre 5 cifre, aggiungendo zeri a sinistra:

3, 45, 789
"""
def add_zero(n):
    return "{:0>5}".format(n)

"""
Esercizio 6: Percentuali
Stampa il valore 0.75 come percentuale, mostrando:

0 decimali (75%)
2 decimali (75.00%)
"""
def PP_perc(n):
    return "{:.2%}".format(n)
def PP_perc_nodec(n):
    return "{:.%}".format(n)



"""
Esercizio 7: Formattazione di stringhe
Formatta le seguenti parole in una larghezza di 10 caratteri, con:

Allineamento a sinistra.
Allineamento a destra.
Allineamento centrato.
Parole: "Python", "Format", "Esempio"
"""
def PP_dx10W(stringa):
    return f"{stringa:<10}"
PP_dx10("Python")
def PP_sx10W(stringa):
    return f"{stringa:>10}"
PP_sx10("Format")
def PP_cc10W(stringa):
    return f"{stringa:^10}"
PP_cc10("Esempio")




"""
Esercizio 8: Numeri in base diversa
Stampa il numero 255 in:

Notazione decimale.
Notazione binaria.
Notazione esadecimale.
Notazione ottale.
"""
def PP_oct(n):
    return "{:o}".format(n)  
def PP_dec(n):
    return "{:d}".format(n)  
def PP_hex(n):
    return "{:x}".format(n)  
def PP_bin(n):
    return "{:b}".format(n)  
PP_bin(13)
PP_oct(13)
PP_dec(13)
PP_hex(13)
"""
Esercizio 9: Gestione di variabili dinamiche
Usa .format() per costruire una frase che prenda i valori da variabili. Variabili:

nome = "Luca"
età = 25
Frase: "Ciao, mi chiamo Luca e ho 25 anni." (usa le variabili dinamiche).

"""
def saluto(nome,eta):
    return f"Ciao, mi chiamo {nome} e ho {eta}anni."


"""
Esercizio 10: Formattazione complessa
Scrivi un programma che stampa una tabella formattata come segue:

Nome       Età  Salario
-----------------------
Mario      30   1500.50
Luisa      25   2100.75
Giovanni   35   3200.10
Usa .format() per garantire che le colonne siano ben allineate e i salari abbiano 2 cifre decimali.

"""
lista = [{"nome":"mario","età":30,"salario":3200.20},{"nome":"luisa","età":25,"salario":2100.20},{"nome":"Giovanni","età":35,"salario":3100.25}]
def crea_tabella(lista):
    tabella = "Nome      Età     Salario \n"
    tabella += "-------------------------\n"
    for persona in lista:
        nome = persona.get("nome")
        età = persona.get("età")
        salario = persona.get("salario")
        tabella += "{:10}{:<7}{:8.2f}\n".format(nome, età, salario)
    print(tabella)
    return tabella
