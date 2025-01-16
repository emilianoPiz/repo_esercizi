# *******************************************************************************************
# 🌄 GUIDA COMPLETA PER RISOLVERE PROBLEMI SULLE MATRICI (LISTE DI LISTE) IN PYTHON 🌄
# *******************************************************************************************

# In questa guida, tratteremo in modo approfondito come lavorare con le matrici
# rappresentate come liste di liste in Python. Ci ispireremo alla struttura della
# guida sugli alberi binari, ma adattandola ai concetti delle matrici e arricchendola
# con esempi ed esercizi pratici.

# 📌 1. COMPRENDERE LA STRUTTURA DI UNA MATRICE (LISTA DI LISTE)
# -------------------------------------------------------------------------------------------
# In Python, una matrice può essere rappresentata come una lista di liste. 
# Ogni “riga” della matrice è una lista, e l'insieme di queste liste costituirà la nostra matrice.
#
# Esempio di matrice 2x3:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
#
# - Numero di righe: 2
# - Numero di colonne: 3
#
# Generalmente, useremo la notazione matrix[r][c] per accedere all'elemento in riga r e colonna c.

# Creiamo qualche esempio di base per familiarizzare con la struttura:

# Esempio 1: Matrice vuota
matrix_empty = []

# Esempio 2: Matrice 2x2 con valori statici
matrix_2x2 = [
    [1, 2],
    [3, 4]
]

# Esempio 3: Matrice 3x3 con valori predefiniti
matrix_3x3 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Esempio 4: Matrice di stringhe 2x3
matrix_strings = [
    ["a", "b", "c"],
    ["d", "e", "f"]
]

# 📌 2. TIPI DI PROBLEMI COMUNI
# -------------------------------------------------------------------------------------------
# Nelle matrici (liste di liste) possiamo incontrare numerose tipologie di problemi. Ecco i più comuni:

# 🔄 a. Traversamenti (visite)
#    - Visita per riga (row-wise)
#    - Visita per colonna (column-wise)
#    - Visita a spirale (spiral traversal)
#    - Visite diagonali (main diagonal, secondary diagonal)
#    - Visite BFS/DFS in caso di interpretazione della matrice come grafo (per esempio in grid problems)

# 🔢 b. Operazioni specifiche
#    - Calcolo di somme (es. somma di tutti gli elementi, somma di una riga, somma di una colonna)
#    - Rotazione della matrice (90°, 180°, 270°)
#    - Trasposizione di una matrice
#    - Ricerca di un elemento
#    - Trovare il minimo/massimo
#    - "Flatten" di una matrice (trasformarla in una lista monodimensionale)
#    - Riconoscere pattern speciali (es. matrice identità, matrice diagonale, triangolare, ecc.)

# 📌 3. STRATEGIE GENERALI
# -------------------------------------------------------------------------------------------
# 🛠 a. Approccio iterativo
# Per manipolare o analizzare una matrice, utilizziamo spesso cicli annidati (doppi for).
# Questi cicli ci permettono di scorrere tutti gli elementi riga per riga o colonna per colonna.

# Template generico di visita con doppio for:
# for r in range(num_rows):
#     for c in range(num_cols):
#         # Elabora matrix[r][c]

# 🌀 b. Approccio ricorsivo
# È meno comune l'utilizzo della ricorsione sulle matrici rispetto agli alberi, 
# ma può capitare, ad esempio, per realizzare DFS (Depth-First Search) su una griglia 
# interpretata come grafo (es. in problemi di pathfinding).

# 📌 4. ESEMPI DI PROBLEMI E SOLUZIONI
# -------------------------------------------------------------------------------------------
# In questa sezione, proponiamo diversi esempi di funzioni utili per lavorare con le matrici.

# *******************************************************************************************
# 4.1 TRAVERSAMENTI
# *******************************************************************************************

# Esempio 1: Stampa di una matrice riga per riga
def print_matrix_row_wise(matrix):
    if not matrix:
        return
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()  # nuova linea dopo ogni riga

# Esempio 2: Stampa di una matrice colonna per colonna
def print_matrix_column_wise(matrix):
    if not matrix:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    for c in range(cols):
        for r in range(rows):
            print(matrix[r][c], end=" ")
        print()

# Esempio 3: Traversamento a spirale (spiral traversal)
def spiral_traversal(matrix):
    if not matrix:
        return []
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while left <= right and top <= bottom:
        # da sinistra a destra (riga top)
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # dall'alto verso il basso (colonna right)
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            # da destra a sinistra (riga bottom)
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            # dal basso verso l'alto (colonna left)
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result

# Esempio 4: Traversamento diagonale principale
def main_diagonal(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    diag = []
    for i in range(min(rows, cols)):
        diag.append(matrix[i][i])
    return diag

# *******************************************************************************************
# 4.2 OPERAZIONI DI BASE
# *******************************************************************************************

# Esempio 1: Somma di tutti gli elementi della matrice
def sum_all_elements(matrix):
    total = 0
    for row in matrix:
        for elem in row:
            total += elem
    return total

# Esempio 2: Calcolo della somma di una riga data (row_index)
def sum_of_row(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        return 0
    return sum(matrix[row_index])

# Esempio 3: Calcolo della somma di una colonna data (col_index)
def sum_of_column(matrix, col_index):
    if not matrix:
        return 0
    if col_index < 0 or col_index >= len(matrix[0]):
        return 0
    total = 0
    for r in range(len(matrix)):
        total += matrix[r][col_index]
    return total

# Esempio 4: Trovare l'elemento massimo e minimo in una matrice
def find_min_and_max(matrix):
    if not matrix or not matrix[0]:
        return None, None
    min_val = matrix[0][0]
    max_val = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min_val:
                min_val = elem
            if elem > max_val:
                max_val = elem
    return min_val, max_val

# *******************************************************************************************
# 4.3 TRASFORMAZIONI COMUNI
# *******************************************************************************************

# Esempio 1: Trasposizione di una matrice (righe diventano colonne e viceversa)
def transpose(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

# Esempio 2: Rotazione di una matrice di 90 gradi in senso orario
def rotate_90(matrix):
    # Una rotazione di 90° in senso orario equivale a:
    # 1) Trasporre la matrice
    # 2) Invertire ogni riga
    t = transpose(matrix)
    for row in t:
        row.reverse()
    return t

# Esempio 3: "Flatten" di una matrice in una sola lista
def flatten_matrix(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list

# Esempio 4: Creare una matrice identità di dimensione n
def identity_matrix(n):
    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(1 if r == c else 0)
        matrix.append(row)
    return matrix

# *******************************************************************************************
# 4.4 RICERCA E PERCORSI
# *******************************************************************************************

# Esempio 1: Ricerca lineare di un valore all'interno della matrice
def contains_value(matrix, target):
    for row in matrix:
        for elem in row:
            if elem == target:
                return True
    return False

# Esempio 2: DFS su una matrice interpretata come grafo (per esempio, per problemi di island counting)
# Nota: si assume che '1' rappresenti un'area da visitare e '0' no. 
def dfs_matrix(matrix, r, c, visited):
    rows = len(matrix)
    cols = len(matrix[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if matrix[r][c] == 0:
        return
    if (r, c) in visited:
        return
    visited.add((r, c))
    # Esplora i vicini (su, giù, sinistra, destra)
    dfs_matrix(matrix, r - 1, c, visited)
    dfs_matrix(matrix, r + 1, c, visited)
    dfs_matrix(matrix, r, c - 1, visited)
    dfs_matrix(matrix, r, c + 1, visited)

# *******************************************************************************************
# 4.5 STRUMENTI E CONSIGLI
# *******************************************************************************************
# 🎨 Disegna la matrice su carta o in console, specialmente se devi gestire traversal complicati
# 🐛 Usa `print` o debugger per vedere l’evoluzione degli indici durante i loop
# 🧪 Testa il codice con:
#     - Matrici vuote
#     - Matrici con una sola riga
#     - Matrici con una sola colonna
#     - Matrici quadrate e rettangolari

# Esempio di funzione di stampa formattata della matrice
def print_formatted_matrix(matrix):
    if not matrix:
        print("Matrice vuota!")
        return
    for row in matrix:
        print("|", end=" ")
        for elem in row:
            print(f"{elem:3}", end=" ")  # :3 per allineare gli elementi
        print("|")

# *******************************************************************************************
# 5. ESERCIZI PRATICI
# *******************************************************************************************
# 💡 Esercizio 1: Creare una matrice di dimensioni n x m riempita con zeri
# 💡 Esercizio 2: Sommare i valori di due matrici della stessa dimensione
# 💡 Esercizio 3: Verificare se una matrice è simmetrica rispetto alla diagonale principale
# 💡 Esercizio 4: Trovare tutte le posizioni di un valore target nella matrice
# 💡 Esercizio 5: Ruotare la matrice di 180 gradi
# 💡 Esercizio 6: Realizzare la visita "a serpente": la prima riga da sinistra a destra, la seconda da destra a sinistra, ecc.

# Esempio di soluzioni per alcuni esercizi:

# 💡 Esercizio 1: Creare una matrice di dimensioni n x m riempita con zeri
def create_zero_matrix(n, m):
    # Crea una matrice n x m di zeri
    return [[0 for _ in range(m)] for _ in range(n)]

# 💡 Esercizio 2: Sommare i valori di due matrici della stessa dimensione
def add_matrices(a, b):
    if not a or not b:
        return []
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if rows_a != rows_b or cols_a != cols_b:
        return []  # Dimensioni non compatibili
    
    result = create_zero_matrix(rows_a, cols_a)
    for r in range(rows_a):
        for c in range(cols_a):
            result[r][c] = a[r][c] + b[r][c]
    return result

# 💡 Esercizio 3: Verificare se una matrice è simmetrica (rispetto alla diagonale principale)
def is_symmetric(matrix):
    if not matrix:
        return True
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False  # Non può essere simmetrica se non è quadrata
    for r in range(rows):
        for c in range(r+1, cols):
            if matrix[r][c] != matrix[c][r]:
                return False
    return True

# 💡 Esercizio 4: Trovare tutte le posizioni di un valore target nella matrice
def find_all_positions(matrix, target):
    positions = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target:
                positions.append((r, c))
    return positions

# 💡 Esercizio 5: Ruotare la matrice di 180 gradi
def rotate_180(matrix):
    # Ruotare di 180° equivale a invertire righe e colonne
    # Possiamo ottenere il risultato invertendo l’ordine delle righe
    # e poi invertendo l’ordine di ogni riga
    rotated = matrix[::-1]  # inverte l'ordine delle righe
    rotated = [row[::-1] for row in rotated]  # inverte l’ordine in ogni riga
    return rotated

# 💡 Esercizio 6: Realizzare la visita a serpente
def snake_traversal(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    result = []
    for r in range(rows):
        if r % 2 == 0:
            # Riga pari: da sinistra a destra
            result.extend(matrix[r])
        else:
            # Riga dispari: da destra a sinistra
            result.extend(matrix[r][::-1])
    return result

# *******************************************************************************************
# 🌟 CON QUESTA GUIDA, SEI PRONTO PER AFFRONTARE QUALSIASI PROBLEMA SULLE MATRICI (LISTE DI LISTE)! 🌟
# *******************************************************************************************

# Risorse Aggiuntive
# -------------------------------------------------------------------------------------------
# - Documentazione Ufficiale Python: https://docs.python.org/3/tutorial/datastructures.html
# - Esercizi su Matrici e Liste: https://www.geeksforgeeks.org/python-list/
# - Argomenti Avanzati: Algoritmi di Pathfinding (DFS, BFS) applicati a griglie

# Consigli Finali
# -------------------------------------------------------------------------------------------
# - Esercitati con diverse dimensioni e tipologie di matrici (vuote, quadrate, rettangolari).
# - Familiarizza con i doppi for, essenziali per la maggior parte delle operazioni sulle matrici.
# - Impara a riconoscere i pattern (trasposta, diagonali, rotazioni) per velocizzare la risoluzione dei problemi.
# - Non sottovalutare casi limite (matrice vuota, righe di diversa lunghezza, ecc.).
# - Buono studio e buona programmazione!
