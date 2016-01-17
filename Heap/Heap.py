__author__ = 'Aditya Pulekar'


class heap ( object ):
    __slots__ = 'data','id','fn','size'

    def __init__(self,fn,id):
        '''
        Constructor takes a comparison function.
        :param fn : It is a function that takes in two inputs and compares them for
        one element to be either greater or smaller than the other element
        '''
        self.size= 0
        self.fn= fn
        self.id=id
        self.data= []

    def __parent(self,loc):
        '''
        This function helps compute the parent location
        :param loc : a heap index
        :return: parent index
        '''
        return (loc-1)//2

    def __bubbleUp(self,loc):  #Note: While Bubbling-Up we require the location of the parent
        '''
        Restructures the heap property by moving the element at the
        given loc to the top of the heap
        :param loc : location from where the bubbling up begins
        '''
        if(self.id == "H"):
            while loc > 0 and self.fn(self.data[loc],self.data[self.__parent(loc)]):
                self.data[loc].Hindex , self.data[self.__parent(loc)].Hindex = self.data[self.__parent(loc)].Hindex , self.data[loc].Hindex
                (self.data[loc], self.data[self.__parent(loc)]) = (self.data[self.__parent(loc)], self.data[loc])
                loc = self.__parent(loc)
        else:
            while loc > 0 and self.fn(self.data[loc],self.data[self.__parent(loc)]):
                self.data[loc].Cindex , self.data[self.__parent(loc)].Cindex = self.data[self.__parent(loc)].Cindex , self.data[loc].Cindex
                (self.data[loc], self.data[self.__parent(loc)]) = (self.data[self.__parent(loc)], self.data[loc])
                loc = self.__parent(loc)

    def __bubbleDown(self,loc):
        '''
        Restructures the heap property by bubbling down the element at top of the heap as far
        down the heap as possible
        :param loc : a location to start bubbling down from
        '''
        swapLoc =  self.__smallest(loc)

        #No swapping will happen if "swapLoc == loc"
        if(len(self.data)>1):
            while swapLoc != loc:
                if(self.id == "H"):
                    (self.data[loc].Hindex, self.data[swapLoc].Hindex) = (self.data[swapLoc].Hindex, self.data[loc].Hindex)
                    (self.data[loc], self.data[swapLoc]) = (self.data[swapLoc], self.data[loc])
                else:
                    (self.data[loc].Cindex, self.data[swapLoc].Cindex) = (self.data[swapLoc].Cindex, self.data[loc].Cindex)
                    (self.data[loc], self.data[swapLoc]) = (self.data[swapLoc], self.data[loc])
                loc = swapLoc
                swapLoc = self.__smallest(loc)
        else:
            if(self.id == "H"):
                self.data[loc].Hindex = self.size - 1
            else:
                self.data[loc].Cindex = self.size - 1


    def __smallest(self,loc):
        '''
        This function finds the smallest value between the loc and its two children
        :param loc: current location on the heap
        :return: the index of the smallest value found
        '''
        ch1= loc*2 + 1
        ch2= loc*2 + 2
        if(ch1 >= self.size): #Becoz there is just a single element
            return loc
        if(ch2 >= self.size): #If there are only 2 elements @ loc 0 and 1
            if(self.fn(self.data[loc],self.data[ch1])):
                return loc
            else:
                return ch1  #Basically saying that a swap is required

        #The parent should be smaller than one of the children
        if(self.fn(self.data[ch1],self.data[ch2])):

            #Since element at ch2 is greater, the heap just needs to ensure that the element at loc
            #is smaller than element at ch1
            if(self.fn(self.data[loc],self.data[ch1])):
                return loc   #No swap required
            else:
                return ch1   #swap required
        else:
            #Since element at ch1 is greater, the heap just needs to ensure that the element at loc
            #is smaller than element at ch2
            if(self.fn(self.data[loc],self.data[ch2])):
                return loc
            else:
                return ch2

    def insert(self,item):
        '''
        Inserts an item into the heap.
        :param item: Item to be inserted
        '''
        if(self.id == "H"):
            item.Hindex = self.size
        else:
            item.Cindex = self.size
        self.data.append(item)
        self.size += 1
        self.__bubbleUp(self.size-1)


    def pop(self):
        '''
        Pops the top element of the heap
        :return: top element of the heap
        '''

        if(self.size == 0):
            print ("\nNo more jobs left to be executed by Harold and Cathy!")
        else:
            retJob= self.data[0]
            self.size -= 1
            if self.size > 0:
               self.data[0] = self.data.pop(self.size)  #Inserting the last element in teh list in the first location and bubbling the list down
               self.__bubbleDown(0)
            else:
                self.data=[]
            return retJob

    def __str__(self):
        retstr = ""
        if(self.size==0):
            print("No more jobs on the heap!")
        for item in range(self.size):
            retstr += str(self.data[item].name) + " " + str(self.data[item].time) + " " + str(self.data[item].cost) + \
                   " " + str(self.data[item].Cindex) + " " + str(self.data[item].Hindex) + "\n"
        return retstr

