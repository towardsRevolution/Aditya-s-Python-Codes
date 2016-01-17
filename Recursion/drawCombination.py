__author__ = 'Aditya Pulekar'
def drawCombination(n,k):
    if(k==0 or k==n or n==1):
        return 1
    else:
        y=drawCombination(n-1,k-1)+drawCombination(n-1,k)
        return y

def main():
    n=int(input("Enter the total number of objects: "))
    k=int(input("Enter the number of objects to be chosen: "))
    res=drawCombination(n,k)
    print("Result: ",res)
main()