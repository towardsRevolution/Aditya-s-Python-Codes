"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS
Author: Aditya Pulekar
Author: Mandar Badave

An implementation of a vertex as part of a graph.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = 'name','type', 'connectedTo', 'coordinate', 'radius', 'cacheforCNP'

    def __init__(self, name, type , coordinate, radius):              #key , name,
        """
        Initialize a vertex
        :param key: The identifier for this vertex
        :return: None
        """
        # self.id = key
        self.name = name
        self.type = type
        self.coordinate = coordinate
        self.radius = radius
        self.connectedTo = []
        self.cacheforCNP = []

    def addNeighbor(self, nbr):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight (int): The edge cost
        :return: None
        """
        self.connectedTo.append(nbr)

    def paintOnCows(self,color):
        self.cacheforCNP.append(color)

    def cowsWithThisColor(self,cows):
        self.cacheforCNP.append(cows)

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self.name) +  ' connectedTo: ' + str([str(x.name) for x in self.connectedTo])

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight (int)
        """
        return self.connectedTo[nbr]

