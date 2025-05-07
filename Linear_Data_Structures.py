import os
import time

from collections import deque

#Stacks
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
element = stack.pop()      # Pop (removes 3)
print(stack)
print(element)
print(stack[-1]) #last element in the stack
print("-----------------")

#Queues
queue = deque()
queue.append(0)
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
element2 = queue.popleft()  # Dequeue (removes 0)
print(queue)
print(element2)
print(queue[0])


for i in range(2):
    print(f"Count: {i}")
    time.sleep(1)  # Wait for 1 second
print("LinkedLists")
time.sleep(1)


#LinkedLists
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

#Traverse the list - O(n)

curr = Head

while curr:
    print(curr)
    curr = curr.next


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))


display(Head)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False


print(search(Head, 2))
print(search(Head, 9))
print(search(Head, 7))

input("You want to continue ? ")


#Doubly Linked Lists
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)
print(head)
print(tail)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('<->'.join(elements))

display(head)


# Insert at the beginning of the list
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)  # Create new node and set it as the new head
    if head:
        head.prev = new_node  # Make the old head point back to the new node
    return new_node, tail  # New head, and tail stays the same

head, tail = insert_at_beginning(head, tail, 3)

display(head)

def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)  # Create new node and set it as the new tail
    if tail:
        tail.next = new_node  # Make the old tail point to the new node
    return head, new_node  # Head stays the same, new node becomes the new tail


def insert_after(node, val):
    new_node = DoublyNode(val)

    # Link the new node to the list
    new_node.next = node.next  # New node's next points to the node after current
    new_node.prev = node  # New node's prev points to current node

    if node.next:  # If there's a node after the current node
        node.next.prev = new_node  # Update the previous pointer of the node after current
    node.next = new_node  # Update the next pointer of the current node

    return new_node  # Return the newly inserted node

def insert_before(node, val):
    new_node = DoublyNode(val) #create the new node

    #link the new_node to the place
    new_node.next = node
    new_node.prev = node.prev

    if node.prev:
        node.prev.next = new_node
    node.prev = new_node

    return new_node





head, tail = insert_at_end(head, tail, 7)

display(head)
print(tail.next)


node_to_insert_after = head.next  # Node with value 3
new_node = insert_after(node_to_insert_after, 4)
print("\nAfter Inserting 4 After Node 3:")
display(head)

node_to_insert_before = head.next.next
new_node = insert_before(node_to_insert_before, 2)
print("\nAfter Inserting 2 before Node 4:")
display(head)

