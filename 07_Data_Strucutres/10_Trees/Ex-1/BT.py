class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)

    def inOrder(self, troot):
        if troot:
            self.inOrder(troot._left)
            print(troot._element, end=' ')
            self.inOrder(troot._right)

    def preOrder(self, troot):
        if troot:
            print(troot._element, end = ' ')
            self.preOrder(troot._left)
            self.preOrder(troot._right)

    def postOrder(self, troot):
        if troot:
            self.preOrder(troot._left)
            self.preOrder(troot._right)
            print(troot._element, end = ' ')

    def levelOrder(self):
        pass

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()

x.maketree(20 , a, a)
y.maketree(30,  a, a)
z.maketree(10, x, y)

print("In-order Traversal: ")
z.inOrder(z._root)

print("\nPre-order Traversal: ")
z.preOrder(z._root)

print("\nPost-order Traversal: ")
z.postOrder(z._root)

