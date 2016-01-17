"""
This class prioritizes the data in the fashion the user wants it to be.
A priority queue is implemented for task scheduling along with its own
test program.

__author__ = 'Aditya Pulekar'

"""

"""
Class for the generation of a node
"""
class node:
    __slots__='data', 'link'

    def __init__(self,data,link):
        """
        Create a new node
        param name: name of the node
        param link: reference of the next node
        """
        self.data = data
        self.link = link

    def __str__(self):
        """
        Return a string representation of the contents of
        a node.
        """
        task = str(self.data)+" "
        return task

"""
Class to design the priority queue
"""
class priorityQ:
    __slots__='afterQ','head','tail'    #

    def __init__(self,after): #
        """
        Initialize a new empty priority queue.
        :param after: an ordering function. See definition of dequeue method.
        :return: None (constructor)
        """
        self.head=None
        self.tail=None
        self.afterQ=after

    def isEmpty(self):
        """
        :return: True iff there are no elements in the queue.
        """
        if(self.head==None):
            return True
        else:
            return False

    def __str__(self):
        """
        :return: Return a string representation of the contents of
        this priority queue, front value first.
        """
        concatRes="["
        p=self.head
        while(p!=None):
            concatRes+=" "+ str(p.data) #+ str(p.time)
            p=p.link
        concatRes+=" ]"
        return concatRes


    def enqueue(self,newValue):
        """
        Enter a new value into the queue.
        :param newValue: the value to be entered into the queue
        :return: None
        """
        ptr=self.head

        #If the queue is empty
        if(self.head==None):
            #newnode= node(newValue.name,newValue.time,None)
            newnode= node(newValue,None)
            self.head=newnode
            self.tail=newnode

        #If there is only one element on the queue and one value is being added
        elif(self.afterQ(self.head.data,newValue)):
                newnode=node(newValue,ptr)
                self.head=newnode

        else:
            #If two elements are having the same value then they will be ordered
            #as per their sequence of arrival (i.e. the element to have spent the
            #longest time inside the queue will be dequeued first). This case is
            #covered in this "else"

            while(ptr!=None):
                if(not self.afterQ(ptr.data,newValue)):
                    previous=ptr
                    ptr=ptr.link
                    nextE = ptr
                else:
                    break
            #There are two possibilities due to which the while loop may break:-

            #If 'ptr' had reached None
            # Task being added at the tails
            if(ptr==None):
                previous.link=node(newValue,None)
                self.tail=previous.link

            #If the execution time of the new task was more than the execution time of
            #all the tasks existing within the queue
            #This "else" considers the fact that the while loop was broken since
            #"Self.head.data" had a greater value than newValue
            else:
                newnode = node(newValue,ptr)
                previous.link = newnode

    """
    insert() function will perform the exact same operation as the enqueue function
    after making the below assignment.
    """
    insert=enqueue

    def dequeue(self):
        """
        Remove one of the values v from the queue such that,
        for all values u in the queue, after(v,u) is False.
        If more than one value satisfies the requirement,
        the value chosen should be the one that has
        been in the queue the longest.
        :pre: not isEmpty()
        :return: None
        """
        if(self.isEmpty()):
            print("Trying to dequeue from an empty queue!")
        else:
            self.head=self.head.link

    def peek(self):
        """
        Find in the queue the value that would be removed were the dequeue
        method to be called at this time.
        :pre: not isEmpty()
        :return: the value described above
        """
        assert not self.isEmpty(),"Empty Queue!"   #What does this mean
        return self.head.data

    """
    remove() function will perform the exact same operation as the dequeue() function
    after making the below assignment.
    """
    remove = dequeue

    """
    This function has been defined for testing the priority queue.
    When we run the taskMaster, the after() function from the
    taskMaster will be passed to the priority queue, which then,
    will use it to order its enqueue operation
    """
    def TestAfter(v,u):
        """
        Returns the result of the comparison between the value of
        the element in the queue and the value of the element to be
        enqueued in terms of a boolean value

        :param v: value of the element in the queue
        :param u: value of the element to be enqueued
        :return: result of the comparison btween v and u
        """
        return v>u

    # The TestAfter() function below can be used to compare strings on the basis
    # their lengths

    # def TestAfter(v,u):
    #     return len(v)>len(u)

#TEST PROGRAM FOR PRIORITY QUEUE

def main():
    """
    Test Program
    :return:  None (main)
    """


    q=priorityQ(priorityQ.TestAfter)

    #Arrangement of data in ascending order (with the data at the head of the
    #priority queue with the smallest value)
    print('Integers being enqueued (in ascending order)...')
    print('Inserting 5 elements into the queue...')
    q.insert(1)
    q.insert(21)
    q.insert(3)
    q.insert(18)
    q.insert(18)
    q.insert(10)
    q.insert(2)
    q.insert(11)
    print("Queue: ",q)
    print('Removing two elements...')
    q.remove()
    q.remove()
    print("Queue: ",q)
    print('Inserting 1 element...')
    q.insert(24)
    print("Queue: ",q)
    print("Next Integer to be dequeued--> ",q.peek())
    print("Is the queue empty? ",q.isEmpty())
    print('Removing all the remaining elements....')
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
    print("Is the queue empty? ",q.isEmpty())
    print('Now, the queue is empty...try doing a dequeue operation')
    q.dequeue()

    #Lexicographic arrangement of strings being enqueued
    print('\n\nStrings being enqueued (lexicographically)....')
    q1=priorityQ(priorityQ.TestAfter)
    print('Inserting 3 elements into the queue...')
    q1.insert("Aditya")
    q1.insert("Shekhar")
    q1.insert("Madhavi")
    print("Queue: ",q1)
    print('Removing 1 element...')
    q1.remove()
    print("Queue: ",q1)
    print("Next string to be dequeued--> ",q1.peek())
    print('Inserting 3 elements into the queue...')
    q1.insert("Abigail")
    q1.insert("Ravi")
    q1.insert("Zebra")
    print("Queue: ",q1)
    print("Next string to be dequeued--> ",q1.peek())
    print('Removing 1 element...')
    q1.remove()
    print("Queue: ",q1)
    print("Is the queue empty? ",q.isEmpty())
    print('Removing all the remaining elements....')
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    print(q1)
    print("Is the queue empty? ",q1.isEmpty())
    print('Now, the queue is empty...try doing a dequeue operation')
    q1.dequeue()

if __name__ == "__main__":
    main()

