__author__= 'Aditya Pulekar','Mandar Badave'
"""
CSCI-603: Lab 2-1
Author: Aditya Pulekar , Mandar Badave

This is a program that draws trees and a house on PyCharm console (Python
Turtle Graphics)& calculates the total units of wood obtained from the trunks
of the trees and the house drawn during the night and, then, builds a new house during the day on the console which
utilises all of the wood obtained from the trunks and the house built during the night
"""
import turtle, random , math
from array import*
count=1


"""
The function provides a space of 100 pixels between two trees
and between a tree and a house
"""
def InitPos(trunkLen):
    turtle.penup()
    turtle.forward(trunkLen)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor("green")
    turtle.forward(100)
    turtle.pencolor("black")


"""
Initialize for drawing
:pre: pos (0,0), heading (east), up
:post: pos (-200,0), heading (North), up
:return: None
"""
def StartPos():
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(0)
    turtle.pendown()


"""
The function draws the trunk of any of the three types of a tree
"""
def trunk(trunkLen):
    turtle.pencolor("brown")
    turtle.left(90)
    turtle.forward(trunkLen)
    turtle.right(90)
    turtle.pencolor("black")


"""
The function draws the top of a pine tree
"""
def triangle():
    turtle.pencolor("green")
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(10)
    turtle.pencolor("black")


"""
This function draws the top of the third type of tree (i.e. a square)
"""
def DifferentShape():
    turtle.pencolor("green")
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pencolor("black")


"""
This function adjusts the position of the pen to draw a star
"""
def starLocAdjust(longestTrunk):
    turtle.penup()
    turtle.left(90)
    turtle.forward(longestTrunk+50)
    turtle.pendown()


"""
This function builds a house during the night with a roof angle of 45
"""
def buildHouse():
    turtle.pencolor("brown")
    turtle.left(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(70.7)
    turtle.right(90)
    turtle.forward(70.7)
    turtle.right(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.pencolor("green")
    turtle.forward(100)
    turtle.pencolor("black")


"""
This function builds a house during the day using the wood obtained from the
trunk and house built  during the night
"""
def buildNewHouse(lenOfWalls):
    turtle.pencolor("brown")
    turtle.left(90)
    turtle.forward(lenOfWalls)
    turtle.right(45)
    turtle.forward(lenOfWalls/math.sqrt(2))
    turtle.right(90)
    turtle.forward(lenOfWalls/math.sqrt(2))
    turtle.right(45)
    turtle.forward(lenOfWalls)
    turtle.right(90)
    turtle.penup()
    turtle.forward(lenOfWalls)
    turtle.left(180)


"""
The function draws the star at a height more than the tallest of
all the trees which are drawn
"""
def star(longestTrunk):
    starLocAdjust(longestTrunk)
    turtle.pencolor("purple")
    for i in range(0,8):
        turtle.forward(10)
        turtle.backward(10)
        turtle.right(45)
    turtle.pencolor("black")
    turtle.hideturtle()


"""
This function draws every type of the three types of trees at random
"""
def drawTree(x,t,Max,houseLoc):
    global count
    if(t=='Maple'):
        trunkLen=random.uniform(50,150)
        trunk(trunkLen)
        turtle.pencolor("green")
        turtle.circle(20,360)
        turtle.pencolor("black")
        turtle.right(90)
        netHeight=trunkLen+60
        Max.append(netHeight)
        if(count<x):
            InitPos(trunkLen)
        else:
            turtle.penup()
            turtle.forward(trunkLen)
            turtle.left(90)
        if(count==houseLoc):
            buildHouse()
            count=count+1
        else:
            count=count+1
            return count

    elif(t=='Pine'):
        trunkLen=random.uniform(50,200)
        trunk(trunkLen)
        triangle()
        turtle.right(90)
        netHeight=trunkLen+17.3
        Max.append(netHeight)
        if(count<x):
            InitPos(trunkLen)
        else:
            turtle.penup()
            turtle.forward(trunkLen)
            turtle.left(90)
        if(count==houseLoc):
            buildHouse()
            count=count+1
        else:
            count=count+1

    else:
        trunkLen=random.uniform(50,200)
        trunk(trunkLen)
        DifferentShape()
        netHeight=trunkLen+20
        Max.append(netHeight)
        if(count<x):
            InitPos(trunkLen)
        else:
            turtle.penup()
            turtle.forward(trunkLen)
            turtle.left(90)
        if(count==houseLoc):
            buildHouse()
            count=count+1
        else:
            count=count+1


"""
The function calculates the length of walls of the building
to be constructed during the day as well as constructs its roof
"""
def dayTime(totalWood):
    print("We have {} units of lumber for building.".format(totalWood))
    lenOfWalls=totalWood/(2+math.sqrt(2))
    print("We will build a house with walls {} tall.".format(lenOfWalls))
    buildNewHouse(lenOfWalls)


"""
The function draws the sun during the day
"""
def showSun():
    turtle.penup()
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.pendown()
    turtle.pencolor("orange")
    turtle.circle(50,360)
    turtle.hideturtle()


"""
This function is responsible for the random selection between the
three types of the trees and drawing as many trees as specified
by the user
:return: findmax
"""
def sketch(x,house):
    findMax=array('d')
    var=x
    if(house=='y'):
        houseLoc=random.randint(1,(x-1))
    else:
        houseLoc=0
    for index in range(0,var):
        t=random.choice(['Maple','Pine','DifferentTree'])
        drawTree(x,t,findMax,houseLoc)
    longestTrunk=max(findMax)
    star(longestTrunk)
    return findMax


"""
This function calculates the total units of wood generated on cutting
down the trunks of the trees and the house present during the night
:return: total
"""
def WoodQuantity(findMax):
    total=0
    for index in findMax:
        total=total+index
    return total


"""
The main function
"""
def main():
    x=int(input('Enter the number of trees: '))
    house=input('Is there a House in the forest (y/n)? ')
    StartPos()
    findmax=sketch(x,house)
    input('Night is done, press enter for the day')
    turtle.clearscreen()
    turtle.penup()
    turtle.setx(-150)
    turtle.sety(-150)
    turtle.pendown()
    total=WoodQuantity(findmax)

    """
    Adding the wood obtained from the trunks and the house built during the night
    """
    dayTime(total+341.4)
    showSun()
    print('Day is done, house is built, ')
    input('Press ENTER to quit')


if __name__=='__main__':
    main()
