from LinkedList import LinkedList

class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [LinkedList() for _ in range(self.hashtable_size)]

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


H = HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(81)
H.insert(60)
H.insert(86)
H.insert(28)
H.display()
print('Result: ' ,H.search(64))

