"""
This program performs the selection sort. It is a modified version of the
selection sort program we had implemented in the lecture and has been
implemented from scratch by us
"""
__author__ = 'Aditya Pulekar'


def SortList(toSort):
    """
    Performs the selection sort
    :param toSort (list): a 2D list containing scores, coordinates of the puzzle and the respective
                          orientations
    :return: sorted list of best scores, their respective orientations and respective coordinates
    """

    for iterator in range(len(toSort)-1):
        smallestInt=iterator

        #The inner 'for' loop searches for the smallest integer in the first location of every list
        #and notes its index in the variable 'smallest'
        for searchSmallest in range(iterator+1,len(toSort)):
            if(toSort[searchSmallest]<toSort[smallestInt]):
                smallestInt=searchSmallest

        #Swap operation
        toSort[smallestInt],toSort[iterator]=toSort[iterator],toSort[smallestInt]
    return toSort
