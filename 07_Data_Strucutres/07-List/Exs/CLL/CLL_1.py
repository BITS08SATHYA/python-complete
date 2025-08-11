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

    def addAny(self, element, pos):
        newest = Node(element, None)
        if self.isempty():
            print("List is empty")
            return
        elif pos == 0:
            self.addFirst(element)
        elif pos == self._size - 1:
            self.addLast(element)
        else:
            p = self._head
            i = 1
            while i < pos - 1:
                p = p._next
                i += 1
            newest._next = p._next
            p._next = newest
        self._size += 1

    def removeFirst(self):
        if self.isempty():
            print("List is empty")
            return
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None

    def removeLast(self):
        if self.isempty():
            print("List is empty")
            return
        p = self._head
        i = 1
        while p and i < self._size - 1:
            p = p._next
            i += 1
        p._next = self._head
        self._tail = p
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None
