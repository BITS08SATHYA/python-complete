from wsgiref.validate import header_re


class Node:
    __slots__ = ('_element', '_next', '_prev')

    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoublyLinkedList:
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
        while p:
            print(p._element, end='->')
            p = p._next
        print()

    def addLast(self, e):
        newest = Node(e, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1

    def addFirst(self, e):
        newest = Node(e, None, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size += 1

    def addAny(self, e, position):
        newest = Node(e, None, None)
        p = self._head
        if self.isempty():
            self._head = newest
            self._tail = newest
        i = 0
        while i < position - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1

    def removeFirst(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e

    def removeLast(self):
        if self.isempty():
            print('List is empty')
        e = self._tail._element
        self._tail = self._tail._prev
        self._size -= 1
        return e

    def removeAny(self, position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -= 1
        return e








D = DoublyLinkedList()
D.addLast(3)
D.addLast(4)
D.addLast(5)
D.display()
D.addFirst(6)
D.display()
D.addAny(10,2 )
D.display()
D.removeFirst()
D.display()
D.removeAny(2)
D.display()

