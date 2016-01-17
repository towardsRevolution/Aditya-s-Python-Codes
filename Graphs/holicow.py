"""
This program creates a directed and unweighted graph of cows and paintballs from the data read from a source file.
It, then, performs the coloring of the cows as per the triggering of the paintballs. The triggering and painting
occurs as per the neighbors of the individual vertices in the graph.

Author: Aditya Pulekar
Author: Mandar Badave
"""

import sys                      #argv
from graphLab9 import Graph
from vertexLab9 import Vertex
import math, random

"""
Class creates a directed and unweighted graph of cows and paintballs from the data read from a source file and
triggers the paintballs and paints the cows as per the neighbors of the individual vertices in the graph.
"""
class CowsPaintGraph:
    __slots__ = "srcFile"

    def __init__(self,srcFile):
        """
        Constructor for this class
        :param srcFile: file from which the data is being read
        :return:
        """
        self.srcFile = srcFile

    def __beginTriggering(self,triggeredVertex,loc):
        """
        Helper function for the triggering operation of the paintballs
        :param triggeredVertex: a vertex
        :param loc: location in the list corresponding to a key
        :return:
        """
        if loc < len(triggeredVertex.connectedTo) and triggeredVertex.connectedTo[loc].type == "paintball":
            print("\t",triggeredVertex.connectedTo[loc].name," paint ball is triggered by ",
                  triggeredVertex.name, " paint ball")
            self.__beginTriggering(triggeredVertex.connectedTo[loc],0)
            self.__beginTriggering(triggeredVertex,loc+1)

        elif loc < len(triggeredVertex.connectedTo)and triggeredVertex.connectedTo[loc].type == "cow":
            if triggeredVertex.name not in triggeredVertex.connectedTo[loc].cacheforCNP:
                triggeredVertex.connectedTo[loc].paintOnCows(triggeredVertex.name)
            print("\t",triggeredVertex.connectedTo[loc].name, " is painted ",triggeredVertex.name , "!")

            #The below statement signifies that we should remain at the current dictionary level
            self.__beginTriggering(triggeredVertex,loc+1)

        elif len(triggeredVertex.connectedTo) == 0:
            print("\t No Cows were painted by any starting paintball!")

    def beginTriggering(self,vertList):
        """
        This function performs the triggering of the paintballs
        :param vertList: a dictionary of vertices
        :return:
        """
        for itr in vertList:
            if vertList[itr].type == "paintball":
                print("Triggering ",itr, " paint ball...")
                self.__beginTriggering(vertList[itr],0)

    def readingFileData(self,CowsAndPaintballs):
        """
        Reads the data from a file and creates vertices to be further linked
        in a graph
        :param CowsAndPaintballs: An instance of this class
        :return: a list containing a graph dictionary and a counter value
        """
        try:
            with open(CowsAndPaintballs.srcFile) as f:
                uniqueList = []
                graph = Graph()
                colorCount=0
                for line in f:
                    line = line.split()
                    if line[0] == "cow":
                        graph.vertList[line[1]] = Vertex(line[1],"cow",[int(line[2]),int(line[3])],0)
                    elif line[0] == "paintball":
                        graph.vertList[line[1]] = Vertex(line[1],"paintball",[int(line[2]),int(line[3])],int(line[4]))
                        colorCount = colorCount + 1
            uniqueList.append(graph.vertList)
            uniqueList.append(colorCount)
            return uniqueList
        except FileNotFoundError as e:
            print('File not found : ',CowsAndPaintballs.srcFile)
            sys.exit()

    def graphCreation(self,graphDict):
        """
        Creates the graph using the Eucledian distance formula
        :param graphDict: a dictionary of the graph
        :return: the dictionary of the graph
        """
        for key, vertexObj in graphDict.items():
                x = vertexObj.coordinate[0]
                y = vertexObj.coordinate[1]
                for itr in graphDict:
                    if itr != key:
                        x1 = graphDict[itr].coordinate[0]
                        y1 = graphDict[itr].coordinate[1]
                        dist = math.sqrt(math.pow((x - x1),2) + math.pow((y - y1),2))
                        if(dist <= vertexObj.radius):
                            vertexObj.addNeighbor(graphDict[itr])
        return graphDict

    def finalResults(self,bestKey,graphDict,colorCount):
        """
        Displays the final results
        :param bestKey: The color which paints maximum number of cows
        :param graphDict: a dictionary of the graph
        :param colorCount: number of colors being considered
        :return:
        """
        print("\nResults: ")
        if(len(bestKey) > 1):
            print("There are more than one paintballs which could be the best choice...")
            print("We choose anyone of them randomly since it is a tie...")
        print("Triggering the ",random.choice(bestKey) , " paint ball/s is the best choice with ",
            colorCount," total paints on the cows: \n")    #", ".join(map(str,bestKey))

        #Displaying the names of the cows and all the colors in which each one has been painted
        for itr,val in graphDict.items():
           if val.type == "cow":
               print(val.name,"'s colors: {",", ".join(map(str,val.cacheforCNP)),"}")

    def printGraph(self,graphDict):
        """
        Prints the graph
        :param graphDict:
        :return: the dictionary of the number of cows being painted by a single color
        """
        cowCount= {}
        for key,vert in graphDict.items():
            print(vert)
            if(vert.type == 'paintball'):
               cowCount[key] = str([str((x.type == 'cow')) for x in vert.connectedTo].count('True'))
        return cowCount

def main():
    #Handling the case in which the arguments are not given correctly
    if len(sys.argv)!=2:
        print("Usage: python3 holicow.py CowsNPaintBalls.txt")
        return
    CowsAndPaintballs = CowsPaintGraph(sys.argv[1])

    #Reading the data from the file
    uniqueList = CowsAndPaintballs.readingFileData(CowsAndPaintballs)
    graphDict = uniqueList[0]
    colorCount = uniqueList[1]

    print("Field of Dreams","\n","--------------------")

    #Using the Eucledian distance formula to decide the neighbors of every vertex
    graphDict = CowsAndPaintballs.graphCreation(graphDict)

    #Printing the graph in the adjacency list format
    cowCount = CowsAndPaintballs.printGraph(graphDict)

    #Finding out which color paints the maximum number of cows
    if len(cowCount) is not 0:
        maxCowsPainted = max(cowCount.values())
        bestKey = [ p for p,q in cowCount.items() if(q == maxCowsPainted)]

        print("\nBeginning Simulation....")

        #Note: If we call the functions in a static way, we need to include "self" inside the
        #      parenthesis
        #Triggering operation begins here....
        CowsAndPaintballs.beginTriggering(graphDict)

        #Obtaining the results
        CowsAndPaintballs.finalResults(bestKey,graphDict,colorCount)
    else:
        print("No Cows were painted since there were no paintballs!")



if __name__ == '__main__':
    main()
