
from typing import Counter


class Node:

    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class doublyLink:

    def __init__(self, head = None):
        self.head = head

    def addValue(self, value):
        
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                node.prev = currentNode
                break
            currentNode = currentNode.next

    def insert(self, index, value):
        currentNode = self.head
        node = Node(value)

        for _ in range(0, index-1):
            currentNode = currentNode.next
        nextNode = currentNode.next
        node.next = nextNode
        nextNode.prev = node
        node.prev = currentNode
        currentNode.next = node
        
        

    def printOut(self):
        
        currentNode = self.head
        print("Head = ", currentNode.value, "\n")
        tail = None
        print("None <->", end=" ")
        while currentNode is not None:
            print(currentNode.value, "<->", end=" ")
            if currentNode.next is None:
                tail = currentNode.value
            currentNode = currentNode.next
        print("None \n")

        print("Tail = ", tail)
                
b = doublyLink()
b.addValue("a")
b.addValue("b")
b.addValue("c")
b.addValue("d")

b.insert(1, "G")

b.printOut()
