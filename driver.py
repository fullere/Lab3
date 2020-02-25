# Elizabeth Fuller
# 2/20/20
# driver file

from linkedlist import SinglyLinkedList

# creates a singly linked list head
print("Lets make a linked list:")
new_list = SinglyLinkedList()
print(new_list)
# adds new nodes to the start of the list
print("Lets add 5, 6, 7, and 8 to the head of the list")
new_list.prepend(5)
new_list.prepend(6)
new_list.prepend(7)
new_list.prepend(8)
print("Lets add 'ko' and '5 Elements' to the end of the list")
new_list.add_to_end('ko')
new_list.add_to_end('5 Elements')
print("Here is the list now")
print(new_list)

print(new_list.remove_from_head())
print("Here is the list now")
print(new_list)

print(new_list.remove_from_end())
print("Here is the list now")
print(new_list)

print("Lets find out if 5 is in the list")
print(new_list.search(5))
print("Lets find out if 10 is in the list")
print(new_list.search(10))

print("Lets remove the number 6 from the list")
print(new_list.remove(6))
print("Here is the list now")
print(new_list)

print("Lets remove the number 7 from the list")
print(new_list.remove(7))
print("Here is the list now")
print(new_list)

print("Lets clear the list:")
new_list.clear()
print(new_list)
