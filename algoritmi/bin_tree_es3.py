def sx(i):     return (i+1)*2
def dx(i):     return sx(i)+1
def parent(i): return (i+1)//2


def es3(root):
    if root == None:
        return 0
    c = 0 
    if root.key%2 == 0 and root.left is not None and root.right is not None:
        c = 1

    c +=es3(root.left)
    c +=es3(root.right)
    return c
