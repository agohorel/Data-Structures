class Node:
    def __init__(self, data = None):
        self.value = data
        self.next = None

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return f"data: {self.value}"

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        count = 0
        while current.next != None:
            current = current.next
            count += 1
        return count

    def display(self):
        current = self.head
        items = []
        while current.next != None:
            current = current.next
            items.append(current.value)
        print(items)

    def get(self, index):
        if index >= self.length():
            print("index out of range")
            return
        current = self.head
        idx = 0
        while current.next != None:
            current = current.next
            if idx == index:
                return current.value
            idx += 1

    def remove(self, index):
        if index >= self.length():
            print("index out of range")
            return
        current = self.head
        idx = 0
        while current.next != None:
            last = current
            current = current.next
            if idx == index:
                last.next = current.next
                return
            idx += 1
            

    def __repr__(self):
        return f"head: {self.head}, tail: {self.tail}"


linkedlist = LinkedList()

linkedlist.add_to_tail(1)
linkedlist.add_to_tail(2)

linkedlist.display()

print(linkedlist.get(0))
print(linkedlist.get(1))

linkedlist.remove(1)

linkedlist.display()