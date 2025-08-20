from LinkedList import LinkedList

class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            self.hashtable[i] = LinkedList()

    def hashCode(self, key):
        return key % self.hashtable_size

    def insert(self, element):
        i = self.hashCode(element)
        self.hashtable[i].insertSorted(element)

    def search(self, key):
        i = self.hashCode(key)
        return self.hashtable[i].search(key) != -1

    def display(self):
        for i in range(self.hashtable_size):
            print('[',i,'] ', end='')
            self.hashtable[i].display()
        print()