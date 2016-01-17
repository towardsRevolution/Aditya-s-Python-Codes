"""
This program schedules the jobs for execution by Harold and Cathy
using heaps
"""

__author__ = 'Aditya Pulekar'
__author__ = 'Mandar Badave'

import Heap

"""
Class to schedule jobs and get them executed using heaps
"""
class jobsDone:
    __slots__ = "name","cost","time","Cindex","Hindex"

    def __init__(self,line,Cindex=0,Hindex=0):
        self.name = line[0]
        self.cost = line[2]
        self.time = line[1]
        self.Cindex = Cindex
        self.Hindex = Hindex

def main():
    H= Heap.heap(lambda x,y: int(x.time) <= int(y.time),"H") #Creating a min heap for Harold
    C= Heap.heap(lambda x,y: int(x.cost) >= int(y.cost),"C") #Creating a max heap for Cathy
    filename = input('Enter the filename: ')
    print("\n")
    try:
        with open(filename) as f:
            for line in f:
                line=line.strip()
                line=line.split()
                if len(line) > 2:
                    newJob=jobsDone(line)
                    print('New Job arriving! Job Name:  ',line[0],line[1],line[2])
                    H.insert(newJob)
                    C.insert(newJob)
                else:
                    if(line[0] == "Cathy"):
                        job=C.pop()
                        if(job is not None):
                            print('Cathy starting job: ',job.name)
                            H.data[0],H.data[job.Hindex] = H.data[job.Hindex],H.data[0]
                            haroldRemovesjob= H.pop()
                            # print("Cathy's Heap: ", C)
                            # print("Harold's Heap after popping: ", H)
                    else:
                        job=H.pop()
                        if(job is not None):
                            print('Harold starting job: ',job.name)
                            C.data[0],C.data[job.Cindex] = C.data[job.Cindex],C.data[0]
                            cathyRemovesjob= C.pop()
                            # print("Cathy's Heap: ", C)
                            # print("Harold's Heap after popping: ", H)

    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()