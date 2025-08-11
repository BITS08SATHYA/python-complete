class Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
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
             print(p._element,  end='-->')
             p = p._next
         print('')

    # Insert methods started
    def insertHead(self, ele):
        new_node = Node(ele, self._head)
        if self.isempty():
            self._head = new_node
            self._tail = new_node
        new_node._next = self._head
        self._head = new_node
        self._size += 1

    def insertTail(self, element):
        new_node = Node(element, None)
        if self.isempty():
            self._head = new_node
            self._tail = new_node
        self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def insertAny(self, element, pos):
        new_node = Node(element, None)
        if self.isempty() or pos == 0:
            self._head = new_node
            self._tail = new_node
        i = 1
        p = self._head
        while p and i < pos-1:
            p = p._next
        new_node._next = p._next
        p._next = new_node
        self._size += 1

    # Insert methods completed

    # delete methods started
    def removeHead(self):
        if self.isempty():
            print('List is empty')
            return
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element

    def removeTail(self):
        if self.isempty():
            print("List is empty")
            return
        i = 1
        p = self._head
        while i < self._size - 1:
            p = p._next
            i += 1
        self._tail = p
        self._tail._next = None
        self._size -= 1
        return p._next._element

    def removeAny(self, pos):
        if self.isempty():
            print('List is empty')
            return
        elif pos == 0:
            self.removeHead()
        elif pos == self._size - 1:
            self.removeTail()
        else:
            i = 1
            p = self._head
            while p and i < pos - 1:
                p = p._next
                i += 1
            e = p._next._element
            p._next = p._next._next
        self._size -= 1
        if self._size == 0:
            self._head = None
            self._tail = None
        return e

    def search(self, target):
        p = self._head
        index = 0
        while p:
            if p._element == target:
                return index
            p = p._next
            index += 1
        return -1




