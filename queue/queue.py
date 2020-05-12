from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class QueueWithList:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def __str__(self):
        return f"{self.storage}"

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.remove_from_tail()


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.dequeue()

