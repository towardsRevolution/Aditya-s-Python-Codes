"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS
Author: Aditya Pulekar
Author: Mandar Badave

An implementation of a graph data structure as an adjacency list.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

from vertexLab9 import Vertex

class Graph:
    """
    A graph implemented as an adjacency list of vertices.

    :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
        object
    :slot: numVertices (int):  The total number of vertices in the graph
    """

    __slots__ = 'vertList', 'numVertices'

    def __init__(self):
        """
        Initialize the graph
        :return: None
        """
        self.vertList = {}
        self.numVertices = 0

    def getVertex(self, key):
        """
        Retrieve the vertex from the graph.
        :param key: The vertex identifier
        :return: Vertex if it is present, otherwise None
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        """
        Returns whether the vertex is in the graph or not.  This allows the
        user to do:

            key in graph

        :param key: The vertex identifier
        :return: True if the vertex is present, and False if not
        """
        return key in self.vertList

    def addEdge(self, src, dest, cost=0):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        :param src: The source vertex identifier
        :param dest: The destination vertex identifier
        :param cost: The edge cost (defaults to 0)
        :return: None
        """
        if src not in self.vertList:
            self.addVertex(src)
        if dest not in self.vertList:
            self.addVertex(dest)
        self.vertList[src].addNeighbor(self.vertList[dest], cost)

    def getVertices(self):
        """
        Return the collection of vertex identifiers in the graph.
        :return: A list of vertex identifiers
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        Return an iterator over the vertices in the graph.  This allows the
        user to do:

            for vertex in graph:
                ...

        :return: A list iterator over Vertex objects
        """
        return iter(self.vertList.values())

