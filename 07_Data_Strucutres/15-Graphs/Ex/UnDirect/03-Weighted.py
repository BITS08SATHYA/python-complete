import numpy as np

class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))

    def insertEdge(self, u , v, x = 1):
        self._adjMat[u][v] = x

    def removeEdge(self, u, v):
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
            print(i, end=' ')
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
        for j in range(self._vertices):
            if self._adjMat[j][v] != 0:
                count += 1
        return count

    def display_adjMat(self):
        print(self._adjMat)

# UnDirected Unweighted graphs
G = Graph(4)
G.display_adjMat()
print( 'Vertices: ' ,G.vertex_count())
print( 'Edges: ' ,G.edge_count())
G.insertEdge(0, 1, 26)
G.insertEdge(0, 2, 16)
G.insertEdge(1, 0, 26)
G.insertEdge(1,2, 12)
G.insertEdge(2,0, 16)
G.insertEdge(2,1, 12)
G.insertEdge(2,3, 8)
G.insertEdge(3,2, 8)
G.display_adjMat()
print('Edges: ', G.edge_count())
G.edges()
print('Edge between 1-3',G.exist_edge(1,3))
print('Edge between 1-2',G.exist_edge(1,2))
print('Degree', G.indegree(2))
G.removeEdge(1,2)
print('Edge between 1-2', G.exist_edge(1,2))




