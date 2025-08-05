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
        i = 0
        while i < len(self):
            print(p._element, end='->')
            p = p._next
            i += 1
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


D = DoublyLinkedList()
D.addLast(3)
D.addLast(4)
D.addLast(5)
D.display()

