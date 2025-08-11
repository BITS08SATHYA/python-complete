class _Node:
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

    def insert_head(self, val):
        new_node = _Node(val, self._head)
        if self.isempty():
            self._head = new_node
            self._tail = new_node
        new_node._next = self._head
        self._head = new_node
        self._size += 1

    def insert_tail(self, val):
        new_node = _Node(val, None)
        if self.isempty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def insert_Any(self, val, pos):
        new_node = _Node(val, None)
        p = self._head
        i = 0
        while p and i < pos-1:
            p = p._next
            i += 1
        new_node._next = p._next
        p._next = new_node
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element , end = '->')
            p = p._next

    def search(self, target):
        p = self._head
        index = 0
        while p:
            if p._element == target:
                return index
            index += 1
            p = p._next
        return -1

#     remove elements
    def remove_first(self):
        if self.isempty():
            print('List is empty')
            return
        ele = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail = None
        return ele

    def remove_last(self):
        if self.isempty():
            print('List is empty')
            return
        p = self._head
        i = 1
        while i < self._size - 1:
            p = p._next
            i += 1
        self._tail = p
        p = p._next
        ele = p._element
        self._tail._next = None
        self._size -= 1
        return ele

    def removeAny(self, pos):
        ele = 0
        if self.isempty():
            print('List is empty')
            return
        elif pos == 0:
            self.remove_first()
        elif pos == self._size - 1:
            self.remove_last()
        else:
            p = self._head
            i = 1
            while i < pos - 1:
                p = p._next
                i += 1
            e = p._next._element
            p._next = p._next._next
        self._size -= 1
        return ele


ll = LinkedList()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_tail(5)
ll.insert_head(3)
# ll.display()
# print('\n')
# print(ll.search(5))
# ll.insert_Any(30, 1)
# print('\n')
# ll.display()
# print('\n')
# ll.remove_first()
# print('\n')
ll.display()
print('\n')
ll.remove_last()
print('\n')
ll.display()
print('\n')
ll.removeAny(3)
print('\n')
ll.display()
