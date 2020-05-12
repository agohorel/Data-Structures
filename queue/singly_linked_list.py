class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"{self.value}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"{self.head}"

    def __len__(self):
        if not self.head:
            return 0
        else:
            current = self.head
            count = 0
            while current != None:
                current = current.get_next()
                count += 1
            return count

    def display(self):
        arr = []
        current = self.head
        while current != None:
            arr.append(current.value)
            current = current.get_next()
        print(arr)

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head

            while current.get_next() != None:
                current = current.get_next()

            current.set_next(new_node)

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.get_next()
            current.next = new_node

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            prev_head = self.head.get_value()
            self.head = self.head.get_next()
            return prev_head

    def remove_from_tail(self):
        if self.head == None:
            return None
        elif self.head.get_next() == None:
            temp = self.head
            self.head = None
            return temp
        else:
            current = self.head
            prev = current
            while current.get_next() != None:
                prev = current
                current = current.get_next()
            prev.set_next(None)
            return current.value
