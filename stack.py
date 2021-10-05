
class Stacks:
    def __init__(self, stack = []):
        self.stack = stack
        
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        print(self.stack[0])
        self.stack.remove(self.stack[0])
        

    def printStack(self):
        for i in range(0, len(self.stack)):
            print(self.stack[i], end=" ")
        

foods = Stacks()

foods.push("Fish")
foods.push("pork")
foods.push("chicken")

foods.printStack()
print("\n")
foods.pop()
foods.printStack()
print("\n")
foods.pop()
foods.printStack()
print("\n")
foods.pop()