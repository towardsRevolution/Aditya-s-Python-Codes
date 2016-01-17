"""
Author: Aditya Pulekar
"""
from vertex2 import Vertex

class Graph:
    __slots__ = 'vertextList','numVertices'

    def __init__(self):
        self.vertextList = {}
        self.numVertices = 0

    def addEdge(self,src,dest,cost=0):
        if src not in self.vertextList:
            self.addVertex(src)
        if dest not in self.vertextList:
            self.addVertex(dest)
        self.vertextList[src].addNeighbor(self.vertextList[dest],cost)

    def addVertex(self,key):
        if key not in self.vertextList:
            self.numVertices += 1
        v = Vertex(key)
        self.vertextList[key] = v

    def __iter__(self):
        return iter(self.vertextList.values())

    def __contains__(self, item):
        return item in self.vertextList

    def getVertices(self):
        return self.vertextList.keys()

    def getVertex(self,key):
        return self.vertextList[key]

def main():
    STATES = {
        'CT' : ('MA', 'RI'),
        'MA' : ('CT', 'NH', 'RI', 'VT'),
        'ME' : ('NH'),
        'NH' : ('MA', 'ME', 'VT'),
        'RI' : ('CT', 'MA'),
        'VT' : ('MA', 'NH')
    }

    # add all the edges to the graph
    northeast = Graph()
    for state, neighbors in STATES.items():
        for neighbor in neighbors:
            # this automatically creates a new vertices if not already present
            northeast.addEdge(state, neighbor)

    # display the vertices, which will show the connected neighbors.
    # this will call the __iter__() method to get the Vertex objects.
    for state in northeast:
        print(state)

    print(northeast.getVertices())

    # check the __contains__() method
    print('MA in northeast (True)?', 'MA' in northeast)
    print('CA in northeast (False)?', 'CA' in northeast)

    # test getVertex()
    #Whenever the vertex will be printed, the __str__ method in vertex2.py will be called
    print('MA vertex:', northeast.getVertex('MA'))

if __name__ == '__main__':
    main()