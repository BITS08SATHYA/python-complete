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
        newest._prev = None
        newest._next = self._head
        self._head._prev = newest
        self._head = newest
        self._size += 1

