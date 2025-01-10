# *******************************************************************************************
# 🌳 GUIDA COMPLETA PER RISOLVERE PROBLEMI SUGLI ALBERI BINARI IN PYTHON 🌳
# *******************************************************************************************
    
# 📌 1. COMPRENDERE LA STRUTTURA DI UN ALBERO BINARIO
# -------------------------------------------------------------------------------------------
# Un albero binario è composto da nodi. Ogni nodo ha:
# - Un valore (ad es., un numero, una stringa, ecc.)
# - Un figlio sinistro (left) e un figlio destro (right), che possono essere None.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Figlio sinistro
        self.right = None  # Figlio destro

# Esempio 1: Costruzione di un albero binario semplice
# ```
#         'A'
#        /   \
#      'B'   'C'
# ```
root = Node('A')
root.left = Node('B')
root.right = Node('C')

# Esempio 2: Costruzione di un albero binario più complesso
# ```
#         10
#        /  \
#       5    15
#      / \     \
#     3   7     18
# ```
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

# Esempio 3: Albero binario con valori misti
# ```
#         "root"
#        /       \
#     "left"    "right"
#      /            \
#  "left.left"    "right.right"
# ```
root = Node("root")
root.left = Node("left")
root.right = Node("right")
root.left.left = Node("left.left")
root.right.right = Node("right.right")

# Esempio 4: Albero binario completo
# ```
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
# ```
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# 📌 2. TIPI DI PROBLEMI COMUNI
# -------------------------------------------------------------------------------------------
# 🔄 a. Traversamenti (visite)
#    - Preorder (Radice, Sinistra, Destra)
#    - Inorder (Sinistra, Radice, Destra)
#    - Postorder (Sinistra, Destra, Radice)
#    - Livello (Breadth-First Search)

## Esempio 1: Traversamento in Inorder
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)  # Visita il figlio sinistro
        print(node.value)             # Visita la radice
        inorder_traversal(node.right) # Visita il figlio destro

## Esempio 2: Traversamento in Livello (Breadth-First Search) senza librerie esterne
def level_order_traversal(root):
    if not root:
        return
    queue = [root]  # Utilizza una lista come coda
    while queue:
        current = queue.pop(0)  # Dequeue
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

## Esempio 3: Traversamento in Postorder
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)  # Visita il figlio sinistro
        postorder_traversal(node.right) # Visita il figlio destro
        print(node.value)               # Visita la radice

## Esempio 4: Traversamento in Preorder Iterativo senza librerie esterne
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

# 🔢 b. Operazioni specifiche
#    - Calcolare altezza/profondità dell'albero
#    - Contare nodi/foglie o nodi con proprietà specifiche

## Esempio 1: Contare il numero totale di nodi nell'albero
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

## Esempio 2: Contare il numero di foglie nell'albero
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

## Esempio 3: Calcolare l'altezza di un albero
def tree_height(node):
    if not node:
        return 0
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return 1 + max(left_height, right_height)

## Esempio 4: Contare i nodi con un solo figlio
def count_single_child_nodes(node):
    if not node:
        return 0
    count = 0
    if (node.left and not node.right) or (node.right and not node.left):
        count = 1
    return count + count_single_child_nodes(node.left) + count_single_child_nodes(node.right)

# 📌 3. STRATEGIE GENERALI
# -------------------------------------------------------------------------------------------
# 🛠 a. Approccio ricorsivo
# La ricorsione è la chiave per molti problemi sugli alberi. La struttura ricorsiva è naturale.

## Template generico:
def solve_tree_problem(node):
    if not node:
        return base_case  # Passo base
    left_result = solve_tree_problem(node.left)   # Ricorsione sul figlio sinistro
    right_result = solve_tree_problem(node.right) # Ricorsione sul figlio destro
    return combine_results(node, left_result, right_result)  # Combina i risultati

## Esempio 1: Sommare i valori di tutti i nodi
def sum_of_nodes(node):
    if not node:
        return 0
    return node.value + sum_of_nodes(node.left) + sum_of_nodes(node.right)

## Esempio 2: Verificare se l'albero contiene un valore specifico
def contains_value(node, target):
    if not node:
        return False
    if node.value == target:
        return True
    return contains_value(node.left, target) or contains_value(node.right, target)

## Esempio 3: Trovare il valore massimo nell'albero
def find_max(node):
    if not node:
        return float('-inf')
    return max(node.value, find_max(node.left), find_max(node.right))

## Esempio 4: Verificare se due alberi sono identici
def are_identical(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2:
        return (node1.value == node2.value and
                are_identical(node1.left, node2.left) and
                are_identical(node1.right, node2.right))
    return False

# 🌀 b. Approccio iterativo
# Usa una pila o una coda per simulare la ricorsione quando necessario.

## Esempio 1: Traversamento iterativo in Preorder
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

## Esempio 2: Traversamento iterativo in Postorder senza stack secondario
def postorder_iterative(root):
    if not root:
        return
    stack = []
    last_node_visited = None
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_node_visited != peek_node.right:
                current = peek_node.right
            else:
                print(peek_node.value)
                last_node_visited = stack.pop()

## Esempio 3: Traversamento iterativo in Inorder
def inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value)
        current = current.right

## Esempio 4: Calcolare la profondità massima iterativamente
def iterative_tree_height(root):
    if not root:
        return 0
    stack = [(root, 1)]
    max_height = 0
    while stack:
        current, height = stack.pop()
        max_height = max(max_height, height)
        if current.left:
            stack.append((current.left, height + 1))
        if current.right:
            stack.append((current.right, height + 1))
    return max_height

# 📌 4. STRUMENTI E CONSIGLI
# -------------------------------------------------------------------------------------------
# 🎨 Disegna l'albero: visualizza la struttura per capire meglio il problema.
# 🐛 Debugging: usa `print` o strumenti di debug per seguire il flusso di esecuzione.
# 🧪 Testa il codice con alberi di varie forme:
#     - Alberi vuoti
#     - Alberi con un solo nodo
#     - Alberi bilanciati e non bilanciati

## Strumento 1: Funzione per disegnare l'albero (visualizzazione semplice)
def print_tree(node, level=0, label="."):
    if node is not None:
        print(" " * (level*4) + label + ": " + str(node.value))
        print_tree(node.left, level+1, "L")
        print_tree(node.right, level+1, "R")

## Strumento 2: Verifica dell'equilibrio dell'albero
def is_balanced(node):
    def check(node):
        if not node:
            return 0, True
        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)
        current_height = 1 + max(left_height, right_height)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return current_height, balanced
    _, balanced = check(node)
    return balanced

## Strumento 3: Funzione per cercare il percorso da root a un nodo specifico
def find_path(node, target, path=None):
    if path is None:
        path = []
    if not node:
        return False
    path.append(node.value)
    if node.value == target:
        return True
    if find_path(node.left, target, path) or find_path(node.right, target, path):
        return True
    path.pop()
    return False

## Strumento 4: Funzione per clonare un albero
def clone_tree(node):
    if not node:
        return None
    new_node = Node(node.value)
    new_node.left = clone_tree(node.left)
    new_node.right = clone_tree(node.right)
    return new_node

# 📌 5. ESERCIZI PRATICI
# -------------------------------------------------------------------------------------------
# 💡 Esercizio 1: Contare le foglie in un albero
# 💡 Esercizio 2: Verificare se un albero è simmetrico
# 💡 Esercizio 3: Sommare i valori di tutti i nodi
# 💡 Esercizio 4: Trovare il nodo più profondo
# 💡 Esercizio 5: Convertire un albero in una lista ordinata (inorder)

# 💡 Esercizio 1: Contare le foglie in un albero
## Soluzione:
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# 💡 Esercizio 2: Verificare se un albero è simmetrico
## Soluzione:
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.value == right.value) and \
               is_mirror(left.left, right.right) and \
               is_mirror(left.right, right.left)
    if not root:
        return True
    return is_mirror(root.left, root.right)

# 💡 Esercizio 3: Sommare i valori di tutti i nodi
## Soluzione:
def sum_of_nodes(node):
    if not node:
        return 0
    return node.value + sum_of_nodes(node.left) + sum_of_nodes(node.right)

# 💡 Esercizio 4: Trovare il nodo più profondo
## Soluzione:
def find_deepest_node(root):
    if not root:
        return None
    queue = [root]  # Utilizza una lista come coda
    deepest = None
    while queue:
        deepest = queue.pop(0)  # Dequeue
        if deepest.left:
            queue.append(deepest.left)
        if deepest.right:
            queue.append(deepest.right)
    return deepest

# 💡 Esercizio 5: Convertire un albero in una lista ordinata (inorder)
## Soluzione:
def inorder_to_list(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_to_list(node.left, result)
        result.append(node.value)
        inorder_to_list(node.right, result)
    return result

# 💡 Esercizio 6: Verificare se due alberi sono identici
## Soluzione:
def are_identical(node1, node2):
    if not node1 and not node2:
        return True
    if node1 and node2:
        return (node1.value == node2.value and
                are_identical(node1.left, node2.left) and
                are_identical(node1.right, node2.right))
    return False

# 💡 Esercizio 7: Trovare il valore massimo nell'albero
## Soluzione:
def find_max(node):
    if not node:
        return float('-inf')
    return max(node.value, find_max(node.left), find_max(node.right))

# 💡 Esercizio 8: Trovare la distanza tra due nodi
## Soluzione:
def find_lca(root, n1, n2):
    if not root:
        return None
    if root.value == n1 or root.value == n2:
        return root
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca

def find_level(root, target, level=0):
    if not root:
        return -1
    if root.value == target:
        return level
    left = find_level(root.left, target, level + 1)
    if left != -1:
        return left
    return find_level(root.right, target, level + 1)

def find_distance(root, n1, n2):
    lca = find_lca(root, n1, n2)
    if not lca:
        return -1
    d1 = find_level(lca, n1, 0)
    d2 = find_level(lca, n2, 0)
    return d1 + d2

# *******************************************************************************************
# 🌟 CON QUESTA GUIDA, SEI PRONTO PER AFFRONTARE QUALSIASI PROBLEMA SUGLI ALBERI BINARI! 🌟
# *******************************************************************************************

# Risorse Aggiuntive
# -------------------------------------------------------------------------------------------
# - [LeetCode - Binary Tree Problems](https://leetcode.com/problemset/all/?topicSlugs=binary-tree)
# - [GeeksforGeeks - Binary Tree](https://www.geeksforgeeks.org/binary-tree-data-structure/)
# - [Visualizzazione degli Alberi con Graphviz](https://graphviz.org/)

# Buono studio e buona programmazione!
