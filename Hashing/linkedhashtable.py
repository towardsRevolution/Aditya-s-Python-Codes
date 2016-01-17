"""
This program builds a linked hash table
"""
__author__ = 'Aditya Pulekar'

import set
import collections.abc

class ChainNode( object ):
    __slots__ = 'obj','prev','link','chain'

    def __init__(self,obj,prev = None, link = None, chain = None):
        """
        Create a new chain node
        :param obj: object to be stored in the table
        :param prev: reference of the previous chain node (linked)
        :param link: reference of the next chain node (linked)
        :param chain: reference of the next chain node in the same hash slot
        :return:
        """
        self.obj = obj
        self.prev = prev
        self.link = link
        self.chain = chain

MIN_BUCKETS = 10
__abstractmethods__ = frozenset()

class LinkedHashTable (set.SetType,collections.abc.Iterable) :
        __slots__ = 'initial_num_buckets','load_limit','back','front','size','table'

        def __init__(self,initial_num_buckets=100,load_limit = 0.75):
            """
            Create a new empty hash table.
            :param initial_num_buckets: starting number_of_buckets
            :param load_limit: See class documentation above.
            :return:
            """
            self.initial_num_buckets = 10 if initial_num_buckets < MIN_BUCKETS else initial_num_buckets
            self.load_limit = load_limit
            self.table = [None for _ in range(self.initial_num_buckets)]
            self.size = 0
            self.front = None
            self.back = None

        def __iter__( self ):
            """
            Build an iterator.
            :return: an iterator for the current elements in the set
            """
            itr = self.front
            while itr != None:
                yield itr.obj
                itr = itr.link


        def add(self,obj):
            """
            Insert a new object into the hash table and remember when it was added
            relative to other calls to this method. However, if the object is
            added multiple times, the hash table is left unchanged, including the
            fact that this object's location in the insertion order does not change.
            Double the size of the table if its load_factor exceeds the load_limit.
            :param obj: the object to add
            :return: None
            """
            flag = 0
            #i.e. Table is empty
            #Note: We require the below "if" so that we can assign the "front" a reference
            if self.size == 0:    # [None for _ in range(self.initial_num_buckets)]
                index = self.hash_function(obj,self.initial_num_buckets)
                self.table[index] = ChainNode(obj)
                self.size += 1
                self.front = self.table[index]
                self.back = self.front
            else:
                #REHASH IF THE SIZE LIMIT HAS BEEN REACHED
                if (self.size // self.initial_num_buckets) > 0.75:
                    recordObj = [None for _ in range(self.size)]
                    count = 0
                    itr = self.front
                    while itr != None:
                        recordObj[count] = itr
                        count += 1
                        itr = itr.link
                    self.initial_num_buckets *= 2
                    newLinkedHashTable = LinkedHashTable( self.initial_num_buckets )
                    self = newLinkedHashTable
                    for index in recordObj:
                        self.add(index.obj)

                index = self.hash_function(obj,self.initial_num_buckets)

                #We also need to identify whether the incoming element is being added to the  hash table
                #or being linked. Bcoz it is only then that we will be able to decide whether the "chain" or "link"
                #or "prev" is to be assigned a reference

                #Since it is a hashTable entry, it will be next in order; So,we link and not chain

                if(self.table[index] == None):
                    self.table[index] = ChainNode(obj)
                    self.table[index].prev = self.back
                    self.size += 1

                    #***Note: If something is to be added in the chain, then it will be added at some point, else we
                    # should keep it "none"
                    self.back.link = self.table[index]
                    self.back = self.table[index]
                else:
                    #Chaining the elements in a slot of the hash table
                    #We iterate till the point we get none
                    forIter = self.table[index]
                    while forIter.chain != None:
                        #Note: We do not add an object if it has already been added once
                        if(forIter.chain.obj == obj):
                            flag = 1
                            break
                    if flag == 0 and not self.contains(obj):
                        temp = forIter
                        forIter.chain = ChainNode(obj)
                        self.size += 1
                        forIter.chain.prev = temp
                        self.back.link = forIter.chain
                        self.back = forIter.chain


        def contains(self,obj):
            """
            Is the given obj in the hash table?
            :return: True iff obj or its equivalent has been added to this table
            """
            flag = 0
            index = self.hash_function(obj,self.initial_num_buckets)
            if(self.table[index] == None):
                return False
            else:
                forIter = self.table[index]
                while forIter != None:
                    if forIter.obj == obj:
                        flag = 1
                        break
                    forIter = forIter.chain
                if flag == 1:
                    return True
                else:
                    return False


        def remove(self,obj):
            """
            Remove an object from the hash table (and from the insertion order).
            Resize the table if its size has dropped below
            (1-load_factor)*current_size.
            :param obj: the value to remove; assumes hashing and equality work
            :return:
            """
            #Resizing...
            if self.size < ( (1 - self.load_limit) * self.initial_num_buckets ):
                recordObj = [None for _ in range(self.size)]
                if self.size > 0:
                    count = 0
                    itr = self.front

                    #Now we will never get the error "list out of range" for recordObj[]
                    while itr != None and count < self.size:
                        recordObj[count] = itr
                        count += 1
                        itr = itr.link
                    self.initial_num_buckets //= 2
                    self.table = [None for _ in range(self.initial_num_buckets)]
                    self.size = 0
                    for index in recordObj:
                        self.add(index.obj)

            index = self.hash_function(obj,self.initial_num_buckets)
            if self.table[index] == None:
                print("Element doesn't exist in the table")

            elif self.table[index].obj == obj:
                #If the obj is not the first element of the linkedHashTable
                if self.table[index].prev != None:
                    self.table[index].prev.link = self.table[index].link
                    self.table[index] = self.table[index].chain
                    self.size -= 1
                #If the obj is the first element of the linkedHashTable
                else:
                    if self.table[index].prev == None and self.size == 1:
                        print("Hash table has been emptied!")
                        self.table[index] = None
                        self.front = None
                        self.size = 0
                    elif self.table[index].prev == None:
                        self.front = self.table[index].link
                        self.table[index] = self.table[index].chain
                        #i.e. the next "front" is in the same chain
                        if self.table[index] == self.front:
                            self.table[index].prev = None #Making it the "front"
                        else:
                            self.front.prev = None
                        #We will have a new front now

                        self.size -= 1
            else:
                #Now iterate through the hash chain to find the perfect match
                forIter = self.table[index]
                while forIter != None:
                    if forIter.chain != None and forIter.chain.obj == obj:
                        break
                    forIter = forIter.chain
                if forIter != None:
                    forIter.chain = forIter.chain.chain
                    self.size -= 1
                else:
                    print("Element doesn't exist in the table")


        def hash_function(self,value, n):
            """
            This function generates the hashCode for an object
            :param value: object reference
            :param n: number of buckets
            :return: index
            """
            hashCode = hash(value) % n
            return hashCode