
from BTNode2 import BTNode

class BST (object):
    __slots__ = 'root', 'size'

    def __init__(self):
        self.root = None
        self.size = 0

    def __size(self,node):
        if node == None:
            return 0
        else:
            return 1 + self.__size(node.left) + self.__size(node.right)

    def sizeOfTree(self):
        if self.root == None:
            return 0
        else:
            return self.__size(self.root)

    def __height(self,node):
        if node == None:
            return -1
        else:
            return 1 + max(self.__height(node.left), self.__height(node.right))

    def height(self):
        return self.__height(self.root)

    def __contains(self,node,val):
        if node == None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self.__contains(node.left,val)
        else:
            return self.__contains(node.right,val)

    def contains(self,val):
        return self.__contains(self.root,val)

    def __insert(self,node,val):
        if val <= node.val:
            if node.left == None:
                node.left = BTNode(val)
            else:
                self.__insert(node.left,val)
        else:
            if node.right == None:
                node.right = BTNode(val)
            else:
                self.__insert(node.right,val)

    def insert(self,val):
        if self.root == None:
            self.root = BTNode(val)
        else:
            self.__insert(self.root,val)
        self.size += 1

    def __inorder(self,node):
        if node == None:
            return ""
        else:
            return self.__inorder(node.left) + " " + str(node.val) + self.__inorder(node.right)

    def __str__(self):
        return self.__inorder(self.root)

def main():
    """
    Test function
    :return: None
    """
    t0 = BST()
    print('t0:', t0)
    print('t0 size (0):', t0.size)
    print('t0 contains 10 (False)?', t0.contains(10))
    print('t0 height (-1)?', t0.height())

    t1 = BST()
    t1.insert(10)
    print('t1:', t1)
    print('t1 size (1):', t1.size)
    print('t1 contains 10 (True)?', t1.contains(10))
    print('t1 contains 0 (False)?', t1.contains(0))
    print('t1 height (0)?', t1.height())

    t2 = BST()
    for val in (20, 10, 30): t2.insert(val)
    print('t2:', t2)
    print('t2 size (3):', t2.size)
    print('t2 contains 30 (True)?', t2.contains(30))
    print('t2 contains 0 (False)?', t2.contains(0))
    print('t2 height (1)?', t2.height())

    t3 = BST()
    for val in (17, 5, 35, 2, 16, 29, 38, 19, 33): t3.insert(val)
    print('t3:', t3)
    print('t3 size (9):', t3.size)
    print('t3 contains 16 (True)?', t3.contains(16))
    print('t3 contains 0 (False)?', t3.contains(0))
    print('t3 height (3)?', t3.height())

if __name__ == '__main__':
    main()