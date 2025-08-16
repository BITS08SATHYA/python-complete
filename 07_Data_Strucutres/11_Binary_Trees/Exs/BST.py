from graphviz import Digraph

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

    def preOrder(self, troot):
        if troot:
            print(troot._element, end='->')
            self.preOrder(troot._left)
            self.preOrder(troot._right)

    def postOrder(self, troot):
        if troot:
            self.postOrder(troot._left)
            self.postOrder(troot._right)
            print(troot._element, end='->')


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

    def delete(self, e):
        p = self._root
        pp = None
        # determine where the node to be deleted is
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right
        if not p:
            return False
        # deleting a node with two children
        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps # Now p has at most one child
        # deleting a node with one child or no children
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        # deleting a root node
        if p == self._root:
            self._root = c
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c


class BinarySearchTreeVisualizer(BinarySearchTree):
    def visualize(self, troot):
        def add_nodes_edges(dot, node):
            if node:
                dot.node(str(id(node)), str(node._element))
                if node._left:
                    dot.edge(str(id(node)), str(id(node._left)))
                    add_nodes_edges(dot, node._left)
                if node._right:
                    dot.edge(str(id(node)), str(id(node._right)))
                    add_nodes_edges(dot, node._right)

        dot = Digraph()
        add_nodes_edges(dot, troot)
        return dot


# B = BinarySearchTree()
# # Iterative
# # B.insert(B._root, 50)
# # B.insert(B._root, 30)
# # B.insert(B._root, 80)
# # B.insert(B._root, 10)
# # B.insert(B._root, 40)
# # B.insert(B._root, 60)
#
# B._root = B.rinsert(B._root, 50)
# B.rinsert(B._root, 30)
# B.rinsert(B._root, 80)
# B.rinsert(B._root, 10)
# B.inorder(B._root)
# print('\n')
# B.preOrder(B._root)
# print('\n')
# B.delete(30)
# B.inorder(B._root)

# Example usage
B = BinarySearchTreeVisualizer()
B._root = B.rinsert(B._root, 50)
B.rinsert(B._root, 30)
B.rinsert(B._root, 80)
B.rinsert(B._root, 10)

# Visualize before deletion
dot = B.visualize(B._root)
dot.render('tree_before', format='png', cleanup=True)

# Perform deletion
B.delete(30)

# Visualize after deletion
dot = B.visualize(B._root)
dot.render('tree_after', format='png', cleanup=True)


