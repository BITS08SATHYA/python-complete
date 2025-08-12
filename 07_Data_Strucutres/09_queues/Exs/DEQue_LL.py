class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class DEQueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        self._rear._next = newest
        self._rear = newest
        self._size += 1

    def addFirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        newest._next = self._front
        self._front = newest
        self._size += 1

    def removeFirst(self):
        if self.isempty():
            print('DEQue is empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def removeLast(self):
        if self.isempty():
            print('DEQue is empty')
            return
        p = self._front
        i = 1
        while p and i < self._size - 1:
            p = p._next
            i += 1
        e = self._rear._element
        self._rear = p
        self._rear._next = None
        self._size -= 1
        return e