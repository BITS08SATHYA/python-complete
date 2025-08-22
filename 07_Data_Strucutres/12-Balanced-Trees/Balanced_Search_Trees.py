class _Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # new node has height = 1

class AVLTree:
    # utility get height
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # Utility: get balance factor
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Right rotation (Left heavy case)
    def right_rotate(self, y):

        x = y.left
        T2 = x.right

        # perform rotation
        x.right = y
        y.left = T2

        # update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # left rotation
    def left_rotate(self, x):

        y = x.right
        T2 = y.left

        # perform rotation
        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return _Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # update height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # balance factor
        balance = self.get_balance(root)

        # Case Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case left right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # case Right left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def preorder(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


tree = AVLTree()
root = None
nums = [10, 20 ,30, 40, 50 , 25]
for num in nums:
    root = tree.insert(root, num)

print("Preorder traversal of the constructed AVL tree is:")
tree.preorder(root)
print()
