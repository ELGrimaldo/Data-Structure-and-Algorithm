import time

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Circularlink:

    def __init__(self, head = None):
        self.head = head
    
    def addValue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        currentNode = self.head
        while True:
            if currentNode.next == self.head:
                currentNode.next = node
                node.next = self.head
                break
            currentNode =currentNode.next 

    def printOut(self):
        
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.next
            time.sleep(1)

c = Circularlink()

c.addValue("as")
c.addValue("nf")
c.addValue("cj")
c.addValue("xn")

c.printOut()
