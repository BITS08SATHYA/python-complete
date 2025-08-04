class _Node:
    __slots__ = '_element', '_next'
    def __init__(self,element, next):
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
            print(p._element, end=" --> ")
            p = p._next
        print('None')

    def search(self, target):
        p = self._head
        index = 0
        while p:
            if p._element == target:
                return index
            p = p._next
            index += 1
        return -1

    def get(self, idx):
        # it should return node not the element
        if self.isempty():
            return None
        p = self._head
        index = 0
        while p:
            if idx == index:
                return p
            p = p._next
            index += 1
        return -1

    def addFirst(self,e):
        node = _Node(e, None)
        if self.isempty():
            self._head = self._tail = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

    def addlast(self, e):
        node = _Node(e, None)
        if self.isempty():
            self._head = self._tail = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def addany(self, position, element):
        newest = _Node(element, None)
        p = self._head
        i = 0
        if position == 0:
            self.addFirst(element)
        elif position == -1:
            self.addlast(element)
        else:
            while i < position - 1:
                p = p._next
                i = i + 1
            newest._next = p._next
            p._next = newest
        self._size += 1


L = LinkedList()
L.addlast(7)
L.addlast(8)
L.addlast(9)
L.addlast(10)
L.addFirst(1)
L.addFirst(25)
L.display()
# print(L.get(3))
L.addany(len(L), 89)
L.display()
# print("Element found at index:  ", L.search(50))
# print('Size: ', L.__len__())