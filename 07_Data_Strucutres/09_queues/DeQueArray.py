class DEQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addFirst(self, e):
        self._data.insert(0, e)

    def addLast(self, e):
        self._data.append(e)

    def removeFirst(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('DEQue is Empty')
            return
        return self._data[-1]


D = DEQueArray()
D.addFirst(1)
D.addLast(2)
D.addLast(3)
print(D._data)