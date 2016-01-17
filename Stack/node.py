__author__: "Aditya Pulekar"

class Node:
    __slots__="data","link"

    def __init__(self,data,link):
        self.data=data
        self.link=link

    def __str__(self):
        return self.data
