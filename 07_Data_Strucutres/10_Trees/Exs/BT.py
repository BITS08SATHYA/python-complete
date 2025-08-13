import Q_LL

class _Node:

    __slots__ = '_element','_left','_right'

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
            print(root._element, end='->')
            self.inorder(root._right)

    def preOrder(self, root):
        if root:
            print(root._element, end='->')
            self.preOrder(root._left)
            self.preOrder(root._right)

    def postOrder(self, root):
        if root:
            self.postOrder(root._left)
            self.postOrder(root._right)
            print(root._element, end='->')

    def levelOrder(self):
        Q = Q_LL.QueuesLinkedList()
        t = self._root
        print(t._element, end='->')
        Q.enqueue(t)
        while not Q.is_empty():
            t = Q.dequeue()
            if t._left:
                print(t._left._element, end='->')
                Q.enqueue(t._left)
            if t._right:
                print(t._right._element, end='->')
                Q.enqueue(t._right)

    def count(self, root):
        if root:
            x = self.count(root._left)
            y = self.count(root._right)
            return x + y + 1
        return 0

    def height(self, root):
        if root:
            x = self.height(root._left)
            y = self.height(root._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0