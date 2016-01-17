__author__ = 'Aditya Pulekar'

#In total 4 recursive calls
def listSum (aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return aList[0] + listSum(aList[1:])

def main():
    list = [12,34,11,10,23]
    tot = listSum(list)
    print("Summation of all the digits: ",tot)

if __name__ == '__main__':
    main()