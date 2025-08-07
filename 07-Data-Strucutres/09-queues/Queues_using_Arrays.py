class QueuesArrays:
    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return self._size == 0

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

    def dequeue(self):
        if self.isempty():
            print('Queue is empty!')
            return
        return self._data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is empty!')
            return
        return self._data[0]

Q = QueuesArrays()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q._data)
Q.dequeue()
print(Q._data)
print(Q.first())