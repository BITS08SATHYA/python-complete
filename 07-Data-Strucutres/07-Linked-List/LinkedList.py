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

    def addlast(self, e):
        node = _Node(e, None)
        if self.isempty():
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

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


L = LinkedList()
L.addlast(7)
L.addlast(8)
L.addlast(9)
L.addlast(10)
L.display()
print("Element found at index:  ", L.search(50))
print('Size: ', L.__len__())