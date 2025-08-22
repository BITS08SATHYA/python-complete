import numpy as np
from Queues_LL import QueuesLinkedList

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))
        self._visited = [0] * vertices

    def insert_edge(self, u, v, x = 1):
        self._adjMat[u][v] = x

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end = ' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, '--', j)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count += 1
        return count

    def display_adjMat(self):
        print(self._adjMat)

    def BFS(self, s):
        i = s
        q = QueuesLinkedList()
        visited = [0] * self._vertices
        print(i, end = ' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                # print("I am printing the vertices ",j, end = '\n')
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end = ' ')
                    visited[j] = 1
                    q.enqueue(j)

    def BFS_1(self, s):
        i = s
        q = QueuesLinkedList()
        visited = [0] * self._vertices
        print(i, end = ' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end = ' ')
                    visited[j] = 1
                    q.enqueue(j)

    def BFS_2(self, s):
        i = s
        q = QueuesLinkedList()
        visited = [0] * self._vertices
        print(i, end = ' ')
        q.enqueue(i)
        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end = ' ')
                    visited[j] = 1
                    q.enqueue(j)

    def DFS(self, s):
        if self._visited[s] == 0:
            print(s, end = ' ')
            self._visited[s] = 1
            for j in range(self._vertices):
                if self._adjMat[s][j] == 1 and self._visited[j] == 0:
                    self.DFS(j)


G = Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)
print('BFS')
G.BFS(0)
# print("\nBFS from vertex 4")
# G.BFS(4)
# print('DFS')
# G.DFS(1)
# G.DFS(4)


# G = Graph(4)
# G.display_adjMat()
# print('Vertices: ', G.vertex_count())
# # print('Edges: ', G.edge_count())
# G.insert_edge(0, 1)
# G.insert_edge(0, 2)
# G.insert_edge(1, 2)
# G.insert_edge(2, 3)
# G.display_adjMat()
# print('Vertices: ', G.vertex_count())
# print('Edges: ', G.edge_count())
# G.edges()
# G.exist_edge(1, 3)
# print('Edge between 1 and 3: ', G.exist_edge(1, 3))
# print('Edge between 2 and 3: ', G.exist_edge(2, 3))