class QueueWArrays:
    def __init__(self, size):
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
        self._data.pop(0)
        self._size -= 1

    def first(self):
        return self._data[0] if not self.isempty() else None

