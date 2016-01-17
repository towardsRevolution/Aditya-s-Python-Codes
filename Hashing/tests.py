""" 
file: tests.py
description: Verify the LinkedHashTable class implementation
"""

__author__ = "Aditya Pulekar" 

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    if a_set.size == 0:
        print ("Table is now empty!")
    for word in a_set: # uses the iter method
        print( word, end=" " )
    print()

def test0():
    #To test the resizing capacity of the table
    print("\n**********************************TEST CASE 1")
    table = LinkedHashTable( 16 )
    table.add( "Hello" )
    table.add( "Addy" )
    table.add( "Maddy" )
    table.add( "Paddy" )
    print( "\nInitial Table: ",end='')
    print_set(table )
    print( "Initial number of buckets: ",table.initial_num_buckets )

    print("\nRemoving 'Addy'...")
    table.remove("Addy")
    print( "Updated Table: ",end='')
    print_set( table )
    print( "Number of buckets after removing 'Addy': ",table.initial_num_buckets )

    print("\nRemoving 'Hello'...")
    table.remove( "Hello" )
    print( "Updated Table: ",end='')
    print_set( table )
    print( "Number of buckets after resizing: ",table.initial_num_buckets )

    print("\nRemoving 'Maddy'...")
    table.remove( "Maddy" )
    print( "Updated table after removing 'Maddy': ", end='' )
    print_set( table )


    #To test the ability of the table to avoid duplicity of objects being added
    print("\n**********************************TEST CASE 2")
    table = LinkedHashTable ( 100 )
    print("Adding 'to','do', 'is', 'to', 'be'.....")
    table.add( "to" )
    table.add( "do" )
    table.add( "is" )
    table.add( "to" )
    table.add( "be" )

    print("Adding 'to' two more times...")
    table.add( "to" )
    table.add( "to" )
    print( "\nInitial Table: ",end='')
    print_set( table )

    print( "'to' in table?", table.contains( "to" ) )
    print("Removing 'to'...")
    table.remove("to")
    print( "'to' in table?", table.contains( "to" ) )
    print( "Updated Table on removing 'to': ",end='')
    print_set(table)
    print("\nAdding 'Hello' and 'play'..")
    table.add("Hello")
    table.add("play")
    print( "Updated Table on adding 'Hello' and 'play': ",end='')
    print_set(table)
    print("\nRemoving 'Hello' and 'be'...")
    table.remove("Hello")
    table.remove("be")
    print( "Updated Table on removing 'Hello' and 'be': ",end='')
    print_set( table )


    #Class example (to test add(), remove() and contains() test thoroughly)
    #QUESTION: WHY DOES THE EXECUTION OF THIS FILE HALT AT THE BELOW LINE AT TIMES?
    print("\n**********************************TEST CASE 3")
    table = LinkedHashTable( 10 )
    table.add( "batman" )
    table.add( "has" )
    table.add( "lots" )
    table.add( "of" )
    table.add( "gizmos" )
    table.add( "on" )
    table.add( "his" )
    table.add( "belt" )
    print( "\nInitial Table: ",end='')
    print_set( table )

    print( "'gizmos' in table?", table.contains( "gizmos" ) )
    print( "'batman' in table?", table.contains( "batman" ) )
    print( "'has' in table?", table.contains( "has" ) )
    print("\nRemoving 'batman','of','on','belt','has','lots','gizmos' from the table...")
    table.remove( "batman" )
    table.remove( "has" )
    table.remove( "lots" )
    table.remove( "of" )
    table.remove( "gizmos" )
    table.remove( "belt" )
    print("Table size when two elements remain...: ", table.size)
    print("\nRemoving 'on'..")
    table.remove( "on" )
    print("\nUpdated Table after removing 'on' : ", end='')
    print_set( table )
    print("table.front.obj: ",table.front.obj)
    print("Table size when one element remain...: ", table.size)
    print("\nRemoving 'his'..")
    table.remove( "his" )
    print("\nUpdated Table after removing 'batman','of','on','belt','has','lots','gizmos' : ", end='')
    if table.size == 0:
        print ("No more objects in the hash table!")
    else:
            print_set( table )

if __name__ == '__main__':
    test0()

