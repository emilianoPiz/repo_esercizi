class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Figlio sinistro
        self.right = None  # Figlio destro


def es3(r):
    if r is None:
        return False
    if r.left is None and r.right is None:
        return True

    path_sx = False
    path_dx = False

    if r.left is not None and r.left.value == r.value:
        path_sx = es3(r.left)

    if r.right is not None and r.right.value == r.value:
        path_dx = es3(r.right)

    return path_sx or path_dx


