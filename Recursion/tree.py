__author__ = 'Addy'
import turtle, random
def drawTree(n,size):
    if(n>0):
        turtle.forward(size)
        turtle.left(45)
        drawTree(n-1,size/2)
        turtle.right(90)
        drawTree(n-1,size/2)
        turtle.left(45)
        turtle.back(size)

def main():
    turtle.left(90)
    drawTree(5,100)
    turtle.done()

if __name__ == '__main__':
    main()