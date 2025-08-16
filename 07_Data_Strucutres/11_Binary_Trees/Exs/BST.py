class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def search_iterative(self, key):
        # Understood now
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end='->')
            self.inorder(troot._right)



    def rsearch(self, troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.rsearch(troot._left, key)
            else:
                return self.rsearch(troot._right, key)
        return False


    def insert(self, troot, e):
        temp = None
        # determine where to insert the new node
        while troot:
            temp = troot
            if e == temp._element:
                return
            elif e < temp._element:
                troot = troot._left
            else:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n



    def rinsert(self, troot, e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left, e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right, e)
        else:
            n = _Node(e)
            troot = n
        return troot


B = BinarySearchTree()
# Iterative
B.insert(B._root, 50)
B.insert(B._root, 30)
B.insert(B._root, 80)
B.insert(B._root, 10)
B.insert(B._root, 40)
B.insert(B._root, 60)
B.inorder(B._root)



