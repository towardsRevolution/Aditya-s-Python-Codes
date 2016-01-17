__author__ = 'Addy'
import node

class queue:
    __slots__="head","tail"

    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        result="Queue ["
        n=self.head
        while(n!=None):
            result += " " + str(n.data)
            n=n.link
        result+=" ]"
        return result

    def isEmpty(self):
        return self.head == None

    def enqueue(self,val):
        newNode = node.Node(val,None)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.link = newNode
        self.tail = newNode

    def dequeue(self):
        self.head=self.head.link

    remove = dequeue
    insert = enqueue

    def peek(self):
        assert not self.isEmpty(), "peek on empty queue"
        return self.head.data

def test():
    s = queue()
    print( s )
    for value in 1, 2, 3:
        s.enqueue( value )
        print( s )
    print( "Dequeueing:", s.peek() )
    s.dequeue()
    print( s )
    for value in 15, 16:
        s.insert( value )
        print( s )
    print( "Removing:", s.peek() )
    s.remove()
    print( s )
    while not s.isEmpty():
        print( "Dequeueing:", s.peek() )
        s.dequeue()
        print( s )
    print( "Trying one too many dequeues... ", end="" )
    try:
        s.dequeue()
        print( "Problem: it succeeded!" )
    except Exception as e:
        print( "Exception was '" + str( e ) + "'" )


if __name__ == "__main__":
    test()