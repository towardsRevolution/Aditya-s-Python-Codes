__author__: "Aditya Pulekar"

import node
class Stack:
    __slots__="top"

    def __init__(self):
        self.top = None

    def __str__(self):
        result="Stack ["
        n=self.top
        while(n!=None):
            result+=" "+str(n.data)
            n=n.link
        result+=" ]"
        return result

    def push(self,val):
        self.top=node.Node(val,self.top)

    def pop(self):
        self.top = self.top.link

    def isEmpty(self):
        return self.top == None

    def peek(self):
        assert not self.isEmpty(), "Peek on Empty Stack!"
        return self.top.data

    insert = push

    remove = pop

def test():
    s = Stack()
    print( s )
    for value in 1, 2, 3:
        s.push( value )
        print( s )
    print( "Popping:", s.peek() )
    s.pop()
    print( s )
    for value in 15, 16:
        s.insert( value )
        print( s )
    print( "Removing:", s.peek() )
    s.remove()
    print( s )
    while not s.isEmpty():
        print( "Popping:", s.peek() )
        s.pop()
        print( s )
    print( "Trying one too many pops... ", end="" )
    try:
        s.pop()     #The control transfers from this line to line 58 on trying to pop from an empty stack
        print( "Problem: it succeeded!" )
    except Exception as e:
        print( "Exception was " + str( e ) + "" )


if __name__ == "__main__":
    test()