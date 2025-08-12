class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class Stacks_LL:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, e):
        new_node = _Node(e, None)
        if self.isempty():
            self._top = new_node
        new_node._next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        element = self._top._element
        self._top = self._top._next
        self._size -= 1
        return element

    def top(self):
        return self._top._element if not self.isempty() else None

    def display(self):
        p = self._top
        while p:
            print(p._element, end='->')
            p = p._next
        print()