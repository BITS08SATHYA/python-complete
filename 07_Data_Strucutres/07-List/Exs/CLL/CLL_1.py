class Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def display(self):
        p = self._head
        i = 0
        while p:
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()


    def addFirst(self, element):
        newest = Node(element, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1

    def addLast(self, element):
        newest = Node(element, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        newest._next = self._tail._next
        self._tail._next = newest
        self._size += 1

