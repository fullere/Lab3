# Elizabeth Fuller
# 2/20/20
# driver file

from linkedlist import SinglyLinkedList

# creates a singly linked list head
new_list = SinglyLinkedList()
print(new_list)
# adds new nodes to the start of the list
new_list.prepend(5)
new_list.prepend(6)
new_list.prepend('ko')
new_list.prepend('5 Elements')

print(new_list)
