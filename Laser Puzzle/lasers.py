"""
This program designs a laser puzzle. It gives the user the best possible laser placements by
analyzing the laser grid.
"""
__author__ = 'Aditya Pulekar'
__author__ = 'Mandar Badave'

#Importing the python file with the sorting code from the same package
import SelectionSort


def traverseGrid(grid):
    """
    Takes a List containing the grid of numbers, performs the addition of three numbers oriented either vertically
    or horizontally , selects the orientation with the maximum score, sorts the list of the best scores and their
    respective orientations at every probable laser position on the grid and returns the sorted list
    :param grid (list): a list containing a grid of numbers
    :return: sorted list of best scores, their respective orientations and respective coordinates
    """

    #Initialising the lists
    ScorePositionOrientation=[]

    for row in range(len(grid)):                #Row length
        for column in range(len(grid[0])):      #Column length

            if((row==0 and column==0) or (row==0 and column==len(grid[0])-1) or (row==(len(grid)-1) and
                                                column==(len(grid[0])-1)) or (row==len(grid)-1 and column==0)):
                print("\nCorner position of the grid: ","(",row,",",column,")",". Not to be taken into account")
            else:
                if((row+1)==len(grid)):
                    score=int(grid[row][column-1])+int(grid[row][column+1])+int(grid[row-1][column])
                    orientation="facing North"

                elif(((column-1)<0)):
                    score=int(grid[row-1][column])+int(grid[row+1][column])+int(grid[row][column+1])
                    orientation="facing East"

                elif(((column+1)==len(grid[0]))):
                    score=int(grid[row-1][column])+int(grid[row+1][column])+int(grid[row][column-1])
                    orientation="facing West"

                elif(((row-1)<0)):
                    score=int(grid[row][column-1])+int(grid[row][column+1])+int(grid[row+1][column])
                    orientation="facing South"

                else:
                    EveryOrientationScoreForMax=[]
                    EveryOrientationScoreForMax.append([int(grid[row-1][column])+int(grid[row+1][column])+
                                                        int(grid[row][column+1]),"facing East"])
                    EveryOrientationScoreForMax.append([int(grid[row-1][column])+int(grid[row+1][column])+
                                                        int(grid[row][column-1]),"facing West"])
                    EveryOrientationScoreForMax.append([int(grid[row][column-1])+int(grid[row][column+1])+
                                                        int(grid[row-1][column]),"facing North"])
                    EveryOrientationScoreForMax.append([int(grid[row][column-1])+int(grid[row][column+1])+
                                                        int(grid[row+1][column]),"facing South"])
                    ScoreAndOrientation=max(EveryOrientationScoreForMax)
                    orientation=ScoreAndOrientation[1]
                    score=ScoreAndOrientation[0]

                ScorePositionOrientation.append([score,(row,column),orientation])

    #Selection sort applied to sort the list 'ScorePositionOrientation'
    SortedScorePositionOrientation=SelectionSort.SortList(ScorePositionOrientation)

    return ScorePositionOrientation


def main():
    """
    The main prompts the user to input the file name containing the grid of numbers and
    the number of lasers to be placed. It then converts the grid obtained from the file
    into a 2D list and passes it to traverseGrid() function for evaluation of the best
    possible laser positions

    :return: None
    """
    filename=input('Enter the filename containing the grid: ')

    #There are 12 possible laser placements in a 4x4 laser grid. For a matrix of higher dimensions
    #you may choose a max value greater than 12
    noOfLasers= int(input('Enter the number of lasers to be placed (choose a value between [1,12]): '))

    #Initialising the list
    grid=[]

    try:
        with open(filename) as f:
            for line in f:
                #removes the new line character from the line
                line=line.strip()

                #Splits a single line from the input file into a list on encountering a space
                line=line.split(' ')

                #Appends the list formed on splitting a single line to the list 'grid'
                counter=0
                # gridIndividualLine=[]
                # while(counter<len(line)):
                #     gridIndividualLine.append(line[counter])
                #     counter=counter+1
                grid.append(line)

    except FileNotFoundError as e:
            print(e)

    #The sorted list of best scores, their respective orientations and their positions is
    # returned and stored in the list 'IdealLaserPlacements'
    IdealLaserPlacements=traverseGrid(grid)
    BestPositions=len(IdealLaserPlacements)-1
    count=0
    print("\nThe best possible laser positions for the given grid: ")

    #Prints as many best possible laser positions as prompted by the user (at the beginning)
    while(count<noOfLasers):
        print(IdealLaserPlacements[BestPositions][1],IdealLaserPlacements[BestPositions][2])
        BestPositions=BestPositions-1
        count=count+1

main()