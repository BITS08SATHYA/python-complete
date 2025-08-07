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

    def inOrder(self, root):
        if root:
            self.inOrder(root._left)
            print(root._element, end = '')
            self.inOrder(root._right)

    def preOrder(self, root):
        if root:
            print(root._element,end='')
            self.preOrder(root._left)
            self.preOrder(root._right)

    def postOrder(self, root):
        if root:
            self.postOrder(root._left)
            self.postOrder(root._right)
            print(root._element, end = ' ')

    def levelOrder(self, root):
        if root:
            pass
