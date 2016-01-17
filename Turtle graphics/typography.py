__author__ = 'Aditya Pulekar'
"""
CSCI-603: Lab 1
Author: Aditya Pulekar

This is a program that draws the characters of my name "ADITYA PULEKAR" on PyCharm console (Python
Turtle Graphics).It demonstrates the importance of using functions and turtle module.
"""
import turtle

# This function introduces the spacing between two alphabets in a word
def Adjust():
    [x, y] = turtle.position()
    turtle.penup()
    x = x + 90
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.setheading(90)


# Function providing the space between two words
def spaceBar():
    [x, y] = turtle.position()
    turtle.penup()
    x = x + 70
    turtle.goto(x, 0)
    turtle.pendown()


# Initialise for drawing
# :pre: pos (0,0), heading (east), up
# :post: pos (-630,0), heading (North), up
# :return: None
def Initialize():
    turtle.penup()
    turtle.goto(-630, 0)
    turtle.pendown()


# The function brings the pen to a fixed location before drawing an alphabet
def Initial_pos(x, y):
    turtle.penup()
    turtle.right(90 + y)
    turtle.forward(50 + x)
    turtle.pendown()


# This function is responsible for the printing of the alphabets on the Python Turtle Graphics
def name():
    Initialize()
    A()
    D()
    I()
    T()
    Y()
    A()
    spaceBar()
    P()
    U()
    L()
    E()
    K()
    A()
    R()


def A():
    # Draw the alphabet "A"
    # First "A"
    # :pre: (relative) pos (-630,0), heading (North), up
    # :post: (relative) pos (-540,0), heading (North), up
    # Second "A"
    # :pre: (relative) pos (-180,0), heading (North), up
    # :post: (relative) pos (-20,0), heading (North), up
    # Third "A"
    # :pre: (relative) pos (340,0), heading (North), up
    # :post: (relative) pos (430,0), heading (North), up
    # :return: None
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    Adjust()


def D():
    # Draw the alphabet "D"
    # :pre: (relative) pos (-540,0), heading (east), up
    # :post: (relative) pos (-450,0), heading (North), up
    # :return: None
    turtle.setheading(0)
    turtle.circle(50, 180)
    turtle.left(90)
    turtle.forward(100)
    Adjust()


def I():
    # Draw the alphabet "I"
    # :pre: (relative) pos (-450,0), heading (east), up
    # :post: (relative) pos (-360,0), heading (North), up
    # :return: None
    turtle.setheading(0)
    turtle.forward(50)
    turtle.backward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    Initial_pos(50, 0)
    Adjust()


def T():
    # Draw the alphabet "T"
    # :pre: (relative) pos (-360,0), heading (east), up
    # :post: (relative) pos (-270,0), heading (North), up
    # :return: None
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)
    Initial_pos(50, 0)
    Adjust()


def Y():
    # Draw the alphabet "Y"
    # :pre: (relative) pos (-270,0), heading (east), up
    # :post: (relative) pos (-180,0), heading (North), up
    # :return: None
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(26.565)
    turtle.forward(55.90)
    turtle.backward(55.90)
    turtle.left(53.13)
    turtle.forward(55.90)
    turtle.penup()
    turtle.left(153.435)
    turtle.forward(100)
    Adjust()


def P():
    # Draw the alphabet "P"
    # :pre: (relative) pos (-180,0), heading (North), up
    # :post: (relative) pos (-20,0), heading (North), up
    # :return: None
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    Adjust()


def U():
    # Draw the alphabet "U"
    # :pre: (relative) pos (-20,0), heading (North), up
    # :post: (relative) pos (70,0), heading (North), up
    # :return: None
    turtle.setheading(90)
    turtle.forward(100)
    Initial_pos(0, 0)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    Adjust()


def L():
    # Draw the alphabet "L"
    # :pre: (relative) pos (70,0), heading (North), up
    # :post: (relative) pos (160,0), heading (North), up
    # :return: None
    turtle.setheading(90)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    Adjust()


def E():
    # Draw the alphabet "E"
    # :pre: (relative) pos (160,0), heading (North), up
    # :post: (relative) pos (250,0), heading (North), up
    # :return: None
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    Initial_pos(0, 0)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(50)
    Adjust()


def K():
    # Draw the alphabet "K"
    # :pre: (relative) pos (250,0), heading (North), up
    # :post: (relative) pos (340,0), heading (North), up
    # :return: None
    turtle.setheading(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(45)
    turtle.forward(70.7)
    turtle.backward(70.7)
    turtle.right(90)
    turtle.forward(70.7)
    Initial_pos(0, 45)
    Adjust()


def R():
    # Draw the alphabet "R"
    # :pre: (relative) pos (430,0), heading (North), up
    # :post: (relative) pos (430,0), heading (West), up
    # :return: None
    turtle.setheading(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(70.7)
    Initial_pos(0, 45)


# The main function
def main():
    name()
    turtle.hideturtle()
    input("Hit enter to close")



if __name__ == '__main__':
    main()
