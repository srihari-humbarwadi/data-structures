# Binary Search Trees implementation
# author Srihari Humbarwadi
# Date 22/06/2018


class Node(object):
    def __init__(self, data):
        self.data = data
        self.LeftChild = None
        self.RightChild = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertnode(data, self.root)

    def insertnode(self, data, node):
        if data < node.data:
            if node.LeftChild:
                self.insertnode(data, node.LeftChild)
            else:
                node.LeftChild = Node(data)
        elif data > node.data:
            if node.RightChild:
                self.insertnode(data, node.RightChild)
            else:
                node.RightChild = Node(data)

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.RightChild:
            return self.getMax(node.RightChild)
        return node.data

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.LeftChild:
            return self.getMin(node.LeftChild)
        return node.data

    def getInorder(self):
        if self.root:
            return self.traverseInorder(self.root)

    def traverseInorder(self, node):
        if node.LeftChild:
            self.traverseInorder(node.LeftChild)
        print(node.data, "", end="")
        if node.RightChild:
            self.traverseInorder(node.RightChild)

    def remove(self, data):
        if self.root:
            self.root = self.removenode(data, self.root)

    def removenode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.LeftChild = self.removenode(data, node.LeftChild)
        elif data > node.data:
            node.RightChild = self.removenode(data, node.RightChild)
        else:
            if not node.LeftChild and not node.RightChild:
                del node
                return None
            if not node.LeftChild:
                tempNode = node.RightChild
                del node
                return tempNode
            elif not node.RightChild:
                tempNode = node.LeftChild
                del node
                return tempNode
            predecsTempNode = self.getPredecessor(node.LeftChild)
            node.data = predecsTempNode.data
            node.LeftChild = self.removenode(predecsTempNode.data, node.LeftChild)
        return node

    def getPredecessor(self, node):
        if node.RightChild:
            return self.getPredecessor(node.RightChild)
        return node


bst = BST()
bst.insert(10)
bst.insert(2)
bst.insert(7)
bst.insert(15)
bst.insert(1)
bst.insert(30)
bst.insert(12)
bst.insert(6)
print(bst.getMaxValue())
print(bst.getMinValue())
bst.getInorder()
bst.remove(10)
bst.getInorder()

