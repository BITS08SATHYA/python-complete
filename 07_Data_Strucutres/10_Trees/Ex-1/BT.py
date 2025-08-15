from Q_LL import QueuesLinkedList
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
        Q = QueuesLinkedList()
        t = self._root
        print(t._element, end=' ')
        Q.enqueue(t)
        while not Q.is_empty():
            t = Q.dequeue()
            if t._left:
                print(t._left._element, end=' ')
                Q.enqueue(t._left)
            if t._right:
                print(t._right._element, end=' ')
                Q.enqueue(t._right)

    def count(self, troot):
        if troot:
            return 1 + self.count(troot._left) + self.count(troot._right)
        return 0

    def height(self, troot):
        if troot:
            return 1 + max(self.height(troot._left), self.height(troot._right))
        return 0


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()

x.maketree(40, a, a)
y.maketree(60, a, a)
z.maketree(20, x, a)
r.maketree(50, a, y)
s.maketree(30, r, a)
t.maketree(10, z, s)



print("In-order Traversal: ")
t.inOrder(t._root)

print("\nPre-order Traversal: ")
t.preOrder(t._root)

print("\nPost-order Traversal: ")
t.postOrder(t._root)

print("\nLevel-order Traversal: ")
t.levelOrder()

print("\nCount of nodes in the tree: ", t.count(t._root))

print("Height of the tree: ", t.height(t._root))

