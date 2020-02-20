# Elizabeth Fuller


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,data):
        self.head = ListNode(data=data, next=self.head)
