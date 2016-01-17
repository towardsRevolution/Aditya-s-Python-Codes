__author__ = 'Addy'

def SelectionS(vals):
    #Selection sort (Just the way we would sort the numbers...i.e by choosing the smallest and placing it first)
    for finger in range(len(vals)-1):
        smallest=finger
        for index in range(finger+1,len(vals)):
            if(vals[smallest]>vals[index]):
                smallest=index
        vals[smallest],vals[finger]=vals[finger],vals[smallest]

def bubbleSort(nums):
    for passSort in range(len(nums)-1): #Note: This for loop is only for the passes
        for itr in range(len(nums)-passSort-1):
            if(nums[itr]>nums[itr+1]):
                nums[itr],nums[itr+1]=nums[itr+1],nums[itr]


def insertionSort(nums):
    for outer in range(len(nums)):
        inner=outer
        while(inner>0 and nums[inner]<nums[inner-1]):
            nums[inner],nums[inner-1]=nums[inner-1],nums[inner]
            inner=inner-1

def Merge(L,R,A):
    nL=len(L)
    nR=len(R)
    i=j=k=0
    while(i<nL and j<nR):
        if(L[i]<R[j]):
            A[k]=L[i]
            i=i+1
            k=k+1
        else:
            A[k]=R[j]
            j=j+1
            k=k+1
    #When either one of the two lists being merged reaches limit, we put the items in the other list into A, one-by-one
    while(i<nL):
        A[k]=L[i]
        k=k+1
        i=i+1
    while(j<nR):
        A[k]=R[j]
        k=k+1
        j=j+1

def MergeSort(nums):
    n=len(nums)
    if(n<2):
        return
    mid=int(n/2)
    left=nums[:mid]
    right=nums[mid:]
    #NOTE: left and right are slices
    MergeSort(left)
    MergeSort(right)
    Merge(left,right,nums)

def main():
    numbers=[23,12,11,45,67,89,30]
    print(numbers)
    nums=numbers
    SelectionS(nums)
    print("SelectionSort: ",nums)
    bubbleSort(nums)
    print("BubbleSort: ",nums)
    insertionSort(nums)
    print("InsertionSort: ",nums)
    MergeSort(nums)
    print("MergeSort: ",nums)


main()