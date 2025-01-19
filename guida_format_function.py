# *******************************************************************************************
# 🏆 GUIDA COMPLETA ALLE FUNZIONI DI FORMATTAZIONE IN PYTHON 🏆
# *******************************************************************************************
#
# In questa guida esploreremo nel dettaglio come utilizzare la formattazione dei valori in Python.
# Grazie alla sintassi "{:...}".format(valore) o alle f-string f"{valore:...}", è possibile
# controllare aspetti quali allineamento, gestione del segno, separatori per migliaia, basi diverse
# e molto altro.
#
# Indice dei contenuti:
#  1) Sintassi di base
#  2) Allineamento del testo
#  3) Gestione del segno (+, -, spazio)
#  4) Separatori di migliaia e decimali
#  5) Conversione in basi diverse (binario, ottale, esadecimale)
#  6) Formati numerici specifici (d, e, E, f, F, g, G, n, %)
#  7) Combinare più opzioni
#  8) Esempi pratici
#
# *******************************************************************************************
# 📌 1. SINTASSI DI BASE
# -------------------------------------------------------------------------------------------
# Esistono due modalità principali di formattazione in Python:
#
#   1) Il metodo .format() su stringa:
#       "{formato}".format(valore)
#
#   2) Le f-string (disponibili da Python 3.6 in poi):
#       f"{valore:formato}"
#
# Qualunque sia il metodo scelto, tra le parentesi graffe puoi inserire le specifiche che
# determinano come il valore verrà mostrato.

def esempio_sintassi_base():
    var1, var2 = 3.14159, 0.25
    print("Con .format():  {:F}, {:%}".format(var1, var2))
    print(f"Con f-string:   {var1:F}, {var2:%}")

# esempio_sintassi_base()

# *******************************************************************************************
# 📌 2. ALLINEAMENTO DEL TESTO
# -------------------------------------------------------------------------------------------
# Puoi controllare l'allineamento di una stringa (o un numero trattato come stringa)
# all’interno di uno spazio riservato. La larghezza si indica con un numero dopo i due punti.
#
#  - {:< }  = Allinea a sinistra
#  - {:> }  = Allinea a destra
#  - {:^ }  = Centra il contenuto
#  - {:= }  = Se è presente un segno, lo colloca in testa (utile per i numeri con segno)
#
# ESEMPIO:

def esempio_allineamento():
    valore = 42
    # Larghezza 10 caratteri, allineamento a sinistra
    print(f"Sinistra:  |{valore:<10}|")
    # Larghezza 10 caratteri, allineamento a destra
    print(f"Destra:    |{valore:>10}|")
    # Larghezza 10 caratteri, testo centrato
    print(f"Centro:    |{valore:^10}|")

    # Se vogliamo piazzare il segno all’estrema sinistra:
    negativo = -123
    print(f"Segno a sx (:=10): |{negativo:=10}|")

# esempio_allineamento()

# *******************************************************************************************
# 📌 3. GESTIONE DEL SEGNO (+, -, SPAZIO)
# -------------------------------------------------------------------------------------------
# Per i numeri, hai diverse modalità di mostrare i segni:
#
#  - {:+ }  = Mostra il + per i positivi e - per i negativi (es. +3, -2).
#  - {:- }  = Mostra il segno - solo per i negativi (default).
#  - {: }   = Aggiunge uno spazio in testa ai numeri positivi e il segno - per i negativi.
#
# ESEMPIO:

def esempio_segni():
    pos, neg = 123, -123
    print(f"Con +:  {pos:+}, {neg:+}")
    print(f"Con -:  {pos:-}, {neg:-}")  # di default, i positivi non mostrano il +
    print(f"Con spazio: {pos: }, {neg: }")

# esempio_segni()

# *******************************************************************************************
# 📌 4. SEPARATORI PER MIGLIAIA E DECIMALI
# -------------------------------------------------------------------------------------------
# Per rendere i numeri più leggibili, puoi usare:
#
#  - {:, }  = Usa la virgola (o il locale specifico) come separatore delle migliaia.
#  - {:_ }  = Usa l’underscore come separatore delle migliaia.
#
# ESEMPIO:

def esempio_separatori():
    grande_numero = 1234567890
    print(f"Separatore virgole:  {grande_numero:,}")
    print(f"Underscore:          {grande_numero:_}")

# esempio_separatori()

# *******************************************************************************************
# 📌 5. BASI DIVERSE: BINARIO, OTTALE, ESADECIMALE
# -------------------------------------------------------------------------------------------
# Se vuoi convertire un intero in varie basi:
#
#  - {:b }  = Binario
#  - {:o }  = Ottale
#  - {:x }  = Esadecimale minuscolo
#  - {:X }  = Esadecimale maiuscolo
#  - {:c }  = Carattere Unicode corrispondente (se l’intero rientra in un codice valido)
#
# ESEMPIO:

def esempio_basi():
    val = 255
    print(f"Binario (b):    {val:b}")
    print(f"Ottale (o):     {val:o}")
    print(f"Esadec. (x):    {val:x}")
    print(f"Esadec. (X):    {val:X}")

    # Esempio per il carattere unicode: 65 corrisponde a 'A'
    val_char = 65
    print(f"Carattere (c):  {val_char:c}")

# esempio_basi()

# *******************************************************************************************
# 📌 6. FORMATI NUMERICI SPECIFICI
# -------------------------------------------------------------------------------------------
# I principali formati numerici per float e int sono:
#
#  - {:d }  = Decimal (solo per interi)
#  - {:e }  = Notazione scientifica (es. 1.23e+03) con 'e' minuscola
#  - {:E }  = Notazione scientifica con 'E' maiuscola
#  - {:f }  = Formato "virgola fissa" (fisso) (es. 123.456)
#  - {:F }  = Come f, ma mostra 'INF' e 'NAN' in maiuscolo
#  - {:g }  = Formato generale (decide tra notazione fissa o scientifica)
#  - {:G }  = Come g, ma con 'E' maiuscola in notazione scientifica
#  - {:n }  = Numero formattato secondo il locale (se configurato)
#  - {:% }  = Percentuale (moltiplica per 100 e aggiunge '%')
#
# ESEMPIO:

def esempio_formati_numerici():
    val_float = 1234.56789
    val_int = 255
    percent = 0.125

    # d = formato intero (val_int deve essere un integer)
    print(f"Intero decimale (d): {val_int:d}")

    # e/E = notazione scientifica
    print(f"Scientifico (e):     {val_float:e}")
    print(f"Scientifico (E):     {val_float:E}")

    # f/F = fix point
    print(f"Fix point (f):       {val_float:f}")
    print(f"Fix point (F):       {val_float:F}")  # INF e NAN in maiuscolo

    # g/G = formato generale
    print(f"Generale (g):        {val_float:g}")
    print(f"Generale (G):        {val_float:G}")

    # n = numero formattato secondo locale
    print(f"Locale (n):          {val_float:n}")

    # % = percentuale
    print(f"Percentuale (%):     {percent:%}")

# esempio_formati_numerici()

# *******************************************************************************************
# 📌 7. COMBINARE PIÙ OPZIONI
# -------------------------------------------------------------------------------------------
# È possibile concatenare diverse opzioni all’interno delle parentesi graffe.
# Ad esempio, puoi definire la larghezza, l’allineamento, il segno e il tipo di formato:
#
# { [allineamento] [larghezza] [separatore_migliaia] [gestione_segno] [formato_numero] }
#
# Ecco un esempio complesso che combina più specifiche contemporaneamente:
#
#   "{:>+10,.2f}".format(1234.5678)
#
#  - >     = allineamento a destra
#  - +     = mostrare il segno anche per i positivi
#  - 10    = larghezza totale di 10 caratteri
#  - ,     = separatore delle migliaia
#  - .2f   = 2 cifre decimali, formato virgola fissa
#
# Prova tu stesso a variare questi parametri!

def esempio_combinato():
    numero = 1234.5678
    # Esempio combinato
    print(f"Formattazione combinata: {numero:>+10,.2f}")

# esempio_combinato()

# *******************************************************************************************
# 📌 8. ESEMPI PRATICI
# -------------------------------------------------------------------------------------------
# 1) Stampa di una lista di numeri in colonne allineate:
#    In questo esempio, ogni numero viene formattato in modo da avere 8 caratteri di spazio,
#    allineato a destra, con 2 decimali.

def esempio_lista_numeri():
    numeri = [3.1, 245.6789, -12.34, 0.005, 123456.789]
    for n in numeri:
        print(f"|{n:>8.2f}|")

# esempio_lista_numeri()

# 2) Utilizzo delle f-string per stampare informazioni su prodotti o valori con formattazioni varie.
def esempio_tabella():
    prodotti = [
        ("Mela", 1.99),
        ("Banana", 0.75),
        ("Ananas", 2.40)
    ]
    print("Prodotto   | Prezzo ")
    print("--------------------")
    for nome, prezzo in prodotti:
        # Allineiamo il nome a sinistra in 10 caratteri, e il prezzo in 7 con 2 decimali
        print(f"{nome:<10} | {prezzo:>7.2f}")

# esempio_tabella()

# *******************************************************************************************
# 🚀 CON QUESTI STRUMENTI, PUOI FORMATTERE QUASI OGNI TIPO DI DATO IN MODO ACCURATO E LEGGIBILE!
# *******************************************************************************************
