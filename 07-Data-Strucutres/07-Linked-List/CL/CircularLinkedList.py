from email.feedparser import headerRE


class Node:
    __slots__ = ('_element', '_next')

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
        while i < len(self):
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()

    def addFirst(self, e):
        newest = Node(e, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1


    def addlast(self, e):
        newest = Node(e, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addAny(self, e ,position):
        newest = Node(e, None)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        # print(p._next._element, end='-->')
        newest._next = p._next
        p._next = newest
        self._size += 1

C = CircularLinkedList()
C.addlast(7)
C.addlast(4)
C.addlast(12)
C.addlast(8)
C.addlast(3)
print(C.addAny(88, 3))

C.display()
print('Size: ', len(C))