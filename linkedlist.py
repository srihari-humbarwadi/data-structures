# Linked list implementation
# author Srihari Humbarwadi
# Date 13/06/2018


class node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtStart(self, data):
        self.size = self.size + 1
        newNode = node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertAtEnd(self, data):
        self.size = self.size + 1
        newNode = node(data)
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def traverse(self):
        if self.head is None:
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data + " ", end="")
            currentNode = currentNode.nextNode

    def remove(self, data):
        if self.head is None:
            return
        self.size = self.size - 1
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            currentNode.nextNode = self.head
        else:
            previousNode.nextNode = currentNode.nextNode

    def Size(self):
        return self.size


la = LinkedList()
la.insertAtStart(10)
la.insertAtStart(22)
la.Size()
la.insertAtEnd(1)
la.insertAtEnd(1220)
la.Size()
la.traverse()
la.remove(22)
la.traverse()
la.Size()

