#funzioni per naviagre l'heap (contando in 1 based)
def left(i):
    return 2 * (i + 1) - 1

def right(i):
    return left(i) + 1

def parent(i):
    return (i+1) // 2

def build_heap(A):
        for i in range (len(A)//2-1,-1,-1):
             heapify(A,i,len(A))
    

def heap_print(heap, i, heap_size, prefix="", child_prefix=""):
    #se l'indice scavalca la dimesione del vettore siamo fuori, perciò si esce
    if i >= heap_size:    return
    else:
        #se l'indice è vbero siamo al nodo radice
        if i == 0:
            print("({})\n".format(heap[i]))
        #altrimenti siamo in un nodo figlio di qualcun'altro    
        else:
            print("{}({})".format(prefix, heap[i]))

        has_left = left(i) < heap_size
        has_right = right(i) < heap_size

        if has_left or has_right:
            if has_left:
                heap_print(heap, left(i), heap_size, child_prefix + "├── ", child_prefix + "│   ")
            if has_right:
                heap_print(heap, right(i), heap_size, child_prefix + "└── ", child_prefix + "    ")

#prende un heap, un indice da controllare per vedere se rispetta la struttura di un heap, dimensione dell'heap
def heapify(heap, i, heap_size):
    #entro nell'heap e scelgo l'indice del figlio destro e sinistro
    sx = left(i)
    dx = right(i)
    #se l'indice del sinistro è inferiore alla dimensione dell'heap ET  il valore è strettamente maggiore del target da confrontare(i)
    if (sx < heap_size) and (heap[sx] > heap[i]):
        #allora l'indice massimo è il sinistro
        imax = sx
    else:
        #altrimenti l'indice massimo è il target da confrontare
        imax = i
    #se l'indice sinistro è inferiore alla dimensione dell'heap ET il valore è strettamente maggiore a destra del valore trovato precedentemente    
    if (dx < heap_size) and (heap[dx] > heap[imax]):
        #allora il destro diventa il massimo
        imax = dx
    #se il massimo è diverso dal target     
    if imax != i:
        #scambio il massimo trovato con il vecchio valore
        (heap[i], heap[imax]) = (heap[imax], heap[i])
        heapify(heap, imax, heap_size)


def heap_sort(A):
    n = len(A)
    build_heap(A)
    print(A)
    for heap_size in range(n-1, 0, -1):
        (A[0], A[heap_size]) = (A[heap_size], A[0])
        heapify(A, 0, heap_size)
          
A = [18, 2, 17, 12, 15, 10, 1, 8, 4, 14, 11, 3]


lgt = len(A)

print("--- Array visto come un albero ---")
heap_print(A, 0, lgt)
print("\n")
print(A)
heap_sort(A)

print("--- Array heapificato ---")
heap_print(A, 0, lgt)