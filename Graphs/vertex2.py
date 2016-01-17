class Vertex :
    __slots__ = 'key','connectsTo'

    def __init__(self,key):
        self.key = key
        self.connectsTo = {}

    def addNeighbor(self,nbr,weight):
        self.connectsTo[nbr] = weight


    def __str__(self):
        return str(self.key) + " ConnectsTo --> " + str([x.key for x in self.connectsTo])

    def getConnections(self):
        return self.connectsTo.keys()

    def getWeight(self,key):
        return self.connectsTo[key]

def main():
    vertexA = Vertex('A')
    vertexB = Vertex('B')
    vertexC = Vertex('C')
    vertexD = Vertex('D')
    vertexA.addNeighbor(vertexB, 3)
    vertexA.addNeighbor(vertexC, 1)
    vertexB.addNeighbor(vertexA, 4)
    vertexB.addNeighbor(vertexC, 2)
    vertexC.addNeighbor(vertexD, 5)

    # test __str__()
    print(vertexA)
    print(vertexB)
    print(vertexC)
    print(vertexD)

    # test getWeight()
    print('A -> B weight (3):', vertexA.getWeight(vertexB))
    print('B -> A weight (4):', vertexB.getWeight(vertexA))
    print('C -> D weight (5):', vertexC.getWeight(vertexD))

    # test getConnections():
    print("B's neighbors ():", [vertex.key for vertex in vertexB.getConnections()])
    print("D's neighbors ():", list(vertexD.getConnections()))

if __name__ == '__main__':
    main()