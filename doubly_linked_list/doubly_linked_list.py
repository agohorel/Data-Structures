"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        list_str = ''
        curr = self.head
        while curr is not None:
            flags = ''
            if curr is self.head:
                flags += '[H]'
            if curr is self.tail:
                flags += '[T]'
            list_str += f'{curr.prev} <-- {flags}{curr} --> {curr.next}\n'
            curr = curr.next
        return list_str

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # set new node's next to old head
            new_node.next = self.head
            # set old head's prev to new node
            self.head.prev = new_node
            # update head
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return
        # if there is only one element
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            # save ref to old head
            temp = self.head
            # set head to it's .next
            self.head = self.head.next
            # set new head's .prev to none
            self.head.prev = None
            self.length -= 1
            return temp.value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # update old tail's next to new node
            self.tail.next = new_node
            # set new node's prev to old tail
            new_node.prev = self.tail
            # update tail
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.head is None:
            return
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return temp.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if self.head == node:
            return
        if self.tail == node:
            # get reference to new tail (second to last)
            new_tail = self.tail.prev
            # delete prev/next on existing tail
            self.tail.delete()
            # set old head's prev to tail node we wish to move (new head)
            self.head.prev = node
            # set new head's next to the old head
            node.next = self.head
            # set new head
            self.head = self.tail
            # set new tail
            self.tail = new_tail

        else:
            # current = self.head
            # while current != None:
            #     current = current.next
            #     if current == node:
            #         current.delete()
            #         self.head.prev = current
            #         current.next = self.head
            #         self.head = current
            self.add_to_head(node.value)
            self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.tail == node:
            return
        else:
            self.add_to_tail(node.value)
            self.delete(node)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.head == node:
            new_head = self.head.next
            new_head.prev = None
            self.head.delete()
            self.head = new_head
            self.length -= 1
        elif self.tail == node:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail.delete()
            self.tail = new_tail
            self.length -= 1
        else:
            # traverse list and find match, then call delete on it
            current = self.head
            while current.next != None:
                current = current.next
                if current == node:
                    current.delete()
                    self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.head is None:
            return None
        else:
            record = 0
            current = self.head
            while current:
                if current.value > record:
                    record = current.value
                current = current.next
            return record

    def display(self):
        arr = []
        current = self.head
        while current:
            arr.append(current)
            current = current.next
        print(arr)


ll = DoublyLinkedList(ListNode(1))

ll.add_to_tail(2)
ll.add_to_tail(3)
print(ll)
ll.display()

ll.move_to_end(ll.tail.prev)
print(ll)
ll.display()


