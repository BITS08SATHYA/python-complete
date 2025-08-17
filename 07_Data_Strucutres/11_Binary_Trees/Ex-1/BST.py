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

    def delete_for_understanding(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
                print(f"Moving left: {p._element if p else 'None'}")
            else:
                p = p._right
                print(f"Moving right: {p._element if p else 'None'}")
        if p is None:
            return 'The element is not found!'
        # Case - 1, deleting the root node
        if pp is None: # p is the root node
            # root has 0 or 1 child
            if p._left is None or p._right is None:
                # pick the single child if present, else None
                self._root = p._left if p._left else p._right
                print('Self._root:', self._root)
                return f'The element {e} is deleted from the tree (root case).'
            else:  # root has two children
                # we will implement this later
                return 'Root has two Children -- handle it in case 3 -- handle this case later!'
        # Case - 2, deleting a non-root with 0 or 1 child
        if p._left is None or p._right is None:
            c = p._left if p._left else p._right   # could be None (leaf node)
            if pp._left is p:
                pp._left = c
            else:
                pp._right = c
            return f'The element {e} is deleted from (non-root with <=1 child.'

        return f'Not implemented for non-root yet!'

    def delete(self, e):
        # search for p (target node) and pp (parent of target node)
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right

        if p is None:
            return 'The element is not found!'

        # Case where the node with two children (use IN-order predecessor)
        if p._left and p._right:
            # find in-order predecessor s and its parent ps:
            # predecessor = max node in left subtree (go left once, then all the way right)
            ps = p
            s = p._left
            while s._right:
                ps = s
                s = s._right

            # Copy predecessor's value up into p
            p._element = s._element

            # Now delete the predecessor node s instead (s has at most one child - only possible left child)
            p = s
            pp = ps  # Now p has at most one child

        # Case 1 & 2: node with 0 or 1 child (root or non-root)
        # after the block above, p is a node with at most one child
        c = p._left if p._left else p._right # for predecessor case, this can only be p._left

        if pp is None:   # deleting the root node
            self._root = c
        elif pp._left is p:
            pp._left = c
        else:
            pp._right = c

        # (Optional) help GC
        p._left = p._right = None

        return f'The element {e} is deleted from the tree.'





    def draw_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self._root
            if node is None:
                return 'No nodes in the tree to visualize!'

        print(" " * (level * 4) + prefix + str(node._element))

        if node._left:
            self.draw_tree(node._left, level + 1, "L ----")
        if node._right:
            self.draw_tree(node._right, level + 1, "R ----")

        if level == 0:
            return 'Tree Visualiation Completed!'
        return None


# class BinarySearchTreeVisualizer(BinarySearchTree):
#     def visualize(self, troot):
#         def add_nodes_edges(dot, node):
#             if node:
#                 dot.node(str(id(node)), str(node._element))
#                 if node._left:
#                     dot.edge(str(id(node)), str(id(node._left)))
#                     add_nodes_edges(dot, node._left)
#                 if node._right:
#                     dot.edge(str(id(node)), str(id(node._right)))
#                     add_nodes_edges(dot, node._right)
#
#         dot = Digraph()
#         add_nodes_edges(dot, troot)
#         return dot


B = BinarySearchTree()
# # Iterative
B.insert(B._root, 50)
# B.insert(B._root, 30)
# B.insert(B._root, 80)
# B.insert(B._root, 10)
# B.insert(B._root, 40)
# B.insert(B._root, 60)

B.draw_tree()
print('=*20*=')
print(B.delete(50))
print('=*20*=')
B.draw_tree()


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

# # Example usage
# B = BinarySearchTreeVisualizer()
# B._root = B.rinsert(B._root, 50)
# B.rinsert(B._root, 30)
# B.rinsert(B._root, 80)
# B.rinsert(B._root, 10)
#
# # Visualize before deletion
# dot = B.visualize(B._root)
# dot.render('tree_before', format='png', cleanup=True)
#
# # Perform deletion
# B.delete(30)
#
# # Visualize after deletion
# dot = B.visualize(B._root)
# dot.render('tree_after', format='png', cleanup=True)


