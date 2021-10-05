

class Node:

    def __init__(self, val, next = None):
        self.value = val
        self.next = next

class linkedList:

    def __init__(self, head=None):
        self.head = head

    def addValue(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        
        currentNode  = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break 
            currentNode = currentNode.next

    def listSize(self):
        currentNode = self.head
        size = 0
        while currentNode.next is not None:
            size+=1
            currentNode = currentNode.next
        return size

    def index(self, indexValue):
        currentNode = self.head
        currentIndex = 0
        while currentNode.next is not None:
            if indexValue == currentIndex:
                return currentNode.value
            currentIndex+=1
            currentNode = currentNode.next

    #Add head and tail specification of insertion
    def insert(self, ind, val):
        currentNode = self.head
        
        node = Node(val)
        for i in range(0, ind-1):
            currentNode = currentNode.next
        node.next = currentNode.next
        currentNode.next = node

    #Fix deletion method...
    def delete(self, ind):
        currentNode = self.head

        for _ in range(0, ind-1):
            currentNode = currentNode.next
        toDelete = currentNode.next
        currentNode = toDelete.next
        del toDelete    
    

    # 1 -> 2 -> 3 -> 4 -> None
    # 4 -> 3 -> 2 -> 1 -> None
    def reverse(self):
        pass

    def sort(self):
        pass
                
    def printOut(self):
        
        currentNode = self.head
        print("Head = ", currentNode.value, "\n")
        tail = None
        while currentNode is not None:
            print(currentNode.value, "->", end=" ")
            if currentNode.next is None:
                tail = currentNode.value
            currentNode = currentNode.next
        print("None \n")
        print("Tail = ", tail)
       
            
            

            

a = linkedList()

a.addValue(1)
a.addValue(2)
a.addValue(3)
a.addValue(4)

a.addValue(8)
a.insert(2, 20)

a.delete(3)
a.reverse()
a.printOut()