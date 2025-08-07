import Q_LL

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
            print(root._element, end = '->')
            self.inOrder(root._right)

    def preOrder(self, root):
        if root:
            print(root._element,end='->')
            self.preOrder(root._left)
            self.preOrder(root._right)

    def postOrder(self, root):
        if root:
            self.postOrder(root._left)
            self.postOrder(root._right)
            print(root._element, end = '->')

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


# X = BinaryTree()
# Y = BinaryTree()
# Z = BinaryTree()
# a = BinaryTree()
# X.maketree(20, a, a)
# Y.maketree(30, a, a)
# Z.maketree(10, X, Y)
# print('In Order Traversal: ')
# Z.inOrder(Z._root)
# print('\n')
# print('Pre Order Traversal: ')
# Z.preOrder(Z._root)
# print('\n')
# print('Post Order Traversal: ')
# Z.postOrder(Z._root)

X = BinaryTree()
Y = BinaryTree()
Z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()
X.maketree(40, a, a)
Y.maketree(60, a, a)
Z.maketree(20, X, a)
r.maketree(50, a, Y)
s.maketree(30, r, a)
t.maketree(10, Z, s)

print('In Order Traversal: ')
t.inOrder(t._root)
print('\n')
print('Pre Order Traversal: ')
t.preOrder(t._root)
print('\n')
print('Post Order Traversal: ')
t.postOrder(t._root)
print('\n')
print('Level Order Traversal: ')
t.levelOrder()
print('Count')
print('\n')
print(t.count(t._root))
print('\n')
print('Height of the tree')
print(t.height(t._root)-1)
