"""
taskmaster.py

Demonstrate stack- or queue-based task lists.
author: James Heliotis
author: Aditya Pulekar
"""

# Uncomment exactly one of the next two lines. Don't change anything else.

# from stack import Stack as Dispenser
#from queue import Queue as Dispenser
#import queue
import prioqueue

class Task:
    __slots__ = "time_left", "name", "time"

    def __init__( self, name, time ):
        self.time_left = time
        self.name = name
        self.time = time


#Ordering the priority queue using execution time, giving
#priority to the task with the smallest execution time
def after(v,u):
    return v.time_left>u.time_left

#The after() function below can be used if we wish to order the tasks lexico-
#graphically (as per their names)

# def after(v,u):
#     return v.name>u.name

TICK_CMD = "tick"
ADD_CMD = "add"
QUIT_CMD = "quit"
COMMANDS = ( TICK_CMD, ADD_CMD, QUIT_CMD )

def main():
    tasks = prioqueue.priorityQ(after)
    time = 0

    cmd, args = get_cmd( COMMANDS )
    while cmd != QUIT_CMD:
        if cmd == TICK_CMD:
            time += 1
            if not tasks.isEmpty():
                current = tasks.peek()
                current.time_left -= 1
                if current.time_left == 0:
                    print( "\nTask '" + current.name + \
                           "' completed at time " + str( time ) + "." )
                    tasks.remove()
                    if not tasks.isEmpty():
                        print( "New task is '" + tasks.peek().name + "'." )
                    else:
                        print( "Nothing else to do." )
            else:
                print( "Nothing to do." )
        elif cmd == ADD_CMD:
            new_task = Task( args[ 0 ],int(args[ 1 ] ) ) # We will always require args[1] to be int
                                                         # since we need to tick for time
            tasks.insert( new_task )
            print( "\nAdded. Current task is '" + tasks.peek().name + \
                   "'." )
        else:
            assert True, "PROGRAM ERROR"
        cmd, args = get_cmd( COMMANDS )

    print( "\nTerminating the simulation." )

def get_cmd( choices ):
    line = input( "\nEnter one of " + str( choices ) + ": " ).split()
    cmd = line.pop( 0 )
    while cmd not in choices:
        print( "\n'" + cmd + "' is not a legal command. Try again." )
        line = input( "\nEnter one of " + str( choices ) + ": " ).split()
        cmd = line.pop( 0 )
    return cmd, line

if __name__ == "__main__":
    main()
