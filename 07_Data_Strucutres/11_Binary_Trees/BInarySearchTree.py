class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if e == troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n



