# Singly Linked Lists
class SinglyNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


""" Below, each node is created independently with next=None by default. 
    They're just separate objects floating in memory - not connected yet. """

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

print(Head.next)  # None because nodes aren't linked yet. None has its own string representation.

""" Here we link the nodes. """
Head.next = A
A.next = B
B.next = C

print(Head.next)  # 3 because nodes are linked now. If __str__ is not overridden, it prints a memory address.
print(Head)  # Only prints head. If __str__ is not overridden, it prints a memory address.


# # Traverse the list - O(n)
# curr = Head
#
# while curr:
#     print(curr)
#     curr = curr.next


# Display linked list - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))


print(Head)  # Still only prints head. If __str__ is not overridden, it prints a memory address.
display(Head)  # A way to display the whole list


# Search for node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False


print(search(Head, 2))

"""
NOTES:
None is a special built-in Python object that has its own string representation already defined. 
When you print None, Python automatically displays it as the text "None" - no custom __str__ method needed.

Why the node objects print as memory addresses:
When you create custom objects (like your SinglyNode instances), Python doesn't know how you want them displayed. 
Without a custom __str__ method, it falls back to the default representation (a memory address):
"""

