# Elizabeth Fuller
# 2/20/20
# linked lists class


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        self.head = Node(data=data, next=self.head)

    def add_to_end(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_from_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_from_end(self):
        current = self.head
        previous = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        return current.data

    def clear(self):
        self.head = None

    def search(self,value):
        curr = self.head
        while curr.next:
            if curr.data == value:
                return True
            curr = curr.next
        if curr.data == value:
                return True
        else:
            return False

    def remove(self,value):
        curr = self.head
        prev = self.head
        if self.head.data == value:
            self.head = self.head.next
            return curr.data
        while curr.data == value or curr.next:
            if curr.data == value:
                prev.next = curr.next
                return curr.data
            prev = curr
            curr = curr.next
