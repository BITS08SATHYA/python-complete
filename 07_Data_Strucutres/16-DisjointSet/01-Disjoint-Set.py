class DisjointSet:

    def __init__(self,n):
        self.n = n
        self.parent = [-1] * (n+1)

    @classmethod
    def from_parent(cls, arr):
        """
        Build directly from a given parent array (1-based).
        Example [-1, 5 -1, 3, -1 ,3 ,1 ,1 , 1, 5]
        :param arr:
        :return:
        """
        n = len(arr)
        obj = cls(n)
        obj.parent = [0] + arr[:]
        return obj

