
class Queue:
    def __init__(self, queue = []):
        self.queue = queue

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue[0]

    def printQueue(self):
        for i in range(0, len(self.queue)):
            print(self.queue[i])


students = Queue()

students.enqueue("Annabelle")
students.enqueue("Rose")
students.enqueue("Annie")
students.enqueue("Joe")

students.printQueue()

print(students.dequeue())