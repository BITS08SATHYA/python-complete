class Node:
    __slots__ = '_data', '_next', '_prev'
    def __init__(self, data, next, prev):
        self._data = data
        self._next = None
        self._prev = None

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def forward(self):
        p = self._head
        while p:
            print(p._data, end = '<->')
            p = p._next
        print()

    def backward(self):
        p = self._tail
        while p:
            print(p._data, end = '<->')
            p = p._prev
        print()

    def addFirst(self, data):
        newest = Node(data, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        newest._next = self._head
        self._head._prev = newest
        self._head = newest
        self._size += 1

    def addLast(self, data):
        newest = Node(data, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        newest._prev = self._tail
        self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addAny(self, data, pos):
        newest = Node(data, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        elif pos == 0:
            self.addFirst(data)
            return
        elif pos == self._size - 1:
            self.addLast(data)
            return
        else:
            i = 1
            p = self._head
            while p and i < pos - 1:
                p = p._next
                i += 1
            newest._next = p._next
            p._next._prev = newest
            p._next = newest
            newest._prev = p
        self._size += 1

    def removeFirst(self):
        if self.isempty():
            print("List is empty")
            return
        e = self._head._data
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e

    def removeLast(self):
        if self.isempty():
            print("List is empty")

