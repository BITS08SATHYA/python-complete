class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class StacksLinked:

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, element ):
        newest = _Node(element, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
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
        if self.isempty():
            print('Stack is empty')
            return
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end='->')
            p = p._next
        print()


S = StacksLinked()
S.push(1)
S.push(2)
S.push(3)
S.display()
S.pop()
S.display()
print(S.top())
