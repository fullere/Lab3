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
        return '['+', '.join(nodes) + ']'

    def prepend(self,data):
        self.head = Node(data=data, next=self.head)
