__author__ = 'Aditya Pulekar'

"""
The below program forms a mosaic structure using recursion.
"""

import turtle
sum=0
def drawSquare(length):
    global sum
    sum=sum+(4*length)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

def drawNestedSquare(rd,length):
    if(rd==0):
        return
    else:
        drawSquare(length)
        drawNestedSquare(rd-1,length/3)
        turtle.forward(2*length)
        drawSquare(length)
        drawNestedSquare(rd-1,length/3)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(2*length)
        drawSquare(length)
        drawNestedSquare(rd-1,length/3)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(2*length)
        drawSquare(length)
        drawNestedSquare(rd-1,length/3)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(3*length)
        turtle.left(90)




def main():
    rd=int(input("Enter the recursion depth: "))
    length=int(input('Enter the length of the square: '))
    turtle.speed("fastest")
    turtle.penup()
    turtle.setx(-300)
    turtle.sety(-300)
    turtle.pendown()
    drawNestedSquare(rd,length)
    print('Total Distance travelled by the pointer: ',sum)
    input("Hit enter to exit...")

main()